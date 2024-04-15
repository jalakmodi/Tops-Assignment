import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * (self.radius ** 2)
        return round(area, 2)

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)

# Create a Circle object with a radius of 5
circle = Circle(5)

# Compute and print the area and perimeter of the circle
print("Area:", circle.area())
print("Perimeter:", circle.perimeter())