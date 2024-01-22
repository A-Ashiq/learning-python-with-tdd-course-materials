import pytest

from src.error_handling import (
    divide_numbers,
    get_item_from_dict,
    FoodNotAvailableForBreedError,
    get_food_type_for_breed,
)


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

    def test_key_error_raised_will_return_fallback_value(self):
        """
        Given a dict and a key which does not exist in the dict
        When `get_item_from_dict()` is called
        Then the expected fallback value is be returned
        """
        # Given
        items = {}
        key = "abc"

        # When
        returned_item: str = get_item_from_dict(items=items, key=key)

        # Then
        assert returned_item == "N/A"

    def test_type_error_raised_will_return_alternative_value(self):
        """
        Given an incompatible argument of a list and a key
        When `get_item_from_dict()` is called
        Then the expected alternative value is returned
        """
        # Given
        items = []
        key = "abc"

        # When
        returned_item: str = get_item_from_dict(items=items, key=key)

        # Then
        assert returned_item == "Invalid"
