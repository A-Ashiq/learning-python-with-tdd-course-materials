import math


class Circle:
    pi = math.pi

    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return self.pi * self.radius ** 2

    @property
    def circumference(self) -> float:
        return 2 * self.pi * self.radius
