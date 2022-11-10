from ai import AI
from player import Player

def initialization():
    ai = AI("random", 0)
    assert ai.flag == "random"
    assert ai.num == 0
    ai = AI("rule", 1)
    assert ai.flag == "rule"
    assert ai.num == 1
    ai = AI("constant", 2)
    assert ai.flag == "constant"
    assert ai.num == 2

def test_random():
    ai = AI("random", 0)
    assert ai.stop(None, 0) == True

def test_rule():
    ai = AI("rule", 10)
    player = Player(ai)
    player.move_num = 0
    assert ai.stop(player, 0) == False
    player.move_num = 9
    assert ai.stop(player, 0) == False
    player.move_num = 10
    assert ai.stop(player, 0) == True
    player.move_num = 11
    assert ai.stop(player, 0) == True

def test_constant():
    ai = AI("constant", 10)
    assert ai.stop(None, 0) == False
    assert ai.stop(None, 9) == False
    assert ai.stop(None, 10) == True
    assert ai.stop(None, 11) == True

if __name__ == "__main__":
    initialization()
    test_random()
    test_rule()
    print("All tests passed!")