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
    choice = make_choice(results, player)
    assert choice in results        # choice is a valid move
    assert choice != None           # choice is not None
    assert len(choice) == 2         # choice is a tuple of 2 elements due to move list being less than 3

    ## Test 2: Test that the function returns a valid move with move list = 2
    # If len of move list is 2, then prioritize returning a valid move that is in the move list
    # If no choice is in the move list, randomly return a valid move with one element
    # Case: Both moves in move list are valid
    player.move_list=[3, 4]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == (3, 4)
    # Case: One move in move list is valid
    player.move_list=[3, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == 3
    # Case: No moves in move list are valid
    player.move_list=[8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert  type(choice) is int

    ## Test 3: Test that the function returns a valid move with a full move list with both being inside the list
    # If len of move list is 3, first checks if any choices have both elements in the move list
    # Returns the first choice that has both elements in the move list
    player.move_list=[3, 4, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == (3, 4)

    ## Test 4: Test that the function returns a valid move with a full move list with one being inside the list
    # Looks at each choice starting with first element, then second element
    # First test checks if the first element is in the move list
    player.move_list=[3, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == 3
    # Second test checks if the second element is in the move list
    player.move_list=[4, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == 4

    ## Test 5: Test that the function returns a valid move with a full move list with neither being inside the list
    # If none of the choices hav an element in the move list, return none
    player.move_list=[2, 8, 9]
    results=[(6, 7), (3, 4), (5, 6)]
    choice = make_choice(results, player)
    assert choice == None

if __name__ == "__main__":
    test_make_choice()
    print("All tests passed!")