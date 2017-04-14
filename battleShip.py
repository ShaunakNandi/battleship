from random import randint  #to generate a random number

board = []  #to store the ocean (O) and ship coordinates

for x in range(5):
    board.append(["O"] * 5) #creating a row vector with all Os (std. syntax)

def print_board(board):
    for row in board:
        print " ".join(row) #converts a list into a string ['O', 'O', 'O'] -> O O O
    print
    
print "In this game , you are to guess the coordinates \
of the battleShip. The coordinates of the same, follow matrix convention, namely, \
the top-left corner is indexed 00, below that is 10, so on...\
Let's play Battleship!"
print_board(board)
print 

def random_row(board):  #to generate a random integer from 0 to board-limit
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

chances = 7             #setting the number of guesses allowed
for turn in range(0, chances):
    print 'you\'re on turn number: %s' %(turn+1)
    print 'you have %s turns left!!! ' %(chances-turn)
    print
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean." #when guesses are off-limits
            
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
            
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            
        if turn == (chances-1):
            print 'Game Over! The battleShip was located at'
            print ship_row, ship_col
        
        print_board(board)
        print 
