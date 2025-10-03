import os
import threading
import time

import numpy as np

from objectproxypool import ProxyPool


class catchtime:
    def __init__(self, verbose=False) -> None:
        self.verbose = verbose

    def __enter__(self):
        self.time = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.time = time.perf_counter() - self.time
        self.readout = f"Time: {self.time:.3f} seconds"
        if self.verbose:
            print(self)

    def __str__(self):
        return self.readout


class TestObject:
    def test_method(self, argument):
        threadId = threading.get_native_id()
        pid = os.getpid()
        sleeptime = argument % 3
        if not argument:
            sleeptime += np.random.rand() > 0.5
        time.sleep(sleeptime)
        return threadId, pid, argument, sleeptime


class TestObject2:
    def __init__(self):
        self.arg = -1

    def test_method(self, argument):
        tmp = self.arg
        self.arg = argument
        sleeptime = argument % 3
        time.sleep(sleeptime)
        pid = os.getpid()
        threadId = threading.get_native_id()
        return (tmp, argument)


def test_synchronization_by_task():
    for argument in (0, range(os.cpu_count())):
        map_args = hasattr(argument, "__iter__")
        for separate_processes in True, False:
            with ProxyPool(TestObject, separate_processes=separate_processes) as pool:
                results = np.array(
                    pool.test_method(
                        argument, map_args=map_args, synchronize_workers=True
                    )
                )
            assert np.unique(results[:, 0]).size == os.cpu_count()

    return True


def test_synchronization_by_worker():
    worker_count = os.cpu_count()
    for argument in (0, range(worker_count)):
        map_args = hasattr(argument, "__iter__")
        for separate_processes in False, True:
            with ProxyPool(
                TestObject2,
                separate_processes=separate_processes,
                dedicated=True,
                worker_count=worker_count,
            ) as pool:
                results1 = pool.test_method(argument, map_args=map_args)
                results2 = pool.test_method(argument, map_args=map_args)
                results3 = pool.test_method(argument, map_args=map_args)
                pool.test_method(0)
            assert (results1[:, 1] == results2[:, 0]).all()
            assert (results2[:, 1] == results3[:, 0]).all()

    return True


def time_me(separate_processes, synchronize):
    with ProxyPool(TestObject, separate_processes=separate_processes) as pool:
        pool.test_method(1e-5, synchronize_workers=synchronize)


def test_speed():
    for synchronize in False, True:
        for separate_processes in False, True:
            with catchtime() as timer:
                time_me(separate_processes, synchronize)

            print(
                "sync. = {}, sep. proc. = {}".format(synchronize, separate_processes),
                timer,
            )


if __name__ == "__main__":
    print(
        "Test synchronization by worker was successful:",
        test_synchronization_by_worker(),
    )
    print(
        "Test synchronization by task was successful:", test_synchronization_by_task()
    )
    test_speed()
