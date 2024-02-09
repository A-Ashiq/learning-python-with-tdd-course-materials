import math
from typing import Self


class Circle:
    pi = math.pi

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return self.pi * self.radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * self.pi * self.radius


class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    @staticmethod
    def calculate_perimeter(length: float, width: float) -> float:
        return 2 * (length + width)

    @classmethod
    def create_square(cls, length: float) -> Self:
        return Rectangle(length=length, width=length)

    def calculate_area(self) -> float:
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length: float):
        super().__init__(length=length, width=length)
