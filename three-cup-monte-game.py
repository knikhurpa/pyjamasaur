from random import shuffle

def shuffle_list(mylist):
    print("Shuffling the ball...\n")
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2 => ")
    
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)

# Initial List
mylist = [' ', 'O', ' ']

# Welcome message
print('****Welcome to Three Cup Monte Game****\nGuess the location of the ball')
print(mylist)
print('  0    1    2\n')

# Shuffle List
mixedup_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
check_guess(mixedup_list, guess)
