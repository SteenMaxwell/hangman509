import random

class Hangman():
    '''
    A play on the classic Hangman game, where the computer chooses a word and the user guesses 
    a letter to see if it is in this word.

    Methods:
    -------
    check_guess(guess)
        checks if the input guess is in the chosen word.
    
    ask_for_input()
        Asks the user to give a letter.
    '''
    
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
        '''
        Parameters:
        ----------
        word_list: list
            List of words to be used for the game
        num_lives: int
            The number of lives the user has

        Attributes:
        ----------
        word: str
            The word to be guessed picked randomly from the word_list
        word_guessed: list
            A list of the letters of the word, with '_' for each letter not yet guessed
        num_letters: int
            The number of UNIQUE letters in the word that have not been guessed yet
        list_letters: list
            A list of the letters that have already been tried
        '''

    def check_guess(self, guess):
        '''
        Checks of the input guess is in the chosen word.
        If it is, replaces '_' in word_guessed with the chosen letter.
        If it is not, user loses a life by -1.

        parameter:
        ---------

        guess: str
            The users input to be checked
        
        '''
    
        guess = guess.lower()
        if guess in self.word:
            print(f'Good Guess! {guess} is in the word!')
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = guess

            self.num_letters -= 1
        
        else:
            self.num_lives -= 1
            print(f'Sorry {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left!')


    def ask_for_input(self):
        '''
        Asks the user to give a letter and checks whether input is valid 
        and if letter has already been tried.
        If it passes both checks, the check_guess method is called.
        '''
        
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please enter a single alhpabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break


word_list = ['apple', 'banana', 'orange']
game = Hangman(word_list)
game.ask_for_input()
