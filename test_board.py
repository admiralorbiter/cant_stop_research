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
if __name__ == "__main__":
    initialization()
    print("All tests passed!")