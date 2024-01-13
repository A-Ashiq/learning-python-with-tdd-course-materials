class TestTuples:
    def test_assign_item(self):
        """
        Given a tuple of items
        When another item is assigned to the tuple
        Then a `TypeError` is raised
        """
        # Given
        items = "a", "b", "c"

        # When / Then
        items[3] = "d"

    def test_raise_error_when_item_is_assigned_after_instantiation(self):
        """
        Given a tuple of items
        When another item is assigned to the tuple
        Then a `TypeError` is raised
        """
        # Given
        items = "a", "b", "c"

        # When / Then
        with pytest.raises(TypeError):
            items[3] = "d"
