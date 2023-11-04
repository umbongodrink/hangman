### MILESTONE 3

"""This code will continuously ask the user for a letter and validate it."""

guess = input("What letter would you like to guess?")

while True:
    guess = input("What letter would you like to guess?")
    if len(guess) != 1 or guess.isalpha == False:
        print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        break

