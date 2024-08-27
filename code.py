board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

player = 'x' #player 1 is x, player 2 is o
gameOver = False

def play():
    global player
    turn = False
    while not turn:
        rowmove = int(input('what row would you like to place in? ')) #asks player to choose position
        columnmove = int(input('what column would you like to place in? '))
        if board[rowmove][columnmove] == None: #checks if position is empty
            board[rowmove][columnmove] = player
            turn = True
        else:
            print('sorry, space taken :(')

    if player == 'x': #switches players
        player = 'o'
    elif player == 'o':
        player = 'x'


def check():
    global gameOver
    empty = 0
    for row in board:
        for column in row:
            if column == None:
                empty += 1 #count number of empty spaces left
    
    if empty == 0: #if no empty spaces, game is over
        print('game over')
        gameOver = True

    if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x': #checks all winning combos
        print('player 1 wins!')
        gameOver = True
    elif board[0][0] == 'o' and board[0][1] == 'o' and board[0][2] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[1][0] == 'x' and board[1][1] == 'x' and board[1][2] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[1][0] == 'o' and board[1][1] == 'o' and board[1][2] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[2][0] == 'x' and board[2][1] == 'x' and board[2][2] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[2][0] == 'o' and board[2][1] == 'o' and board[2][2] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[0][0] == 'x' and board[1][0] == 'x' and board[2][0] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[0][0] == '0' and board[1][0] == 'o' and board[2][0] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[0][1] == 'x' and board[1][1] == 'x' and board[2][1] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[0][1] == 'o' and board[1][1] == 'o' and board[2][1] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[0][2] == 'x' and board[1][2] == 'x' and board[2][2] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[0][2] == 'o' and board[1][2] == 'o' and board[2][2] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o':
        print('player 2 wins!')
        gameOver = True
    elif board[2][0] == 'x' and board[1][1] == 'x' and board[0][2] == 'x':
        print('player 1 wins!')
        gameOver = True
    elif board[2][0] == 'o' and board[1][1] == 'o' and board[0][2] == 'o':
        print('player 2 wins!')
        gameOver = True

def display(): #prints each row on a new line, displays like normal board
    for row in board:
        print(row, '\n')

def game():
    while not gameOver: #game runs until it's over
        display()
        play() #runs functions
        check()
game()
