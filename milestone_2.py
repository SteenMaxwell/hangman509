import random

word_list = ['apple', 'banana', 'orange', 'kiwi', 'mango']

print(word_list)

random_word = random.choice(word_list)
print(random_word)

guess = input('Enter a single letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')

else:
    print('Oops! That is not a valid input.')
    

