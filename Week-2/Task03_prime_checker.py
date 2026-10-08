number = int(input("Enter a number: "))

for i in range(2, number):
    if number % i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")