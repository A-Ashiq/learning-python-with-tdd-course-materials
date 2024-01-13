import pytest

from src.dicts import add_item_to_dict, get_item_from_dict


class TestDicts:
    def test_item_can_be_added(self):
        """
        Given an empty dictionary
        And a new key value pair to be added
        When `add_item_to_dict()` is called
        Then the returned dictionary contains the key-value pair
        """
        # Given
        items = {}
        new_key = "abc"
        new_value = 123

        # When
        items = add_item_to_dict(items=items, key=new_key, value=new_value)

        # Then
        assert new_key in items
        assert items[new_key] == new_value

    def test_items_are_deduplicated_when_added(self):
        """
        Given a dictionary which contains a key-value pair
        And a new key value pair of the same key
        When `add_item_to_dict()` is called
            for both key-value pairs
        Then the returned dictionary contains the 2nd value
        """
        # Given
        items = {}
        key = "abc"
        original_value = 123
        new_value = 456

        # When
        items = add_item_to_dict(items=items, key=key, value=original_value)
        assert items == {key: original_value}
        items = add_item_to_dict(items=items, key=key, value=new_value)

        # Then
        assert items == {key: new_value}

    def test_looking_up_non_existent_key_raises_error(self):
        """
        Given a dictionary and a non-existent key
        When `get_item_from_dict()` is called
        Then a `KeyError` is raised
        """
        # Given
        items = {}
        key = "abc"

        # When / Then
        with pytest.raises(expected_exception=KeyError):
            get_item_from_dict(items=items, key=key)
