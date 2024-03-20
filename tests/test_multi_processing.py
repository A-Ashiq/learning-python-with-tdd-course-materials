import time

from src.concurrency import (
    io_bound_operation,
    SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION,
)
from src.multi_processing import run_with_multiple_processes, cpu_bound_operation


class TestMultiprocessing:
    def test_multiprocessing_can_run_multiple_cpu_bound_operations(self):
        """
        Given a callable which performs an intensive CPU bound operation
        When `run_with_multiple_processes()` is called
            to run the callable with 10 processes
        Then the total elapsed time is reduced
            when compared to sequential execution
        """
        # Given
        start_time = time.time()
        number_of_processes = 10

        # When / Then
        run_with_multiple_processes(
            func=cpu_bound_operation, number_of_processes=number_of_processes
        )

        # Then
        end_time = time.time()
        elapsed_time: float = round(end_time - start_time, 2)
        print(f"Total execution took {elapsed_time}s")

    def test_running_multiple_cpu_bound_operations_sequentially(self):
        """
        Given a callable which performs an intensive CPU bound operation
        When the callable is executed 10 times
        Then the total elapsed time is greater
            when compared to parallel execution
        """
        # Given
        start_time = time.time()
        number_of_executions = 10

        # When / Then
        for i in range(number_of_executions):
            cpu_bound_operation(index=i)

        # Then
        end_time = time.time()
        elapsed_time: float = round(end_time - start_time, 2)
        print(f"Total execution took {elapsed_time}s")

    def test_multiprocessing_can_run_multiple_io_bound_operations(self):
        """
        Given a callable which emulates a long I/O operation
        When `run_with_multiple_processes()` is called
            to run the callable with 10 processes
        Then the total elapsed time is slightly greater
            than the time taken for 1 process to complete
        """
        # Given
        start_time = time.time()
        number_of_processes = 10

        # When
        run_with_multiple_processes(
            func=io_bound_operation, number_of_processes=number_of_processes
        )

        # Then
        end_time = time.time()
        elapsed_time: float = round(end_time - start_time, 2)

        time_taken_for_sequential_operations: int = (
            number_of_processes * SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION
        )
        assert (
            SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION
            <= elapsed_time
            < time_taken_for_sequential_operations
        )
