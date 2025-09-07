# Number Guessing Game
import random

print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

# Generate random number
secret_number = random.randint(1, 100)
guess = None
attempts = 0

# Loop until correct guess
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
