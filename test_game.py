from game import *
from board import Board
from player import Player
from ai import AI

if __name__ == "__main__":
    b = Board()
    b.test_board()
    player1 = Player()
    # dice = b.roll_dice(4, 6)                   # roll the dice
    # results = b.dice_combinations(dice)        # calculate all possible combinations
    # print(results)
    # player1.move_list=[7, 8, 9]
    # print(player1.move_list)
    # choice=make_choice(results, player1)
    # if choice!=[]:
    #     make_move(b, choice, 1, player1)
    #     print(player1.cols)
    complete_turn(b, player1, 1)
    assert player1.cols>=1
    print("All tests passed!")