class Board:
    # constructor
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.validMove = True
    # resets the board
    def resetBoard(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
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
        if move == "TL":
            self.board[0][0] = symbol
            self.validMove = True
        elif move == "TM":
            self.board[0][1] = symbol
            self.validMove = True
        elif move == "TR":
            self.board[0][2] = symbol
            self.validMove = True
        elif move == "LM":
            self.board[1][0] = symbol
            self.validMove = True
        elif move == "M":
            self.board[1][1] = symbol
            self.validMove = True
        elif move == "RM":
            self.board[1][2] = symbol
            self.validMove = True
        elif move == "BL":
            self.board[2][0] = symbol
            self.validMove = True
        elif move == "BM":
            self.board[2][1] = symbol
            self.validMove = True
        elif move == "BR":
            self.board[2][2] = symbol
            self.validMove = True
        else:
            print("Invalid input")
            self.validMove = False
