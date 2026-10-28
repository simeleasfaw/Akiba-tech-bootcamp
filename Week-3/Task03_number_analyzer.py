def is_prime(prime):
    if number < 2:
        return False
    
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def get_divisors(number):
    divisors = []
    
    
    for i in range(1, abs(number) + 1):
        if number != 0 and number % i == 0:
            divisors.append(i)

    return divisors


def sum_of_digits(number):
    number = abs(number)
    total = 0

    while number > 0:
        digit = number % 10
        total += digit
        number //= 10

    return total


def reverse_number(number):
    sign = -1 if number < 0 else 1
    number = abs(number)
    reversed_num = 0

    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number //= 10

    return reversed_num * sign


def analyze_number(number):
    analysis = {
        "number": number,
        "type": "Even" if number % 2 == 0 else "Odd",
        "is_prime": is_prime(number),
        "sum_of_digits": sum_of_digits(number),
        "reversed_number": reverse_number(number),
        "divisors": get_divisors(number)
    }

    return analysis


number = int(input("Enter a number: "))
result = analyze_number(number)

for key, value in result.items():
    print(f"{key}: {value}")