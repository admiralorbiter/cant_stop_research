from board import Board

def initialization():
    print("Testing initialization...")
    b = Board()
    assert b.board[0]==[2, 0, 0]
    assert b.board[1]==[3, 0, 0]
    assert b.board[2]==[4, 0, 0]
    assert b.board[3]==[5, 0, 0]
    assert b.board[4]==[6, 0, 0]
    assert b.board[5]==[7, 0, 0]
    assert b.board[6]==[8, 0, 0]
    assert b.board[7]==[9, 0, 0]
    assert b.board[8]==[10, 0, 0]
    assert b.board[9]==[11, 0, 0]
    assert b.board[10]==[12, 0, 0]

def test_roll_dice():
    board = Board()
    roll=board.roll_dice(4, 6)
    assert len(roll)==4
    assert roll[0]>=1


def test_dice_combinations():
    board = Board()
    dice = [1, 2, 3, 4]
    combos = board.dice_combinations(dice)
    assert combos[0] == (3, 7)
    assert combos[1] == (4, 6)
    assert combos[2] == (5, 5)
    #TODO: Test if dice list is larger or smaller

def test_evaluate_move():
    board = Board()
    assert board.evaluate_move(2) == True
    assert board.evaluate_move(3) == True
    assert board.evaluate_move(4) == True
    assert board.evaluate_move(5) == True
    assert board.evaluate_move(6) == True
    assert board.evaluate_move(7) == True
    assert board.evaluate_move(8) == True
    assert board.evaluate_move(9) == True
    assert board.evaluate_move(10) == True
    assert board.evaluate_move(11) == True
    assert board.evaluate_move(12) == True
    #TODO: Change board state to test if move is invalid
    # Will need to test if move is invalid for each column and player combination
if __name__ == "__main__":
    initialization()
    test_roll_dice()
    test_dice_combinations()
    test_evaluate_move()
    print("All tests passed!")