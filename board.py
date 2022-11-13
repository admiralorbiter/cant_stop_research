import random

class Board:
    # Board Object has a list called board that keeps track of the current board state
    # Each entry in the list is a tuple of the form 
    # (column number, number of tokens in player 1 column, number of tokens in player 2 column)
    def __init__(self):
        self.board = []
        for i in range(1, 12):
            self.board.append([i+1, 0, 0])

    def roll_dice(self,num_dice, num_sides):
        dice = []
        for i in range(num_dice):
            dice.append(random.randint(1, num_sides))
        return dice

    def calc_single_odds(self, dice):
        results=[]
        results.append((dice[0]+dice[1], dice[2]+dice[3]))
        results.append((dice[0]+dice[2], dice[1]+dice[3]))
        results.append((dice[0]+dice[3], dice[1]+dice[2]))
        return results

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

    def evaluate_move(self, p, n):
        if n==7:
            if self.board[n-2][p]>=8:
                return False
            else:
                return True
        elif n==8 or n==6:
            if self.board[n-2][p]>=7:
                return False
            else:
                return True
        elif n==9 or n==5:
            if self.board[n-2][p]>=6:
                return False
            else:
                return True
        elif n==10 or n==4:
            if self.board[n-2][p]>=5:
                return False
            else:
                return True
        elif n==11 or n==3:
            if self.board[n-2][p]>=4:
                return False
            else:
                return True
        elif n==12 or n==2:
            if self.board[n-2][p]>=3:
                return False
            else:
                return True
