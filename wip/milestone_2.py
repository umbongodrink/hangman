import random
from string import ascii_letters as valid_letters


# Define a list of words from which to start the game.
# In this instance, the set of words will be the author's five favourite fruits.
word_list = ["Apple", "Orange", "Kiwi", "Blueberries", "Raspberries"]

# Select a word from the list at random.
word = random.choice(word_list)

# Validate that a word was selected
print(word)

# As player1 to guess a single letter
guess = input("What letter would you like to guess?")


# Check to see if player1's guess is valid: is it a single letter? 

# <Long version>
#if len(guess) == 1 and guess in valid_letters:
#    print("Good guess!")
#else:
#    print("Oops! That is not a valid input.")

### <Short version, Refactor #1>
print("Good guess!") if len(guess) == 1 and guess in valid_letters else print("Oops! That is not a valid input.")

### <function created, Refactor #2>
#def guess_response(guess):
#    return print("Good guess!") if len(guess) == 1 and guess in valid_letters else print("Oops! That is not a valid input.")