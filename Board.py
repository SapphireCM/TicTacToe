class Board:
    # constructor
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.validMove = True
        self.playerOne = " "
        self.playerTwo = " "
        self.won = " "
    # resets the board
    def resetBoard(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.won = " "
        self.validMove = True
    # prints the board
    def printBoard(self):

        print(" " + str(self.board[0][0]), end =" | ")
        print(self.board[0][1], end=" | ")
        print(self.board[0][2])

        print("___|___|___")

        print(" " + str(self.board[1][0]), end=" | ")
        print(self.board[1][1], end=" | ")
        print(self.board[1][2])

        print("___|___|___")

        print(" " + str(self.board[2][0]), end=" | ")
        print(self.board[2][1], end=" | ")
        print(self.board[2][2])

    def printInputs(self):
        print("\nInputs are the following: ")
        print("TL - Top Left", "TM - Top Middle", "TR - Top Right", sep ="\n")
        print("ML - Middle Left", "M - Middle", "MR - Middle Right", sep="\n")
        print("BL - Bottom Left", "BM - Bottom Middle", "BR - Bottom Right", sep="\n")

    def move(self, move, symbol):
        if move == "TL" and self.board[0][0] == ' ':
            self.board[0][0] = symbol
            self.validMove = True
        elif move == "TM" and self.board[0][1] == ' ':
            self.board[0][1] = symbol
            self.validMove = True
        elif move == "TR" and self.board[0][2] == ' ':
            self.board[0][2] = symbol
            self.validMove = True
        elif move == "LM" and self.board[1][0] == ' ':
            self.board[1][0] = symbol
            self.validMove = True
        elif move == "M" and self.board[1][1] == ' ':
            self.board[1][1] = symbol
            self.validMove = True
        elif move == "RM" and self.board[1][2] == ' ':
            self.board[1][2] = symbol
            self.validMove = True
        elif move == "BL" and self.board[2][0] == ' ':
            self.board[2][0] = symbol
            self.validMove = True
        elif move == "BM" and self.board[2][1] == ' ':
            self.board[2][1] = symbol
            self.validMove = True
        elif move == "BR" and self.board[2][2] == ' ':
            self.board[2][2] = symbol
            self.validMove = True
        else:
            print("Invalid input")
            self.validMove = False

    def winner(self):
        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            self.won = self.board[0][0]
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == self.playerOne:
            self.won = self.board[1][0]
        elif self.board[2][0] == self.board[2][1] == self.board[2][2]:
            self.won = self.board[2][0]
        elif self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.won = self.board[0][0]
        elif self.board[0][1] == self.board[1][1] == self.board[2][1]:
            self.won = self.board[0][1]
        elif self.board[0][2] == self.board[1][2] == self.board[2][2]:
            self.won = self.board[0][2]
        elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.won = self.board[0][0]
        elif self.board[2][0] == self.board[1][1] == self.board[0][2]:
            return self.board[2][0]
        else:
            self.won = " "
