from game import *
from board import Board
from player import Player
from ai import AI

if __name__ == "__main__":
    b = Board()
    player1 = Player()
    dice = b.roll_dice(4, 6)                   # roll the dice
    results = b.dice_combinations(dice)        # calculate all possible combinations
    print(results)
    player1.move_list=[2, 4, 6]
    print(player1.move_list)
    choice=make_choice(results, player1)
    if choice!=[]:
        make_move(b, choice)