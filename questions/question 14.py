class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return round(0.5 * self.base * self.height, 2)


base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

triangle = Triangle(base, height)

area = Triangle.calculate_area(triangle)

print(f"Area = {area}")

Base = float(input('Enter the base : '))
Height = float(input('Enter the height : '))

Area = (0.5 * Base * Height)
print(f'Area of the triangle is: {Area}')
