import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter your guess between 1 and {x}: "))
        if guess < random_number:
            print("The random number is larger than the guess.")
        elif guess > random_number:
            print("The random number is smaller than the guess.")
        elif guess == random_number:
            print(f"That's the correct guess! The number was {random_number}.")
        else:
            print("Error!")

guess(10)