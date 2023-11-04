### MILESTONE 3
import random

word_list = ["Apple", "Orange", "Kiwi", "Blueberries", "Raspberries"]

word = random.choice(word_list)

guess = input("What letter would you like to guess?")

# This code will continuously ask the user for a letter and validate it.
while True:
    guess = input("What letter would you like to guess?")
    if len(guess) != 1 or guess.isalpha == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        break

if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    "Sorry, {guess} is not in the word. Try again."

