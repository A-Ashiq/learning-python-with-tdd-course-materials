from src.error_handling import divide_numbers


class TestErrorHandling:
    def test_divide_returns_fallback_value_for_invalid_string_input(self):
        """
        Given an integer and a string
        When `divide_numbers()` is called
        Then the expected fallback value is be returned
        """
        # Given
        x = 1
        invalid_input = "some-string"

        # When
        value = divide_numbers(x=x, y=invalid_input)

        # Then
        assert value == "N/A"

    def test_zero_division_error_returns_fallback_value(self):
        """
        Given 2 integers where the denominator is 0
        When `divide_numbers()` is called
        Then the expected fallback value is be returned
        """
        # Given
        x = 1
        y = 0

        # When
        value = divide_numbers(x=x, y=y)

        # Then
        assert value == "N/A"
