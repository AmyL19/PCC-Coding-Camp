# starter code for implementing tic-tac-toe
# HINTS:
#   - think about the types of the variables and functions
#   - don't be afraid to ask for help


def insertBoard(letter: str, pos: int, board: list):
    # write a function that takes
    #   in a letter (X or O),
    #   a position on the board,
    #   and the board itself
    # and returns the board with that space filled
    pass

def isSpaceFree(pos: int, board: list):
    # write a function that takes a position and the board
    # and returns true if that space is free and false otherwise
    pass

def playerMove(board: list, letter: str):
    # write a function that asks the player to make a move
    pos = input("choose a position: ")   # "3"
    # validates it to make sure it is a valid move
    # if the move is valid, then make it
    # if not, then ask the user to input another move

    # return the resulting board
    pass

def isWinner(board: list, letter: str):
    # write a function that takes in the board and a letter (X or O)
    # and checks whether that player has won the game
    # you will need to check if their are three consecutive occurences of
    # the letter on the board horizontally, vertically, or diagonally
    # return true if there is a win and false otherwise
    pass

def isBoardFull(board: list):
    # write a function that checks if all spaces on the board are full
    # return true if the board is full and false otherwise
    pass

def printBoard(board: list):
    # write a function that prints out the current state of the board
    pass

def main():
    # in the main function, you will need to:
        # print the rules of the game (optional)
        # ask the players to input their names (optional)
        # create an empty board
        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        # while the game is not over:
            # print the board
            # allow the next player to choose a square
            # check if that square is free
            # make the move
            # check if the game is over
        # when the game is over, print the outcome and end
    pass

# call the main function here to run the game