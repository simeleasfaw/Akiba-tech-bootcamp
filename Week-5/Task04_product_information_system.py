
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"Product: {self.name} | Price: ${self.price} | Quantity: {self.quantity}"


# Create three product objects.
p1 = Product("Laptop", 999.99, 5)
p2 = Product("Smartphone", 499.99, 10)
p3 = Product("Headphones", 89.50, 25)

print("==================================================")
print(p1)
print(p2)
print(p3)
print("==================================================")

print("Laptop total value:", p1.total_value())
print("Smartphone total value:", p2.total_value())
print("Headphones total value:", p3.total_value())
