total = 0
even_count = 0
odd_count = 0

for i in range(10):
    number = int(input("Enter a number: "))

    total += number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    if i == 0:
        largest = number
        smallest = number
    else:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

average = total / 10

print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)
print("Average:", average)
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)