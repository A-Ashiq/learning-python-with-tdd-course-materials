import logging
import threading
from multiprocessing.dummy import Pool as ThreadPool
import time
from typing import Callable

logger = logging.getLogger(__name__)


SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION = 5


def io_bound_operation(index: int) -> None:
    print(f"\nStarting io bound operation for thread number {index}")
    time.sleep(SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION)
    print(
        f"\nFinished io bound operation for thread number {index} in {SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION}s"
    )


def run_with_multiple_threads(func: Callable, number_of_threads: int) -> None:
    print(f"Creating pool of {number_of_threads} threads")
    indexes = [i for i in range(number_of_threads)]
    with ThreadPool(processes=number_of_threads) as pool:
        pool.map(func, indexes)


def run_with_multiple_threads_simple(func: Callable, number_of_threads: int) -> None:
    print(f"Creating pool of {number_of_threads} threads")
    indexes = [i for i in range(number_of_threads)]

    threads = [threading.Thread(target=func, args=(i,)) for i in indexes]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
