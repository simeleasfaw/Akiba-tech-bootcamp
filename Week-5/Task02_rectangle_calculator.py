class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width})"
    
rectangle1 = Rectangle(5, 3)
r2 = Rectangle(10, 4)

print(f"rectangle1: {rectangle1}")

print(f"Area of rectangle1: {rectangle1.area()}")
print(f"Perimeter of rectangle1: {rectangle1.perimeter()}")

print(f"rectangle2: {r2}")

print(f"Area of rectangle2: {r2.area()}")
print(f"Perimeter of rectangle2: {r2.perimeter()}")