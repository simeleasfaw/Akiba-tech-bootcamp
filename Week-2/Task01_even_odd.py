number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
elif number > 0:
    print(f"{number} is a positive number.")
    if number % 2 == 0:
        print("It is even")
    else:
        print("It is odd")
else:
    print("It is a negative number")
    if number % 2 == 0:
        print("It is even")
    else:
        print("It is odd")