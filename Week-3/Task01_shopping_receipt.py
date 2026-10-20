items = [
    {"name": "Notebook", "price": 80, "quantity": 3},
    {"name": "Pen", "price": 15, "quantity": 5}
]

def calculate_subtotal(items):
    total = 0
    for item in items:
        total += item["price"] * item["quantity"]
    return total
# print(calculate_subtotal(items))  

def calculate_discount(subtotal):
    if subtotal >= 3000:
        return subtotal * 0.1  
    if subtotal>=1000:
        return subtotal * 0.05  
    else:
        return 0  # No discount
# print(calculate_discount(345))  

def calculate_tax(amount, tax_rate):
    if amount <0:
        return "amount cannot be negative"
    if tax_rate < 0 or tax_rate > 100:
        return "tax rate must be between 0 and 100"
    tax = amount * (tax_rate / 100)
    return tax
# print(calculate_tax(345, 10))  

def generate_receipt(items, tax_rate):
    subtotal = calculate_subtotal(items)
    discount = calculate_discount(subtotal)
    total_after_discount = subtotal - discount
    tax = calculate_tax(total_after_discount, tax_rate)
    total_amount = total_after_discount + tax

    receipt = "Receipt:\n"
    for item in items:
        receipt += f"{item['name']} - {item['quantity']} x {item['price']} = {item['quantity'] * item['price']}\n"
    receipt += f"Subtotal: {subtotal}\n"
    receipt += f"Discount: {discount}\n"
    receipt += f"Total after discount: {total_after_discount}\n"
    receipt += f"Tax: {tax}\n"
    receipt += f"Total Amount: {total_amount}\n"

    return receipt
print(generate_receipt(items, 10))  