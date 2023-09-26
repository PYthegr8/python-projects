import random


board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"]

firstPlayer = "X"
winner = None
gameRunning = True





# print game board
def printBoard(board):
    print(board[0]+  " | "+ board[1] + " | "+ board [2])
    print("---------")
    print(board[3]+  " | "+ board[4]+ " | "+ board [5])
    print("---------")
    print(board[6]+  " | "+ board[7]+ " | "+ board [8])
   
 

# accept player input

def playerInput(board):
    inp= int(input("Select spot 1-9:"))
    if inp>=1 and inp<= 9 and board[inp-1] == "-":
        board[inp-1]= firstPlayer
    else:
        print ("spot taken")
    
# Check for Win or Tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner=board[0]
        return True
    elif board[3]== board[4]== board[5] and board[3]!= "-":
        winner= board[3]
        return True
    elif board[6]== board[7]== board[8] and board[6]!= "-":
        winner= board[6]
        return True
    

def CheckVertical(board):
    global winner
    if  board[0] == board[3] == board[6] and board[0] != "-":
        winner=board[0]
        return True
    elif board[1]== board[4]== board[7] and board[1]!= "-":
        winner= board[1]
        return True
    elif board[2]== board[5]== board[8] and board[2]!= "-":
        winner= board[3]
        return True
    
def CheckDiag(board):
    global winner
    if  board[0] == board[4] == board[8] and board[0] != "-":
        winner=board[0]
        return True
    elif board[2]== board[4]== board[6] and board[4]!= "-":
        winner= board[2]
        return True


def CheckTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("This game is a tie")
        gameRunning = False
    
def CheckWin():
    global gameRunning
    if CheckDiag(board) or CheckVertical(board) or checkHorizontal(board):
        print(f"The winner is {winner}!")
        gameRunning= False

# Switch Player

def switchPlayer():
    global firstPlayer 
    if firstPlayer == "X":
     firstPlayer = "0"
    else:
        firstPlayer="X"

  
#computer
def computer(board):
    while firstPlayer == "0":
        position = random.randint(0, 8)
        if board[position]== "-":
            board[position]="0"
            switchPlayer()
    
# Check for win or Tie




while gameRunning:
    printBoard(board)
    playerInput(board)
    CheckWin()
    CheckTie(board)
    switchPlayer()
    computer(board)
    CheckWin
    CheckTie(board)
