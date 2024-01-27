import math

from src.classes import Circle


class TestCircle:
    def test_pi_as_class_attribute(self):
        """
        Given the `Circle` class
        When the `pi` attribute is accessed
        Then the correct value is returned
        """
        # Given / When
        pi = Circle.pi

        # Then
        assert pi == math.pi

    def test_diameter_as_instance_attribute(self):
        """
        Given the `Circle` class
        When the `diameter` attribute is accessed
        Then the correct value is returned
        """
        # Given
        diameter = 2.5

        # When
        circle = Circle(diameter=diameter)

        # Then
        assert circle.diameter == diameter
