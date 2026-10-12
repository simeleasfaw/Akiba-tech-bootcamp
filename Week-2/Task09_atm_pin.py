correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    pin = input("Enter your PIN: ")
    attempts += 1

    if pin == correct_pin:
        print("PIN correct. Access granted.")
        break
    else:
        remaining = max_attempts - attempts
        print("Incorrect PIN.")
        print("Attempts remaining:", remaining)

if attempts == max_attempts and pin != correct_pin:
    print("Access denied.")