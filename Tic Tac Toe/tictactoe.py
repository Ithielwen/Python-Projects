"""
Tic Tac Toe
Author: Emma Hungrige
"""

symbol = ["", "x", "o"]

def printRow(row):

    #Output left border
    rowStr = "| "

    #Each square in the row
    for square in row:
        rowStr = rowStr + symbol[square] + " | "
    print(rowStr)

def printboard(board):
    
    #Print the top border
    print("+----------------+")

    #Each row on the board
    for row in board:
        printRow(row)
        print("+----------------+")

def markBoard(board, row, col, player):

    #Check if wanted square is blank
    if board[row][col] == 0:
        board[row][col] = player
        return True
    
    else:
        return False

def getPlayerMove():

    #prompt the user separately for the row/col numbers
    row = int(input("Enter the row for your move (0-2): "))
    col = int(input("Enter the column for your move (0-2): "))
    return (row, col)

def hasBlanks(board):

    #For each row on the board
    for row in board:

        #For each square in the row
        for square in row:
            if square == 0:
                return True
    return False

def won(board):
    if horizontalWin(board) != 0:
        return horizontalWin(board)
    
    elif verticalWin(board) != 0:
        return verticalWin(board)

    elif diagonalWin(board) != 0:
        return diagonalWin(board)
    
    else:
        return 0
    
def horizontalWin(board):

    #For each row on the board
    for row in board:
        value = row[0]
        win = True
        for square in row:
            if square != value or square == 0:
                win = False
                break
        
        if win:
            return value
    return 0

def verticalWin(board):

    #For each column on the board
    for col in range(len(board[0])):

        value = board[0][col]
        win = True
        for square in range(len(board)):
            if board[square][col] != value or board[square][col] == 0:
                win = False
                break
        
        if win:
            return value
    return 0

def diagonalWin(board):

    #For each column on the board
    value = board[0][0]
    for col in range(len(board[0])):
        row = col
        if board[row][col] != value or board[row][col] == 0:
            return 0

    value = board[2][0]
    for col in range(len(board[0])):
        row = 2 - col
        win = True
        if board[row][col] != value or board[row][col] == 0:
            return 0
    return value

def main():
    board = [[0,0,0], [0,0,0], [0,0,0]]
    player = 1

    while hasBlanks(board) and won(board) == 0:
        printboard(board)
        row,col = getPlayerMove()
        if markBoard(board, row, col, player):
            player = player % 2 + 1
        
        else:
            print("Square taken. Select a different square.")
    printboard(board)
    if won(board) != 0:
        print(symbol[won(board)] + " wins!")

main()
