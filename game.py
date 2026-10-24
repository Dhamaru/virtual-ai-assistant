# game.py - Number guessing game with "higher" / "lower" hints.
import random

LOWEST, HIGHEST = 1, 20  # range of the secret number
MAX_TRIES = 5            # how many guesses the user gets


def play_guessing_game(name):
    secret = random.randint(LOWEST, HIGHEST)  # random whole number from 1 to 20
    print(f"Assistant: I'm thinking of a number between {LOWEST} and {HIGHEST}. You have {MAX_TRIES} tries.")

    tries_left = MAX_TRIES
    while tries_left > 0:
        try:
            guess = int(input("Guess a number: "))
        except ValueError:  # "abc" is not a number; ask again without using a try
            print("Assistant: That's not a whole number - try again.")
            continue

        tries_left = tries_left - 1
        if guess == secret:
            print(f"Assistant: Correct, {name}! You guessed it.")
            return
        elif guess < secret:
            print(f"Assistant: Go higher. Tries left: {tries_left}")
        else:
            print(f"Assistant: Go lower. Tries left: {tries_left}")

    print(f"Assistant: Out of tries! The number was {secret}. Better luck next time, {name}.")
