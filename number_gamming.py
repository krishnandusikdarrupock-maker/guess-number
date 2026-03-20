import random

num = random.randint(1, 50)

print("Guess the number between 1 to 50")

while True:
    guess = int(input("Enter number: "))

    if guess == num:
        print("You win!")
        break
    elif guess > num:
        print("Too high")
    else:
        print("Too low")