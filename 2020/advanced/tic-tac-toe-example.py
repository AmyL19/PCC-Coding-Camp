class TicTacToe(object):
  PLAYER = ["X", "O"]

  def __init__(self):
    self.board = Board()
    self.turn = 0

  def play(self):
    self.playerNames = self.start()
    self.run()

  @staticmethod
  def start():
    msg = "Press enter to continue"
    input(f"This is tic-tac-toe. {msg}")
    playerOneName = input(f"Player 1 will be X. Enter Player 1's name: ")
    playerTwoName = input(f"Player 2 will be O. Enter Player 2's name: ")
    input(f"Take turns playing on a 3x3 board until one player reaches 3 in a row. {msg}")
    input(
f"""For each turn, you will play by selecting the square you want to place in, shown below: 
{Board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])}
{msg}"""
    )
    input("Have fun!")
    return (playerOneName, playerTwoName)

  def run(self):
    winner = False
    while(not winner and self.board.hasEmptySquares()):
      print(self.board)
      self.makeMove()
      winner = self.checkForWin()
    self.announceWinner(winner)

  def checkForWin(self):
    def threeStraight(lst): 
      if lst[0] == lst[1] and lst[0] == lst[2] and lst[0] != 0: 
        return lst[0] 
      else: return False

    res = False
    for i in range(3):
      res = res or threeStraight(self.board.getRow(i)) or threeStraight(self.board.getCol(i))
    return res or threeStraight(self.board.getLeftDiag()) or threeStraight(self.board.getRightDiag())
    
  def announceWinner(self, winner):
    print(self.board)
    if winner == "X": 
      winnerName = self.playerNames[0] 
    elif winner == "O":
      winnerName = self.playerNames[1]
    else:
      self.tieGame()
      return
    print(f"{winnerName} has won!")

  def makeMove(self):
    inp = input("Select where to make your move: ")
    while(inp not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
      inp = input("Please choose a valid square. Select where to make your move: ")
    index = int(inp) - 1
    row = index // 3
    col = index % 3
    if self.board.squareIsEmpty(row, col):
      self.board.setSquare(row, col, TicTacToe.PLAYER[self.turn])
      self.turn = 1 - self.turn
    else:
      print("Square taken, try again.", end=" ")
      self.makeMove()

  def tieGame(): print("Game is tied.")
  

class Board(object):
  def __init__(self, board=None): 
    if board == None:
      self.board = [[0 for i in range(3)] for j in range(3)]
    else:
      self.board = board

  def getRow(self, i): return self.board[i]

  def getCol(self, j): return list(map(lambda l : l[j], self.board))

  def getLeftDiag(self): return [self.board[0][0], self.board[1][1], self.board[2][2]]

  def getRightDiag(self): return [self.board[2][0], self.board[1][1], self.board[0][2]]

  def squareIsEmpty(self, row, col): return self.board[row][col] == 0

  def setSquare(self, row, col, value): self.board[row][col] = value

  def hasEmptySquares(self):
    for i in range(3):
      for j in range(3):
        if self.board[i][j] == 0: return True
    return False

  def __repr__(self):
    def printSquare(row, col):
      val = self.board[row][col]
      if val == 0:
        return " "
      return val

    return(
f""" 
      -------------
      | {printSquare(0, 0)} | {printSquare(0, 1)} | {printSquare(0, 2)} |
      -------------
      | {printSquare(1, 0)} | {printSquare(1, 1)} | {printSquare(1, 2)} |
      -------------
      | {printSquare(2, 0)} | {printSquare(2, 1)} | {printSquare(2, 2)} |
      -------------
""")

TicTacToe().play()