import random

word_list = ['apple', 'banana', 'orange', 'kiwi', 'mango']

print(word_list)

random_word = random.choice(word_list)
print(random_word)

def check_guess(guess):
    if guess in random_word:
        print(f'Good guess! {guess} is in the word!')

    else:
        print(f'Sorry, {guess} is not in the word. Try again.')

def ask_for_input():
    while True:
        guess = input('Enter a single letter: ').lower()
        if len(guess) == 1 and guess.isalpha():
            break
    
        else:
            print('Invalid character. Please enter a single alphabetical character.')
    
    check_guess(guess)

ask_for_input()
