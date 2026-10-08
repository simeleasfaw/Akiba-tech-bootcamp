secret_number = 8
attempts = 0

while attempts < 5:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    if guess == secret_number:
        print("Congratulations!")
        print("You get the number in", attempts, "attempts.")
        break
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")
else:
    print("Game Over!")