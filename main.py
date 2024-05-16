# PROJECT NAME: TICTACTOE
# AUTHOR: CESAR MORALES
#
#

import Board

gameOver = False

# MAIN

gameBoard = Board.Board()

gameBoard.playerOne = input("Enter player one's symbol: ")
while len(gameBoard.playerOne) > 1:
    print("Invalid symbol, please try again.\n")
    gameBoard.playerOne = input("Enter player one's symbol: ")

# will keep track of which player is next
currentTurn = gameBoard.playerOne

gameBoard.playerTwo = input("Enter player two's symbol: ")

while len(gameBoard.playerTwo) > 1 or gameBoard.playerOne == gameBoard.playerTwo:
    print("Invalid symbol, please try again.\n")
    gameBoard.playerTwo = input("Enter player two's symbol: ")

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
    if currentTurn == gameBoard.playerOne:
        currentTurn = gameBoard.playerTwo
    else:
        currentTurn = gameBoard.playerOne

    gameBoard.winner()
    if gameBoard.won != " ":
        gameOver = True

    if gameOver:

        if gameBoard.won == gameBoard.playerOne:
            print("Player " + gameBoard.playerOne + " Won!")
        else:
            print("Player " + gameBoard.playerTwo + " Won!")

        print("\nNew game?(Y/N): ", end="")
        answer = input()

        if answer == "Y":
            gameBoard.resetBoard()
            gameOver = False
        else:
            exit(0)
