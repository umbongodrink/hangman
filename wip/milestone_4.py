### MILESTONE 4
import random


class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word.lower()))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for _ in self.word:
                if _ == guess:
                    index_value = self.word.index(_)
                    print(index_value)
                    self.word_guessed[index_value] = guess
                    print(self.word_guessed)

    def ask_for_input(self):
        while True:
            guess = input("Please choose a letter...")
            print(guess)
            if len(guess) != 1 or guess.isalpha == False:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)