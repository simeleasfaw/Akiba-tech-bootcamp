def check_minimum_length(password, min_length):
    return len(password) >= min_length


def check_uppercase(password):
    return any(char.isupper() for char in password)


def check_lowercase(password):
    return any(char.islower() for char in password)


def check_digits(password):
    return any(char.isdigit() for char in password)


def check_special_characters(password):
    return any(not char.isalnum() and not char.isspace()
               for char in password)

def analyze_password(password, min_length=8):

    report = {
        "Minimum Length": check_minimum_length(password, min_length),
        "Uppercase Letters": check_uppercase(password),
        "Lowercase Letters": check_lowercase(password),
        "Digits": check_digits(password),
        "Special Characters": check_special_characters(password)
    }

    return report

passwords = [
    "hello",
    "Hello123",
    "HELLO123!",
    "hello123!",
    "Hello@123"
]


for password in passwords:

    print("\nPassword:", password)

    result = analyze_password(password)

    for requirement, status in result.items():

        if status:
            print(requirement, ": PASS")
        else:
            print(requirement, ": FAIL")

    if all(result.values()):
        print("Password Status: STRONG")
    else:
        print("Password Status: WEAK")

print("\n===== CUSTOM MINIMUM LENGTH =====")

result = analyze_password("Hello@123", 10)

for requirement, status in result.items():
    print(requirement, ":", "PASS" if status else "FAIL")
