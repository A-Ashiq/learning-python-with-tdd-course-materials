from src.lists import (
    add_item_to_list,
    remove_item_from_list,
    add_list_to_list,
    get_index_of_item,
    insert_item_at_index,
    sort_items_in_list,
    count_items,
)


class TestLists:
    def test_add_item_to_list(self):
        """
        Given a list of integers and a new number to be added
        When `add_item_to_list()` is called
        Then the new number can be found in the list
        """
        # Given
        new_number = 4
        numbers = [1, 2, 3]

        # When
        new_numbers = add_item_to_list(items=numbers, item=new_number)

        # Then
        assert new_numbers == [1, 2, 3, 4]

    def test_remove_item_from_list(self):
        """
        Given a list of integers
        When `remove_item_from_list()` is called
        Then the item cannot be found in the list
        """
        # Given
        number_to_remove = 3
        numbers = [1, 2, number_to_remove]

        # When
        new_numbers = remove_item_from_list(items=numbers, item=number_to_remove)

        # Then
        assert new_numbers == [1, 2]

    def test_add_list_to_list(self):
        """
        Given 2 list of integers and
        When `add_list_to_list()` is called
        Then all the items in the 2nd list will be added
        """
        # Given
        main_list = [1, 2]
        items_to_be_added = [3, 4]

        # When
        new_numbers = add_list_to_list(
            items=main_list, items_to_be_added=items_to_be_added
        )

        # Then
        assert new_numbers == [1, 2, 3, 4]

    def test_get_index_of_item(self):
        """
        Given a list of strings
        When `get_index_of_item()` is called for a given string
        Then the correct index is returned
        """
        # Given
        items = ["a", "b", "c"]

        # When
        index = get_index_of_item(items=items, item="b")

        # Then
        assert index == 1

    def test_insert_item_at_index(self):
        """
        Given a list of items
        When `test_insert_item_at_index()` is called
            for a given item and index
        Then the item is added to the list at the given index
        """
        # Given
        items = ["a", "c", "d"]

        # When
        insert_item_at_index(items=items, index=1, item="b")

        # Then
        assert items == ["a", "b", "c", "d"]

    def test_sort_items_in_list(self):
        """
        Given a list of items
        When `sort_items_in_list()` is called on the list
        Then the items within the list are sorted
        """
        # Given
        items = ["b", "c", "a"]

        # When
        sort_items_in_list(items=items)

        # Then
        assert items == ["a", "b", "c"]

    def test_count_items(self):
        """
        Given a list of items
        When `count_items()` is called with the list
        Then an integer is returned representing the number of items
        """
        # Given
        items = ["b", "c", "a"]

        # When
        number_of_items = count_items(items=items)

        # Then
        assert number_of_items == 3
