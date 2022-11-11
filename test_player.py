from player import Player
from ai import AI

def initialization():
    player = Player(AI("random", 0))
    assert player.cols == 0
    assert player.rule_constant == 0
    assert player.move_list == []
    assert player.ai.flag == "random"

if __name__ == "__main__":
    initialization()
    print("All tests passed!")