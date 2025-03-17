import random

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    number = random.randint(1, 100)
    guess = 0
    while guess != number:
        guess = int(input("Enter your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
    print("Congratulations! You guessed the number!")
    
game()