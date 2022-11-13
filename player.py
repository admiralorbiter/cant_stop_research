from ai import AI

class Player:
    def __init__(self, ai):
        self.cols = 0                   #number of columns taken
        self.rule_constant = 0          # keeps track of the 'rule of 28' based on research
        self.move_list = []             #current list of moves
        self.ai = ai                    #AI object

    ### Add a move to the player's move list ###
    # Checks if the move is in the move list, if not, adds it
    # If the move list is full (3 moves), then it calculates the rule of '28' constant that is based on previous research
    # TODO: move the rule of '28' calculation to a separate function
    # move - column number
    def add_move(self, move):
        if move not in self.move_list:
            self.move_list.append(move)
            if len(self.move_list)==3:
                #if all moves are odd, add 2 points, even subtract 2
                if self.move_list[0]%2==1 and self.move_list[1]%2==1 and self.move_list[2]%2==1:
                    self.rule_constant+=2
                elif self.move_list[0]%2==0 and self.move_list[1]%2==0 and self.move_list[2]%2==0:
                    self.rule_constant-=2
                #if sum of moves is less than 8 and greater than 6, add 4 points
                elif self.move_list[0]+self.move_list[1]+self.move_list[2]<8 and self.move_list[0]+self.move_list[1]+self.move_list[2]>6:
                    self.rule_constant+=4
    
    ### Calculate the rule of '28' constant depending on the column###
    # Calculates the constant based on the column number
    # move - column number
    # TODO: Move this into add_move function
    def move_calc(self, move):
        num=0
        if move==2 or move==12:
            num=12
        elif move==3 or move==11:
            num=10
        elif move==4 or move==10:
            num=8
        elif move==5 or move==9:
            num=6
        elif move==6 or move==8:
            num=4
        elif move==7:
            num=2
        if move in self.move_list:
            self.rule_constant+=num/2;
        else:
            self.rule_constant+=num;
