import pytest


class TestGenerators:
    def test_items_are_yielded_until_exhausted(self):
        """
        Given an iterator of integers
        When `next()` is called continuously
        Then the next integers are returned
            until the iterator is exhausted
        """
        # Given
        iterator = (n for n in range(3))

        # When
        first_value = next(iterator)
        assert first_value == 0

        second_value = next(iterator)
        assert second_value == 1

        third_value = next(iterator)
        assert third_value == 2

        # Then
        with pytest.raises(StopIteration):
            next(iterator)

    def test_items_are_yielded_until_exhausted_from_function(self):
        """
        Given an iterator of integers as a function
        When `next()` is called continuously
        Then the next integers are returned
            until the iterator is exhausted
        """
        # Given
        def example_iterator():
            for i in range(3):
                yield i

        iterator = example_iterator()

        # When
        first_value = next(iterator)
        assert first_value == 0

        second_value = next(iterator)
        assert second_value == 1

        third_value = next(iterator)
        assert third_value == 2

        # Then
        with pytest.raises(StopIteration):
            next(iterator)
