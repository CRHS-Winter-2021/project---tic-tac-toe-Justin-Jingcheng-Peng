##Tic Tac Toe
#Name:
#Date:

#1. (Var) Setup the empty board as a list
theBoard = [" "," "," "," "," "," "," "," "," "," ",]

#2. (fun) Print the board.
#in: a 10 item list (either x, o or ' ')
#do: print a graphic for the board
#out: none

def printBoard(board):
  print(theBoard[7] + '|' + theBoard[8] + '|' + theBoard[9])
  print("-----")
  print(theBoard[4] + '|' + theBoard[5] + '|' + theBoard[6])
  print("-----")
  print(theBoard[1] + '|' + theBoard[2] + '|' + theBoard[3])
  

#3a. (fun) Determine if player is X or O
player1 = 'X'
player2 = 'O'

#in: None
#do: get user choice, assign X/O to player1 and 2
#out: None

def chooseLetter():
  global player1
  global player2
  a = input('player1, type X/O ')
  while True:
    if a == 'O' or a == 'X':
      break
    a = input('player1, type X/O ')
    if a == 'O' or a == 'X':
      break
    
  if a == 'X':
    player1 = 'X'
    player2 = 'O'
  else:
    player1 = 'O'
    player2 = 'X'
  print('player1: ' + player1, "player2 " + player2)


#3b. (fun) Choose starting player 1 or 2
def chooseStart():

  a = input('Who to start? ')
  while True:
    if a == '1' or a == '2':
      break
    a = input('Please return proper string. Who to start? ')
    if a == '1' or a == '2':
      break
  
  if a == '1':
    return 1
  else:
    return 2

#4. (fun) Get player move
#in: board as list, player as X or O
#do: get user choice (1-9),
#    check if the space is empty,
#    update the board with the X or O at the user location
#out: none

def playerMove(board, player):
  choice = int(input("Which position? "))
  while board[choice] != ' ':
    print('That is occupied ')
    choice = int(input("Which position? "))
  if board[choice] == ' ':
      board[choice] = player  
  printBoard(theBoard)


#5. (fun) Check Winner
#in: board as list, player as X or O
#do: check all possible win scenarios
#out: True for win, False otherwise
  
def checkWin(board, player):
  
  if theBoard[1] == theBoard[2] == theBoard[3] == 'X' or theBoard[4] == theBoard[5] == theBoard[6] == 'X' or theBoard[7] == theBoard[8] == theBoard[9] == "X" or theBoard[1] == theBoard[4] == theBoard[7] == "X"or theBoard[2] == theBoard[5] == theBoard[8] == "X" or theBoard[3] == theBoard[6] == theBoard[9] == "X" or theBoard[3] == theBoard[5] == theBoard[7] == "X" or theBoard[1] == theBoard[5] == theBoard[9] == "X":
    if player == 'X':
      return True
    else:
      return False
  elif theBoard[1] == theBoard[2] == theBoard[3] == 'O' or theBoard[4] == theBoard[5] == theBoard[6] == 'O' or theBoard[7] == theBoard[8] == theBoard[9] == "O" or theBoard[1] == theBoard[4] == theBoard[7] == "O"or theBoard[2] == theBoard[5] == theBoard[8] == "O" or theBoard[3] == theBoard[6] == theBoard[9] == "O" or theBoard[3] == theBoard[5] == theBoard[7] == "O" or theBoard[1] == theBoard[5] == theBoard[9] == "O":
    if player == 'O':
      return True
    else:
      return False
         
   
  


#6. (fun) Check if board is full
#Because there are 10 list items for 9 spots,
#the first item theBoard[0] will always be ' '
#in: board as list
#do: count number of empty spaces, if there is no more spaces
#out: return True if board is full, False otherwise

def checkFull(board):
  if board.count(' ') == 1:
    return True
  else:
    return False

#7. Main function

def main():
    #print Welcome
    #print instructions

    #game play
    #get player letter choice
    
    #while board is not full
    ###first player move
        #player chooses move
        #print board
        #check win
        #check board full

    ###second player move
        #player chooses move
        #print baord
        #check win
  currentplayer = ''  
  chooseLetter()
  if chooseStart() == 2:
    currentplayer = 2
    print('Player ' + str(currentplayer) + " 's turn ")
    playerMove(theBoard, player2)
    
  
  while True:
    currentplayer = 1
    print('Player ' + str(currentplayer) + " 's turn")
    playerMove(theBoard, player1)
    if checkWin(theBoard, player1) == True:
      print('player1 wins, game over')
      return 0
    elif checkFull(theBoard) == True:
      print('Full, Game Over')
      return 0
    
    currentplayer = 2
    print('Player ' + str(currentplayer) + " 's turn")
    playerMove(theBoard, player2)
    if checkWin(theBoard, player2) == True:
      print('player2 wins, game over')
      return 0
    elif checkFull(theBoard) == True:
      print('Full, Game Over')
      return 0

main()
    