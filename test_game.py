from game import *
from board import Board
from player import Player
from ai import AI

def test_make_choice():
    ## Test 1: Test that the function returns a valid move with move list < 3
    # If len of move list is strictly less than 3, then randomly return a valid move
    b = Board()
    player = Player(AI("constant", 10))
    dice=b.roll_dice(4, 6)
    results=b.dice_combinations(dice)
    choice = make_choice(results, player, b.board)
    assert choice in results        # choice is a valid move
    assert choice != None           # choice is not None
    assert len(choice) == 2         # choice is a tuple of 2 elements due to move list being less than 3

    ## Test 2: Test that the function returns a valid move with move list = 2
    # If len of move list is 2, then prioritize returning a valid move that is in the move list
    # If no choice is in the move list, randomly return a valid move with one element
    # Case: Both moves in move list are valid
    player.move_list=[3, 4]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == (3, 4)
    # Case: One move in move list is valid
    player.move_list=[3, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == 3
    # Case: No moves in move list are valid
    player.move_list=[8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert  type(choice) is int

    ## Test 3: Test that the function returns a valid move with a full move list with both being inside the list
    # If len of move list is 3, first checks if any choices have both elements in the move list
    # Returns the first choice that has both elements in the move list
    player.move_list=[3, 4, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == (3, 4)

    ## Test 4: Test that the function returns a valid move with a full move list with one being inside the list
    # Looks at each choice starting with first element, then second element
    # First test checks if the first element is in the move list
    player.move_list=[3, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == 3
    # Second test checks if the second element is in the move list
    player.move_list=[4, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == 4

    ## Test 5: Test that the function returns a valid move with a full move list with neither being inside the list
    # If none of the choices hav an element in the move list, return none
    player.move_list=[2, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player, b.board)
    assert choice == None
    
def test_taken_columns():
    board = [[2, 2, 3], [3, 4, 0], [4, 5, 0], [5, 6, 5], [6, 0, 7], [7, 0, 8], [8, 6, 7], [9, 6, 5], [10, 1, 5], [11, 3, 4], [12, 2, 3]]
    taken_columns=check_taken_columns(board)
    assert taken_columns == [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


#TODO: Test temp columns
def test_make_move():
    b = Board()
    player = Player(AI("constant", 10))
    player_num = 1

    ## Test 1: Test 2 element choice
    choice = (3, 4)
    make_move(b, choice, player_num, player)
    assert b.board[choice[0]-2][player_num] == 1
    assert b.board[choice[1]-2][player_num] == 1
    assert player.move_list == [3, 4]
    assert player.temp_cols == 0
    ## Test 2: Test single element choice
    choice = 5
    make_move(b, choice, player_num, player)
    assert b.board[choice-2][player_num] == 1
    assert player.move_list == [3, 4, 5]
    assert player.temp_cols == 0
    ## Test 3: Test temp column evaluation
    choice = (3, 3)
    make_move(b, choice, player_num, player)
    choice = 3
    make_move(b, choice, player_num, player)
    assert b.board[choice-2][player_num] == 4
    assert player.move_list == [3, 4, 5]
    assert player.temp_cols == 1

def test_stop_ai():
    player = Player(AI("constant", 10))
    next = player.ai.stop(player, 10)

if __name__ == "__main__":
    print("Testing taken columns")
    test_taken_columns()
    print("Testing make choice")
    test_make_choice()
    print("Testing make move")
    test_make_move()
    print("Testing stop ai")
    test_stop_ai()
    print("All tests passed!")