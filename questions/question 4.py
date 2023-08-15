import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)


radius = float(input("Enter the radius of the circle: "))

circle = Circle(radius)

area = circle.calculate_area()

print(f"Area = {area}")
