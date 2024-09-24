while True:
    guess = input('Enter a single letter: ')
    if len(guess) == 1 and guess.isalpha():
        print('Good guess!')
        break
    
    else:
        print('Invalid character. Please enter a single alphabetical character.')