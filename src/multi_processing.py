import logging
import time
from multiprocessing.pool import Pool
from random import randrange

from typing import Callable

logger = logging.getLogger(__name__)


def run_with_multiple_processes(func: Callable, number_of_processes: int) -> None:
    print(f"Creating pool of {number_of_processes} processes")
    indexes = [i for i in range(number_of_processes)]
    with Pool(processes=number_of_processes) as pool:
        pool.map(func, indexes)


def cpu_bound_operation(index: int) -> None:
    print(f"Starting CPU bound operation for process number {index}")
    number: int = randrange(10_000_000, 100_000_000)
    count(number=number)
    print(f"Finished CPU bound operation for process number {index}")


def count(number: int) -> None:
    start_time = time.time()

    result = 0

    while result < number:
        result += 1

    end_time = time.time()
    elapsed_time: float = round(end_time - start_time, 2)

    print(f"Finished counting to {number} in {elapsed_time}s")
