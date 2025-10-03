import os
import sys
import threading
import warnings
from collections import deque
from copy import deepcopy
from functools import cached_property, partial
from itertools import count as itercount
from itertools import repeat, starmap
from multiprocessing import Manager, util
from multiprocessing.pool import (
    ExceptionWithTraceback,
    MaybeEncodingError,
    Pool,
    ThreadPool,
    _helper_reraises_exception,
)
from queue import Queue
from threading import Lock

import more_itertools
import numpy as np

MAX_WIN32_WORKERS = 61

INIT_COUNTER = itercount()


class lenzip:
    def __init__(self, *args) -> None:
        if not args:
            raise ValueError("lenzip takes at least one argument")
        self._args = args

    def __iter__(self):
        return zip(*self._args)

    def _classify_args(self):
        self._no_len_args_ = []
        self._min_len_ = np.inf
        for arg in self._args:
            if isinstance(arg, lenzip):
                self._min_len_ = min(self._min_len_, arg._min_len)
                self._no_len_args_ += arg._no_len_args
            elif hasattr(arg, "__len__"):
                self._min_len_ = min(self._min_len_, len(arg))
            else:
                self._no_len_args_.append(arg)

    @cached_property
    def _min_len(self):
        self._classify_args()
        return self._min_len_

    @cached_property
    def _no_len_args(self):
        _ = self._min_len  # invoke argument classification if necessary
        return self._no_len_args_

    @cached_property
    def _len(self):
        if self._no_len_args:
            if np.isfinite(self._min_len):
                iterable = zip(range(self._min_len), *self._no_len_args)
            else:
                iterable = zip(*self._no_len_args)

            try:
                return more_itertools.ilen(deepcopy(iterable))
            except TypeError:
                raise TypeError(
                    "Cannot determine the length of an unpickable object such as "
                    "a generator. Convert the argument to a list first."
                )
        else:
            return self._min_len

    def __len__(self):
        return self._len


class lenrepeat:
    def __init__(self, value, number):
        self._number = number
        self._value = value

    def __len__(self):
        return self._number

    def __iter__(self):
        return iter(repeat(self._value, self._number))


def get_chunks_iter(iterator, chunksizes, manager):
    iterator = iter(iterator)
    return (ManagedIterator(iterator, manager, limit) for limit in chunksizes)


class ResultManager:
    def __init__(self) -> None:
        self._resultIndices = deque()
        self._iteratorNumber = 0
        self._resultIterators = []
        self.lock = Lock()

    def register_input(self, *iterators):
        for iterator in iterators:
            iterator._id = self._iteratorNumber
            self._iteratorNumber += 1

    def add_result_id(self, resultID):
        self._resultIndices.append(resultID)

    def register_output(self, *iterators):
        for iterator in iterators:
            self._resultIterators.append(iter(iterator))

    def __next__(self):
        if not self._resultIndices:
            raise StopIteration()
        return next(self._resultIterators[self._resultIndices.popleft()])

    def __iter__(self):
        assert len(self._resultIterators) == self._iteratorNumber
        return self


class ManagedIterator:
    def __init__(self, iterator, manager, limit):
        self._index = 0
        self._iterator = iterator
        self._limit = limit
        self._id = None
        self._manager = manager
        manager.register_input(self)

    def __len__(self):
        return self._limit - self._index

    def __next__(self):
        with self._manager.lock:
            if not len(self):
                raise StopIteration()
            self._manager.add_result_id(self._id)
            self._index += 1
            return next(self._iterator)

    def __iter__(self):
        return self


def get_chunksizes(num, chunksize):
    result = np.zeros(num // chunksize + 1, dtype=int)
    result[:] = num // result.size
    result[: num % result.size] += 1
    return result


def get_chunksize_per_worker(num, workers):
    if hasattr(workers, "__iter__"):
        workers = list(workers)
        for i, w in enumerate(workers):
            if hasattr(w, "_processes"):
                workers[i] = w._processes
        worker_number = sum(workers)
        if len(workers) <= 1:
            workers = worker_number
    else:
        worker_number = workers

    result = np.full(worker_number, num // worker_number, dtype=int)
    result[: num % worker_number] += 1

    if hasattr(workers, "__iter__"):
        splits = np.cumsum([0] + workers)
        result = [
            sum(result[start:stop]) for start, stop in zip(splits[:-1], splits[1:])
        ]

    return result


def iterlen(iterable):
    """
    Returns the length of an iterable.
    WARNING! The iterator needs to be copied and evaluated,
             which may fail for generator objects. In these
             cases, convert the generator to a list first!
    """
    if hasattr(iterable, "__len__"):
        return len(iterable)
    else:
        try:
            return more_itertools.ilen(deepcopy(iterable))
        except TypeError:
            raise TypeError(
                "Cannot determine the length of an unpickable object such as "
                "a generator. Convert the argument to a list first."
            )


def object_mapstar(remote_object, args):
    return list(map(partial(args[0], remote_object), args[1]))


def object_starmapstar(remote_object, args):
    return list(starmap(partial(args[0], remote_object), *args[1:]))


def object_kwstarmapstar(remote_object, args):
    fun = args[0]
    return [
        fun(remote_object, *row[0][0], **dict(zip(row[1], row[0][1])))
        for row in args[1]
    ]


class _InitCounter(object):
    def __init__(self, pool, count, jobID=-1):
        self._pool = pool
        self._event = threading.Event()
        self._jobID = jobID
        self._cache = pool._cache
        self._cache[self._jobID] = self
        self.count = count

    def ready(self):
        return self._event.is_set()

    def wait(self, timeout=None):
        self._event.wait(timeout)

    def _set(self, i, obj):
        self._success, self._value = obj
        self.count -= 1
        if self.count <= 0:
            self._event.set()
            del self._cache[self._jobID]
            self._pool = None

    def get(self, timeout=None):
        self.wait(timeout)
        if self._success:
            return self._value
        else:
            raise self._value


class Value:
    def __init__(self, value):
        self.value = value


class Synchronizer(object):
    def __init__(self, worker_count, manager=None, timeout=None):
        self._worker_count = worker_count
        if not manager:
            self._status = Value(0)
            self._event = threading.Event()
        else:
            self._status = manager.Value("i", 0)
            self._event = manager.Event()
        self._timeout = timeout

    def ready(self):
        return self._event.is_set()

    def wait(self):
        self._event.wait(self._timeout)

    def set(self):
        self._status.value += 1
        if not self._status.value % self._worker_count:
            self._event.set()
        elif self.ready():
            self._event.clear()


class dedicatedFunction:
    def __init__(self, func, synchronizer):
        self._func = func
        self._synchronizer = synchronizer

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        self._synchronizer.set()
        self._synchronizer.wait()
        return result


class RLockProxy:
    def __init__(self, queues):
        self._rlocks = [q._rlock for q in queues]

    def acquire(self, *args, **kwargs):
        return all(r.acquire(*args, **kwargs) for r in self._rlocks)

    def release(self):
        any(r.release() for r in self._rlocks)


class QueueFamily:
    def __init__(self, count, QueueClass=None):
        self._len = count
        self._queues = [QueueClass() for _ in range(count)]
        self._in_queue_index = 0
        self._out_queue_index = 0
        if QueueClass is not Queue:
            self._rlock = RLockProxy(self._queues)

    def put(self, item):
        if item is None:
            for q in self._queues:
                q.put(item)
        else:
            self._queues[self._in_queue_index].put(item)
            self._next_in_queue()

    def reset(self):
        self._in_queue_index = 0
        self._out_queue_index = 0

    def _next_in_queue(self):
        self._in_queue_index = (self._in_queue_index + 1) % self._len

    def _next_out_queue(self):
        self._out_queue_index = (self._out_queue_index + 1) % self._len

    def _send(self, item):
        if item is None:
            for q in self._queues:
                q._writer.send(item)
        else:
            self._queues[self._in_queue_index]._writer.send(item)
            self._next_in_queue()

    def get(self, *args, **kwargs):
        item = self._queues[self._out_queue_index].get(*args, **kwargs)
        self._next_out_queue()
        return item

    def _recv(self):
        item = self._queues[self._out_queue_index]._reader.recv()
        self._next_out_queue()
        return item

    def assert_is_reset(self):
        assert self._in_queue_index == 0 and self._out_queue_index == 0, (
            f"QueueFamily not reset. in_queue_index={self._in_queue_index}, out_queue_index={self._out_queue_index}"
        )

    @property
    def _reader(self):
        result = self._queues[self._out_queue_index]._reader
        self._next_out_queue()
        return result

    def __iter__(self):
        yield from self._queues

    def __len__(self):
        return self._len


def worker(inqueue, outqueue, cls, init_args=(), maxtasks=None, wrap_exception=False):
    if (maxtasks is not None) and not (isinstance(maxtasks, int) and maxtasks >= 1):
        raise AssertionError("Maxtasks {!r} is not valid".format(maxtasks))
    put = outqueue.put
    get = inqueue.get
    if hasattr(inqueue, "_writer"):
        inqueue._writer.close()
        outqueue._reader.close()

    try:
        remote_object = cls(*init_args)
        result = (True, None)
    except Exception as e:
        if wrap_exception:
            e = ExceptionWithTraceback(e, e.__traceback__)
        result = (False, e)
        return
    finally:
        put((-1, 0, result))

    completed = 0
    while maxtasks is None or (maxtasks and completed < maxtasks):
        try:
            task = get()
        except (EOFError, OSError):
            util.debug("worker got EOFError or OSError -- exiting")
            break

        if task is None:
            util.debug("worker got sentinel -- exiting")
            break

        job, i, func, args, kwds = task
        try:
            result = (True, func(remote_object, *args, **kwds))
        except Exception as e:
            if wrap_exception and func is not _helper_reraises_exception:
                e = ExceptionWithTraceback(e, e.__traceback__)
            result = (False, e)
        try:
            put((job, i, result))
        except Exception as e:
            wrapped = MaybeEncodingError(e, result[1])
            util.debug("Possible encoding error while sending result: %s" % (wrapped))
            put((job, i, (False, wrapped)))

        task = job = result = func = args = kwds = None
        completed += 1
    util.debug("worker exiting after %d tasks" % completed)


# def distributedRemoteTask(task, *args, **kwargs):
#     threadID = threading.get_native_id()
#     return task(*(arg[threadID] for arg in args), **{kwarg[threadID] for kwarg in kwargs})


class _ObjectPoolExt:
    def __init__(self, processes, is_dedicated):
        if processes is None:
            processes = os.process_cpu_count() or 1
        self._is_dedicated = is_dedicated
        self._processes = processes

    def _repopulate_pool(self):
        if hasattr(self, "initCounter"):
            self.initCounter.count += self._processes - len(self._pool)
        else:
            self.initCounter = _InitCounter(self, self._processes - len(self._pool))
        return self._repopulate_pool_static(
            self._ctx,
            self.Process,
            self._processes,
            self._pool,
            self._inqueue,
            self._outqueue,
            self._initializer,
            self._init_args,
            self._maxtasksperchild,
            self._wrap_exception,
            is_dedicated=self._is_dedicated,
        )

    def _setup_queues(self):
        if hasattr(self, "_is_dedicated") and self._is_dedicated:
            QueueClass = (
                Queue if isinstance(self, ThreadPool) else self._ctx.SimpleQueue
            )
            self._inqueue = QueueFamily(self._processes, QueueClass)
            self._outqueue = QueueFamily(self._processes, QueueClass)
            if QueueClass is Queue:
                self._quick_put = self._inqueue.put
                self._quick_get = self._outqueue.get
            else:
                self._quick_put = self._inqueue._send
                self._quick_get = self._outqueue._recv
        else:
            super()._setup_queues()

    def _get_sentinels(self):
        if (
            not isinstance(self, ThreadPool)
            and hasattr(self, "_is_dedicated")
            and self._is_dedicated
        ):
            task_queue_sentinels = [q._reader for q in self._outqueue]
            self_notifier_sentinels = [self._change_notifier._reader]
            return [*task_queue_sentinels, *self_notifier_sentinels]
        else:
            return super()._get_sentinels()

    """
    Applies all calls to the pool to a number of object instances of given type
    """

    @staticmethod
    def _repopulate_pool_static(
        ctx,
        Process,
        processes,
        pool,
        inqueue,
        outqueue,
        initializer,
        init_args,
        maxtasksperchild,
        wrap_exception,
        is_dedicated=False,
    ):
        """Bring the number of pool processes up to the specified number,
        for use after reaping workers which have exited.
        """
        if is_dedicated:
            assert len(inqueue) == len(outqueue) == processes, (
                "If dedicated, all queues must have the same length"
            )
            queue_iter = zip(inqueue, outqueue)
        else:
            size = processes - len(pool)
            queue_iter = lenrepeat((inqueue, outqueue), size)

        for _inqueue, _outqueue in queue_iter:
            w = Process(
                ctx,
                target=worker,
                args=(
                    _inqueue,
                    _outqueue,
                    initializer,
                    init_args,
                    maxtasksperchild,
                    wrap_exception,
                ),
            )
            w.name = w.name.replace("Process", "PoolWorker")
            w.daemon = True
            w.start()
            pool.append(w)
            util.debug("added worker")

    def map(self, func, iterable, chunksize=None, synchronizer=None):
        """
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned.
        """
        return self.map_async(func, iterable, chunksize, synchronizer).get()

    def map_async(self, func, iterable, chunksize=None, synchronizer=None):
        """
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned.
        """
        if synchronizer:
            func = dedicatedFunction(func, synchronizer)
        return self._map_async_check_synchronization(
            func, iterable, object_mapstar, chunksize
        )

    def starmap(self, func, iterable, chunksize=None, synchronizer=None):
        """
        Like `map()` method but the elements of the `iterable` are expected to
        be iterables as well and will be unpacked as arguments. Hence
        `func` and (a, b) becomes func(a, b).
        """
        return self.starmap_async(func, iterable, chunksize, synchronizer).get()

    def starmap_async(self, func, iterable, chunksize=None, synchronizer=None):
        """
        Like `map()` method but the elements of the `iterable` are expected to
        be iterables as well and will be unpacked as arguments. Hence
        `func` and (a, b) becomes func(a, b).
        """
        if synchronizer:
            func = dedicatedFunction(func, synchronizer)
        return self._map_async_check_synchronization(
            func, iterable, object_starmapstar, chunksize
        )

    def kwstarmap(self, func, args, kwargs, chunksize=None, synchronizer=False):
        """
        Apply `func` to each element in `iterable`, collecting the results
        in a list that is returned.
        """
        return self.kwstarmap_async(func, args, kwargs, chunksize, synchronizer).get()

    def kwstarmap_async(self, func, args, kwargs, chunksize=None, synchronizer=False):
        """
        Apply `func` to each element in `iterable`
        """
        return self._kwstarmap_async(
            func,
            lenzip(args, lenzip(*kwargs.values())),
            tuple(kwargs.keys()),
            chunksize,
            synchronizer,
        )

    def _kwstarmap_async(self, func, args, keys, chunksize=None, synchronizer=False):
        """
        Apply `func` to each element in `iterable`
        """
        if synchronizer:
            func = dedicatedFunction(func, synchronizer)
        return self._map_async_check_synchronization(
            func,
            lenzip(args, lenrepeat(keys, iterlen(args))),
            object_kwstarmapstar,
            chunksize,
        )

    def _map_async_check_synchronization(
        self, func, iterable, mapper, chunksize=None, **kwargs
    ):
        if self._is_dedicated:
            self._inqueue.assert_is_reset()
            self._outqueue.assert_is_reset()

        if self._is_dedicated:
            if not hasattr(iterable, "__len__"):
                iterable = list(iterable)

            if not len(iterable) == self._processes:
                raise ValueError(
                    f"Length of iterable ({len(iterable)}) must match the number of workers ({self._processes}) if the pool is dedicated."
                )

            if chunksize not in (None, 1):
                raise ValueError("Chunksize must be 1 if the pool is dedicated.")

        return self._map_async(func, iterable, mapper, chunksize=chunksize, **kwargs)


class ObjectPool(_ObjectPoolExt, Pool):
    def __init__(self, processes=None, *args, dedicated=False, **kwargs):
        _ObjectPoolExt.__init__(self, processes, dedicated)
        Pool.__init__(self, self._processes, *args, **kwargs)


class ObjectThreadPool(_ObjectPoolExt, ThreadPool):
    def __init__(self, processes=None, *args, dedicated=False, **kwargs):
        _ObjectPoolExt.__init__(self, processes, dedicated)
        ThreadPool.__init__(self, self._processes, *args, **kwargs)


class DistributedPool:
    """
    Extension of Pool to circumvent the bug
    limiting the process count to 61 on Windows.
    """

    def __init__(self, worker_count=None):
        if worker_count is None:
            worker_count = os.cpu_count()

        self.distributed_pools = (
            worker_count > MAX_WIN32_WORKERS and sys.platform == "win32"
        )

        if not self.distributed_pools:
            self.pool = Pool(worker_count)
        else:
            self.pool = [
                Pool(num) for num in get_chunksizes(worker_count, MAX_WIN32_WORKERS)
            ]

        self.worker_count = worker_count

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def join(self):
        if self.distributed_pools:
            for pool in self.pool:
                pool.join()
        else:
            self.pool.join()

    def close(self):
        if self.distributed_pools:
            pools = self.pool
        else:
            pools = (self.pool,)

        for pool in pools:
            pool.close()
            pool.join()
            pool.terminate()

    def starmap(self, fun, args, **kwargs):
        if self.distributed_pools:
            result_manager = ResultManager()
            worker_chunks = get_chunksize_per_worker(iterlen(args), self.pool)
            results = [
                pool.starmap_async(fun, arg, **kwargs)
                for pool, arg in zip(
                    self.pool,
                    get_chunks_iter(args, worker_chunks, manager=result_manager),
                )
            ]
            result_manager.register_output(*(result.get() for result in results))
            return result_manager
        else:
            return self.pool.starmap(fun, args, **kwargs)

    def map(self, fun, args, **kwargs):
        if self.distributed_pools:
            worker_chunks = get_chunksize_per_worker(iterlen(args), self.pool)
            result_manager = ResultManager()
            results = [
                pool.map_async(fun, arg, **kwargs)
                for pool, arg in zip(
                    self.pool,
                    get_chunks_iter(args, worker_chunks, manager=result_manager),
                )
            ]
            result_manager.register_output(*(result.get() for result in results))
            return result_manager
        else:
            return self.pool.map(fun, args, **kwargs)


class ProxyPool:
    def __init__(
        self,
        cls,
        worker_count=None,
        init_args=(),
        separate_processes=False,
        dedicated=False,
        *,
        numWorkers=None,
        initargs=None,
        separateProcesses=None,
    ):
        if numWorkers is not None:
            warnings.warn(
                "The 'numWorkers' argument is deprecated. Use 'worker_count' instead.",
                DeprecationWarning,
            )
            if worker_count is None:
                worker_count = numWorkers
        if initargs is not None:
            warnings.warn(
                "The 'initargs' argument is deprecated. Use 'init_args' instead.",
                DeprecationWarning,
            )
            if init_args == ():
                init_args = initargs
        if separateProcesses is not None:
            warnings.warn(
                "The 'separateProcesses' argument is deprecated. Use 'separate_processes' instead.",
                DeprecationWarning,
            )
            if separate_processes is False:
                separate_processes = separateProcesses

        self._cls = cls

        if worker_count is None:
            worker_count = os.cpu_count()

        self.distributed_pools = (
            separate_processes
            and worker_count > MAX_WIN32_WORKERS
            and sys.platform == "win32"
        )

        if separate_processes:
            poolCls = ObjectPool
        else:
            poolCls = ObjectThreadPool

        if not self.distributed_pools:
            self.pool = poolCls(worker_count, cls, init_args, dedicated=dedicated)
            pools = [self.pool]
        else:
            self.pool = [
                poolCls(num, cls, init_args, dedicated=dedicated)
                for num in get_chunksizes(worker_count, MAX_WIN32_WORKERS)
            ]
            pools = self.pool

        for pool in pools:
            pool.initCounter.get()

        self.worker_count = worker_count

        if separate_processes:
            self.synchronizationManager = Manager()
        else:
            self.synchronizationManager = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def get_synchronizer(self, timeout=None):
        if timeout is not None and not timeout:
            return None
        return Synchronizer(self.worker_count, self.synchronizationManager, timeout)

    def join(self):
        if self.distributed_pools:
            for pool in self.pool:
                pool.join()
        else:
            self.pool.join()

    def close(self):
        if self.distributed_pools:
            pools = self.pool
        else:
            pools = (self.pool,)

        for pool in pools:
            pool.close()
            pool.join()
            pool.terminate()

    def _starmap(self, fun, args, synchronize_workers=False, **kwargs):
        if self.distributed_pools:
            worker_chunks = get_chunksize_per_worker(iterlen(args), self.pool)
            result_manager = ResultManager()
            synchronizer = self.get_synchronizer(synchronize_workers)
            results = [
                pool.starmap_async(fun, arg, synchronizer=synchronizer, **kwargs)
                for pool, arg in zip(
                    self.pool,
                    get_chunks_iter(args, worker_chunks, manager=result_manager),
                )
            ]
            result_manager.register_output(*(result.get() for result in results))
            return result_manager
        else:
            return self.pool.starmap(
                fun,
                args,
                synchronizer=self.get_synchronizer(synchronize_workers),
                **kwargs,
            )

    def _kwstarmap(self, fun, args, kwargs, synchronize_workers=False, **poolkwargs):
        if not kwargs:
            return self._starmap(
                fun, args, synchronize_workers=synchronize_workers, **poolkwargs
            )

        if self.distributed_pools:
            keys = tuple(kwargs.keys())
            kwargs = lenzip(*kwargs.values())

            if not args:
                task_length = len(kwargs)
                iter_args = lenzip(lenrepeat((), task_length), kwargs)
            else:
                iter_args = lenzip(args, kwargs)
                task_length = len(iter_args)

            worker_chunks = get_chunksize_per_worker(task_length, self.pool)

            result_manager = ResultManager()
            synchronizer = self.get_synchronizer(synchronize_workers)
            results = [
                pool._kwstarmap_async(
                    fun, arg, keys, synchronizer=synchronizer, **poolkwargs
                )
                for pool, arg in zip(
                    self.pool,
                    get_chunks_iter(iter_args, worker_chunks, manager=result_manager),
                )
            ]
            result_manager.register_output(*(result.get() for result in results))
            return result_manager
        else:
            return self.pool.kwstarmap(
                fun,
                args,
                kwargs,
                synchronizer=self.get_synchronizer(synchronize_workers),
                **poolkwargs,
            )

    def __getattr__(self, key):
        try:
            if isinstance(getattr(self._cls, key), staticmethod):
                return self._cls.key
        except AttributeError:
            pass

        def function_wrapper(
            *args,
            map_args=False,
            chunksize=None,
            synchronize_workers=False,
            stack_results=True,
            **kwargs,
        ):
            fun = getattr(self._cls, key)
            if map_args:
                result = list(
                    self._kwstarmap(
                        fun,
                        lenzip(*args),
                        kwargs,
                        chunksize=chunksize,
                        synchronize_workers=synchronize_workers,
                    )
                )
            else:
                if kwargs:
                    fun = partial(fun, **kwargs)
                result = list(
                    self._starmap(
                        fun,
                        lenrepeat(args, self.worker_count),
                        chunksize=chunksize,
                        synchronize_workers=synchronize_workers,
                    )
                )
            if result and isinstance(result[0], np.ndarray) and stack_results:
                return np.vstack(result)
            else:
                try:
                    return np.asarray(result)
                except:
                    return np.asarray(result, dtype=object)

        return function_wrapper
