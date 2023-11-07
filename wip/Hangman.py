import random

class Hangman:
    ''' A Class to define objects that form a game of Hangman.
        The computer chooses a word at random from a pre-defined list.
        The player, who has a set number of lives then uses guesses of letters
        to try and figure-out the word. For every wrong guess, the player loses
        a life.
    

    Parameters:
    ----------
    word_list: list
        A list of five words used in the game.
    num_lives: int
        The number of lives (or guesses) the player has in the game. Default is 5.

    Attributes:
    ----------
    word: str
        The word to be guessed by the player. Chosen at random from the word_list.
    word_guessed: list
        A list of ('blank') strings, denoted by '_' underscores, that represent 
        unguessed letters in the word. As the player correctly guesses a letter,
        the blank string is replaced by the letter in the list.
    num_letters: int
        The number of unique letters in the word to be guessed.
    list_of_guesses: list
        An empty list that is populated by each letter guessed by the player

    Methods:
    -------
    check_guess(guess)
        Checks if the player's letter guess is in the word. 
        If it is, the player is informed of this, and the number of letters to
        be guessed is decreased. 
        If it is not, the player is informed of this, and the number of guesses
        or lives is decreased.

    ask_for_input()
        The game asks the player for a guess.
        If the player inputs a non-valid single alphanumeric letter, they are
        informed as such.
        Otherwise, the input is passed to the check_guess function.
    '''

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word.lower()))
        self.list_of_guesses = []

    def __check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, letter in enumerate(self.word):
                    if letter == guess:
                        self.word_guessed[index] = guess
            print(f"The state of the game is: {self.word_guessed}.")
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        guess = input("\nPlease choose a letter...")
        print(f"You guessed: {guess}.")
        if len(guess) != 1 or guess.isalpha == False:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.__check_guess(guess)
            self.list_of_guesses.append(guess)

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("\nYou lost!\U0001F623\n")
            break
        elif game.num_lives > 0 and game.num_letters == 0:
            print(f"\nCongratulations.\U0001F973 You won the game! The word was: '{game.word}'!\n")
            break
        elif game.num_letters > 0:
            game.ask_for_input()           
    response = input("Do you want to play again? [type yes/no] ")
    if response.lower() == "yes":
        play_game(word_list)
    elif response.lower() == "no":
        print("Thanks for playing!\U0001F609\n")
    else:
            print(
            "Sorry I didn't understand your response.\U0001F914 \
            \nThanks for playing.\
            \nBy the way, if you ever want to play again, just type ===> 'python3 Hangman.py'.\n")

if __name__ == "__main__":
    play_game(["apple", "mango", "kiwi", "blueberries", "raspberries"])
    
