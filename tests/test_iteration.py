from src.iteration import print_all_items


class TestIteration:
    def test_loops_over_list(self):
        """
        Given a list of strings
        When `print_all_items()` is called
        Then each item is printed
        """
        # Given
        items = ["red", "blue", "green"]

        # When / Then
        print_all_items(items=items)

    def test_loops_over_dict(self):
        """
        Given a dict of strings
        When `print_all_items()` is called
        Then each item is printed
        """
        # Given
        items = {"red": 1, "blue": 2, "green": 3}

        # When / Then
        print_all_items(items=items)

    def test_loops_over_generator(self):
        """
        Given a generator of strings
        When `print_all_items()` is called
        Then each item is printed
        """
        # Given
        def iterator_of_items():
            yield "red"
            yield "blue"
            yield "green"

        items = iterator_of_items()

        # When / Then
        print_all_items(items=items)
