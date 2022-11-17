import random

class AI:
    def __init__(self, flag, num):
        self.flag=flag      #flag for strategy   
        self.num=num        #number for strategy
    
    def stop(self, player, turn):
        ### Random Strategy ###
        # Will roll a n sided dice, where n is the specified number. If roll a 0, stop.
        if self.flag=="random":
            if random.randint(0, self.num)==0:
                return True
            else:
                return False
        ### Rule of '28' Strategy ###
        # Will stop if the player has reached n points, where n is specified number
        # Points calculated based on previous research
        if self.flag=="rule":
            if player.rule_constant>=self.num:
                return True
            else:
                return False
        ### Constant Strategy ###
        # Will stop if the turn number is greater than n, where n is specified number
        if self.flag=="constant":
            if turn>=self.num:
                return True
            else:
                return False
        else:
            return True