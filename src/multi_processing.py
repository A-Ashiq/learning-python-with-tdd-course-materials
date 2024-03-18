from multiprocessing.pool import Pool

from typing import Callable


def run_with_multiple_processes(func: Callable, number_of_processes: int) -> None:
    print(f"Creating pool of {number_of_processes} processes")
    indexes = [i for i in range(number_of_processes)]
    with Pool(processes=number_of_processes) as pool:
        pool.map(func, indexes)
