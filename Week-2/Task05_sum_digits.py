number = int(input("Enter a number: "))

total = 0

while number > 0:
    digit = number % 10 # take the last digit
    total = total + digit  # add it
    number = number // 10 # remove the last digit

print("Sum of digits:", total)