import random

#test_board = ['#', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X', 'O']

# function to display tic-tac-toe board
def display_board(board):
    print('\n'*100)
    print(f'''
    {board[7]} | {board[8]} | {board[9]}
    ---------
    {board[4]} | {board[5]} | {board[6]}
    ---------
    {board[1]} | {board[2]} | {board[3]}
    ''')

# test 1
# display_board(board)

# function to take marker input and assign it to the player
def player_input():
    '''
    OUTPUT = (Player 1 marker, Player 2 marker)
    '''
    
    marker = None

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1: Choose your marker (x or o): ").upper()

        if not (marker == 'X' or marker == 'O'):
            print('Invalid input!')
    
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# test 2
# player1_marker, player2_marker = player_input()
# print(f'Plauyer 1 marker is {player1_marker} and Player 2 marker is {player2_marker}')

# function to put marker on board

def place_marker(board, position, marker):
    board[position] = marker

# test 3
# place_marker(board, 3, 'X')
# display_board(board)

# function to chewck if specific marker has won

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark)                    
            )

# test4 
# display_board(test_board)
# print(win_check(test_board, '#'))

# write function to randomly decide which player goes first

def choose_first():
    first_move = random.randint(1, 2)

    if first_move == 1:
        return 'Player 1'
    else:
        return 'Player 2'
    
# write function to check if space on the board is freely available
def space_check(board, position):
    return board[position] == ' '

# write function to check if board is full
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False # board is not full
    return True # board is full

# write function to ask player for next position and check if it's free
def player_choice(board):
    position = None

    while not (position in range(1,10) and space_check(board, position)):
        position = int(input('Choose a position (1-9): '))

        if not position in range(1,10):
            print('Invalid input!')
        elif not space_check(board, position):
            print("Selected position is not empty! Choose another position!")

    return position

# write function to ask player if they want to play again
def replay():
    choice = input("Play again? ('y' or 'n'): ")

    return choice == 'y'

# Final game logic
# while loop to keep the game running
print('Welcome to Tic Tac Toe')

while True:
    # set eveything up (Board, Who's first, choose markers X O)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(f'{turn} will go first')

    play_game = input("Ready to play? (y or n): ")

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # play the game
    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on position
            place_marker(the_board, position, player1_marker)
            # check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won!')
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game!')
                game_on = False
            else:
                turn = 'Player 2'
            # check if there is tie
            # no tie and no win? then next player's turn
        else:
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place the marker on position
            place_marker(the_board, position, player2_marker)
            # check if won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won!')
                game_on = False
            elif full_board_check(the_board):
                display_board(the_board)
                print('Tie game!')
                game_on = False
            else:
                turn = 'Player 1'
            # check if there is tie
            # no tie and no win? then next player's turn

    if not replay():
        break
