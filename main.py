# PROJECT NAME: TICTACTOE
# AUTHOR: CESAR MORALES
#
#

import Board

gameOver = False


# MAIN

gameBoard = Board.Board()

playerOne = input("Enter player one's symbol: ")
while len(playerOne) > 1:
    print("Invalid symbol, please try again.\n")
    playerOne = input("Enter player one's symbol: ")

# will keep track of which player is next
currentTurn = playerOne

playerTwo = input("Enter player two's symbol: ")

while len(playerTwo) > 1 or playerOne == playerTwo:
    print("Invalid symbol, please try again.\n")
    playerTwo = input("Enter player two's symbol: ")

help = input("Would you like to know the inputs to play? (Y/N): ")

if help == "Y":
    gameBoard.printInputs()

while not gameOver:

    print("")
    gameBoard.printBoard()
    print("")

    move = input("Enter your choice: ")

    gameBoard.move(move, currentTurn)

    # checks if the input is a valid move
    while not gameBoard.validMove:
        move = input("Enter your choice: ")
        gameBoard.move(move, currentTurn)


    # switch currentTurn once the other player enters a valid move
    if currentTurn == playerOne:
        currentTurn = playerTwo
    else:
        currentTurn = playerOne

    if gameOver:
        print("\nNew game?(Y/N): ", end= "")
        answer = input()

        if answer == "Y":
            gameBoard.resetBoard()
            gameOver = False
        else:
            exit(0)


