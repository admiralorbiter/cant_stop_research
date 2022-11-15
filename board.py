import random

class Board:
    # Board Object has a list called board that keeps track of the current board state
    # Each entry in the list is a tuple of the form 
    # (column number, number of tokens in player 1 column, number of tokens in player 2 column)
    def __init__(self):
        self.board = []
        self.taken_columns=[] #TODO: Test this with unit tests
        for i in range(1, 12):
            self.board.append([i+1, 0, 0])

    ### Roll Dice ###
    # Helper function that takes number of dice and sides to roll and returns the results in a list
    # EX: roll_dice(4,6) will roll 4 6-sided dice and return the results in a list
    def roll_dice(self,num_dice, num_sides):
        dice = []
        for i in range(num_dice):
            dice.append(random.randint(1, num_sides))
        return dice

    ### Calculate Dice Combinations ###
    # Given the four dice, this function calculates all possible combinations of dice for a given move
    # dice - list of four dice
    def dice_combinations(self, dice):
        results=[]
        results.append((dice[0]+dice[1], dice[2]+dice[3]))
        results.append((dice[0]+dice[2], dice[1]+dice[3]))
        results.append((dice[0]+dice[3], dice[1]+dice[2]))
        return results

    ### Print Board ###
    # Prints the current board state in an easy to read format
    # O - player 1 token
    # X - player 2 token
    def print_board(self):
        print("Board:")
        for i in range(0, 10):
            if(self.board[i][1]>self.board[i][2]):
                for j in range(0, self.board[i][1]):
                    print("O", end="")
            else:
                for j in range(0, self.board[i][2]):
                    print("X", end="")
            print("")

    ### Evaluates if the move is valid ###
    # n - column number
    # if the column is full, returns false, else returns true
    # TODO: Write unit tests for taken_columns
    def evaluate_move(self, n):
        if n in self.taken_columns:
            return False
        if n==7:
            if self.board[n-2][1]>=8 or self.board[n-1][2]>=8:
                self.taken_columns.append(n)
                return False
            else:
                return True
        elif n==8 or n==6:
            if self.board[n-2][1]>=7 or self.board[n-1][2]>=7:
                self.taken_columns.append(n)
                return False
            else:
                return True
        elif n==9 or n==5:
            if self.board[n-2][1]>=6 or self.board[n-1][2]>=6:
                self.taken_columns.append(n)
                return False
            else:
                return True
        elif n==10 or n==4:
            if self.board[n-2][1]>=5 or self.board[n-1][2]>=5:
                self.taken_columns.append(n)
                return False
            else:
                return True
        elif n==11 or n==3:
            if self.board[n-2][1]>=4 or self.board[n-1][2]>=4:
                self.taken_columns.append(n)
                return False
            else:
                return True
        elif n==12 or n==2:
            if self.board[n-2][1]>=3 or self.board[n-1][2]>=3:
                self.taken_columns.append(n)
                return False
            else:
                return True
