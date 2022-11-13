from player import Player
from ai import AI

def initialization():
    player = Player(AI("random", 0))
    assert player.cols == 0
    assert player.rule_constant == 0
    assert player.move_list == []
    assert player.ai.flag == "random"

def test_add_move():
    # Testing default case, no change to rule constant
    player = Player(AI("constant", 8))
    player.move_list = [2, 3]
    player.add_move(4)
    assert player.rule_constant == 0
    #TODO: Test rule constant 2
    #TODO: Test rule constant 4
    #TODO: Test rule constant -2
    #TODO: Test adding a move that is already in the list

def test_move_calc():
    player = Player(AI("constant", 8))
    player.move_calc(2)
    player.add_move(2)
    assert player.rule_constant == 12
    player.move_calc(2)
    assert player.rule_constant == 18
    #TODO: Test the rest of the columns
    #TODO: Test numbers out of range

if __name__ == "__main__":
    initialization()
    test_add_move()
    test_move_calc()
    print("All tests passed!")