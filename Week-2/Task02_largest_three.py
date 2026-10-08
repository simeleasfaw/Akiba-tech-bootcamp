number1 = int(input("enter the first number: "))
number2 = int(input("enter the second number: "))
number3 = int(input("enter the third number: "))

if number1 > number2 and number1 > number3:
    print(f"{number1} is the largest number.")
elif number2 > number1 and number2 > number3:
    print(f"{number2} is the largest number.")
else:
    print(f"{number3} is the largest number.")