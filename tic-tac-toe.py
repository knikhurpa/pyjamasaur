import random

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

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

    while not (marker == 'X' or marker == 'Y'):
        marker = input("Player 1: Choose your marker (x or y): ").upper()

        if not (marker == 'X' or marker == 'Y'):
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