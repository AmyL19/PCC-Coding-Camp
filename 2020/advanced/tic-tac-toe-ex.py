# starter code for implementing tic-tac-toe
# HINTS:
#   - think about the types of the variables and functions
#   - don't be afraid to ask for help

def insertBoard(letter, pos, board):
    # write a function that takes
    #   in a letter (X or O),
    #   a position on the board,
    #   and the board itself
    # and returns the board with that space filled
    board[pos] = letter
    return board

def spaceIsFree(pos, board):
    # write a function that takes a position and the board
    # and returns true if that space is free and false otherwise
    if (board[pos] == " "):
         return True
    return False

def playerMove(board, letter):
    # write a function that asks the player to make a move
    # validates it to make sure it is a valid move
    # if the move is valid, then make it
    # if not, then ask the user to input another move
    # return the resulting board
    pos = int(input("Make a move: "))
    while (True):
        if (spaceIsFree(pos, board)):
            return insertBoard(letter, pos, board)
        else:
            pos = int(input("That is not a valid move, please choose another space: "))
    return

def isWinner(board, letter):
    # write a function that takes in the board and a letter (X or O)
    # and checks whether that player has won the game
    # you will need to check if their are three consecutive occurences of
    # the letter on the board horizontally, vertically, or diagonally
    # return true if there is a win and false otherwise
    check = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    for (x, y, z) in check:
        if (board[x] == board[y] and board[y] == board[z] and board[z] == letter):
            return True
    return False

def isBoardFull(board):
    # write a function that checks if all spaces on the board are full
    # return true if the board is full and false otherwise
    for i in board:
        if i == " ":
            return False

    return True

def printBoard(board):
    # write a function that prints out the current state of the board
    print(f"""
            -------------
            | {board[0]} | {board[1]} | {board[2]} |
            -------------
            | {board[3]} | {board[4]} | {board[5]} |
            -------------
            | {board[6]} | {board[7]} | {board[8]} |
            -------------
        """)
    return

def main():
    # print the rules of the game (optional)
    print ("Hello there! This is tic-tac-toe. Get 3 in a row and you win!")
    # ask the players to input their names (optional)
    p1 = input("Player 1, what is your name? ")
    print ("Hello, " + p1 +" !")
    p2 = input("Player 2, what is your name? ")
    print ("Hello, " + p1 +" !")
    # create an empty board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    # while the game is not over:
    isGameOver = False
    currentPlay = "X"
    while(not isGameOver):
        # print the board
        printBoard(board)

        # have player make a move
        board = playerMove(board, currentPlay)

        # check if the game is over
        if (isWinner(board, currentPlay)):
            printBoard(board)
            print("Congrats, player " + ("1" if currentPlay == "X" else "2") + " you won!")
            isGameOver = True
            return
        if (isBoardFull(board)):
            printBoard(board)
            print("There was a tie!")
            isGameOver = True
            return
        if (currentPlay == "X"):
            currentPlay = "O"
        else:
             currentPlay = "X"

    return 1

# call the main function here to run the game
main()