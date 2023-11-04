### MILESTONE 3
import random

word_list = ["Apple", "Mango", "Kiwi", "Blueberries", "Raspberries"]
word_to_guess = random.choice(word_list)


# This function will check if player1's letter is in the chosen word.
def check_guess(guess):
    guess = guess.lower()
    if guess in word_to_guess:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

# This code will check if player1's guess if valid. 
def ask_for_input():
    while True:
        guess = input("What letter would you like to guess?")
        if len(guess) != 1 or guess.isalpha == False:
            print("Invalid letter. Please, enter a single alphabetical character. ")
        else:
            break
    
    # It then plays the game by calling the check_guess()function
    check_guess(guess)

# The game commences with the ask_for_input() function call.
ask_for_input()