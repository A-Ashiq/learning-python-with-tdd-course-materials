import math

from src.classes import Circle, Rectangle, Square


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

    def test_radius_as_instance_attribute(self):
        """
        Given the `Circle` class
        When the `radius` attribute is accessed
        Then the correct value is returned
        """
        # Given
        radius = 2.5

        # When
        circle = Circle(radius=radius)

        # Then
        assert circle.radius == radius

    def test_circumference_as_property(self):
        """
        Given a radius of 2.5
        When the `circumference` property is accessed
            from an instance of a `Circle`
        Then the correct value of 15.71 is returned
        """
        # Given
        radius = 2.5

        # When
        circle = Circle(radius=radius)

        # Then
        assert circle.circumference == 2 * math.pi * radius

    def test_calculate_area_as_instance_method(self):
        """
        Given a radius of 2.5
        When `calculate_area()` is called
            from an instance of a `Circle`
        Then the correct value of 19.63 is returned
        """
        # Given
        radius = 2.5
        circle = Circle(radius=radius)

        # When
        area = circle.calculate_area()

        # Then
        assert area == math.pi * radius**2


class TestRectangle:
    def test_calculate_perimeter(self):
        """
        Given a length of 2.5 and width 1
        When the `calculate_perimeter()` method
            is called from the `Rectangle` class
        Then the correct value is returned
        """
        # Given
        length = 2.5
        width = 1.0

        # When
        perimeter: float = Rectangle.calculate_perimeter(
            length=length,
            width=width,
        )

        # Then
        assert perimeter == 2 * (length + width)

    def test_create_square(self):
        """
        Given a length of 2.5
        When the `create_square()` class method
            is called from the `Rectangle` class
        Then a `Rectangle` instance is returned
            with equal length and widths
        """
        # Given
        length = 2.5

        # When
        square = Rectangle.create_square(
            length=length,
        )

        # Then
        assert square.length == square.width == length


class TestSquare:
    def test_calculate_area(self):
        """
        Given a length of 2.5
        When the `calculate_area()` method
            is called from the `Square` class
        Then the correct value is returned
        """
        # Given
        length = 2.5
        square = Square(length=length)

        # When
        area: float = square.calculate_area()

        # Then
        assert area == length * length