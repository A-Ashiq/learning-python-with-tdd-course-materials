from src.sets import add_item_to_set, get_difference


class TestSets:
    def test_items_are_deduplicated(self):
        """
        Given multiple identical strings
        When they are added to a set
        Then the set only contains the 1 unique item
        """
        # Given
        items = set()
        duplicated_item = "a"

        # When
        for _ in range(5):
            items = add_item_to_set(items=items, item=duplicated_item)

        # Then
        assert len(items) == 1
        assert duplicated_item in items

    def test_get_difference(self):
        """
        Given 2 sets
        When `get_difference()` is called
        Then the returned set contains
            the difference of set A against set B
        """
        # Given
        main = {"a", "b"}
        secondary = set("b")

        # When
        difference: set = get_difference(main=main, secondary=secondary)

        # Then
        assert difference == {"a"}
