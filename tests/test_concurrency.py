import time

from src.concurrency import (
    io_bound_operation,
    run_with_multiple_threads,
    SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION,
)


class TestConcurrency:
    def test_multi_threading_can_run_multiple_io_bound_operations(self):
        """
        Given a callable which emulates a long I/O operation
        When `run_with_multiple_threads()` is called
            to run the callable with 10 threads
        Then the threads are executed concurrently
        And the total elapsed time is slightly greater
            than the time taken for 1 thread to complete
        """
        # Given
        start_time = time.time()
        number_of_threads = 10

        # When
        run_with_multiple_threads(
            func=io_bound_operation, number_of_threads=number_of_threads
        )

        # Then
        end_time = time.time()
        elapsed_time: float = round(end_time - start_time, 2)

        time_taken_for_sequential_operations: int = (
            number_of_threads * SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION
        )
        assert (
            SECONDS_TAKEN_FOR_SINGLE_IO_OPERATION
            <= elapsed_time
            < time_taken_for_sequential_operations
        )
