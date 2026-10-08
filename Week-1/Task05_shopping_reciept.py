Customer_name = input("Enter customer name: ")
Product1 = input("Enter first product name: ")
Product2 = input("Enter second product name: ")
Price1 = float(input("Enter first product price: "))
Price2 = float(input("Enter second product price: "))
Quantity1 = int(input("Enter first product quantity: "))
Quantity2 = int(input("Enter second product quantity: "))


total_price1 = Price1 * Quantity1
total_price2 = Price2 * Quantity2
print("==========================================")
print("           RECIEPT               ")
print("==========================================")

print(f"\nCustomer: {Customer_name}")
print("-" * 40)

print(f"{'Product':<16}{'Price':<12}{'Qty':<5}")
print("-" * 40)

print(f"{Product1:<16}{Price1:<12}{Quantity1:<5}")
print(f"{Product2:<16}{Price2:<12}{Quantity2:<5}")

print("-" * 40)
print(f"{'Total:':<16}{total_price1 + total_price2:.2f} ETB")
print("Thank you for shopping!")
print("===========================================")