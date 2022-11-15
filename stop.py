import csv
import random
import math
import copy

# random.seed(10)
test=False
years=10

class AI:
    def __init__(self, flag, num):
        self.flag=flag
        self.num=num
    def stop(self, player, turn):
        if self.flag=="random":
            if random.randint(0, self.num)==0:
                return True
            else:
                return False
        if self.flag=="rule":
            if player.move_num>=self.num:
                return True
            else:
                return False
        if self.flag=="constant":
            if turn>=self.num:
                return True
            else:
                return False
        else:
            return True

class Player:
    def __init__(self, ai):
        self.points = 0
        self.move_num = 0
        self.move_list = []
        self.ai = ai
    def add_move(self, move):
        if move not in self.move_list:
            self.move_list.append(move)
            if len(self.move_list)==3:
                #if all moves are odd, add 2 points, even subtract 2
                if self.move_list[0]%2==1 and self.move_list[1]%2==1 and self.move_list[2]%2==1:
                    self.points+=2
                elif self.move_list[0]%2==0 and self.move_list[1]%2==0 and self.move_list[2]%2==0:
                    self.points-=2
                #if sum of moves is less than 8 and greater than 6, add 4 points
                elif self.move_list[0]+self.move_list[1]+self.move_list[2]<8 and self.move_list[0]+self.move_list[1]+self.move_list[2]>6:
                    self.points+=4
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
            self.move_num+=num/2;
        else:
            self.move_num+=num;

class Board:
    def __init__(self):
        self.board = []
        for i in range(1, 12):
            self.board.append([i+1, 0, 0])

    def roll_dice(self,num_dice, num_sides):
        dice = []
        for i in range(num_dice):
            dice.append(random.randint(1, num_sides))
        return dice

    def calc_single_odds(self, dice):
        results=[]
        results.append((dice[0]+dice[1], dice[2]+dice[3]))
        results.append((dice[0]+dice[2], dice[1]+dice[3]))
        results.append((dice[0]+dice[3], dice[1]+dice[2]))
        return results

    def print_board(self):
        print("Board:")
        for i in range(0, 10):
            if(self.board[i][1]>self.board[i][2]):
                for j in range(0, self.board[i][1]):
                    print("O", end="")
            else:
                for j in range(0, self.board[i][2]):
                    print("X", end="")
            print("")

    def evaluate_move(self, p, n):
        if n==7:
            if self.board[n-2][p]>=8:
                return False
            else:
                return True
        elif n==8 or n==6:
            if self.board[n-2][p]>=7:
                return False
            else:
                return True
        elif n==9 or n==5:
            if self.board[n-2][p]>=6:
                return False
            else:
                return True
        elif n==10 or n==4:
            if self.board[n-2][p]>=5:
                return False
            else:
                return True
        elif n==11 or n==3:
            if self.board[n-2][p]>=4:
                return False
            else:
                return True
        elif n==12 or n==2:
            if self.board[n-2][p]>=3:
                return False
            else:
                return True

def make_move(b, player_num, choice, player, test):
    if choice in taken_columns:
        return 0, player, False
    if choice not in player.move_list and len(player.move_list)>=3:
        return 0, player, False
    eval = b.evaluate_move(player_num, choice)
    if eval==True:
        b.board[choice-2][player_num]+=1
        player.add_move(choice)
        if test:print("New Move List: ",player.move_list)
        eval = b.evaluate_move(player_num, choice)
    if eval==False:
        if test:print("Player took column ", choice)
        taken_columns.append(choice)
        return 1, player, True
    else:
        return 0, player, True

def make_choice(results, player):
    if len(player.move_list)<3:
        return results[random.randint(0,2)]
    else:
        choices=[]
        for i in range(0, len(results)):
            if results[i][0] in player.move_list or results[i][1] in player.move_list:
                choices.append(results[i])
        if test:("Valid choices: ", choices)
        if len(choices)!=0:
            return choices[random.randint(0, len(choices)-1)]

def play_game(player, player1, player2, test):
    global taken_columns
    taken_columns=[]
    b = Board()
    if test:print(b.board)
    if test:print("Player ", player, " turn")
    turns=0
    oldboard=copy.deepcopy(b)
    old_points=0
    while player1.points<3 and player2.points<3:
        dice=b.roll_dice(4, 6)
        # print(dice)
        results=b.calc_single_odds(dice)
        #randomly pick a result
        # choice=results[random.randint(0,2)]
        # print("Results: ", results)
        if player==1:
            choice = make_choice(results, player1)
        else:
            choice = make_choice(results, player2)
        if test:print("Choice: ",choice)
        next=False
        # if random.randint(0, 3)==0:
        #     next=True
        if player==1:
            turns+=1
            next=True
            if test:print("Player 1 moves", player1.move_list)
            if test:print("Player 1 old points", old_points)
            if choice!=None:
                points, temp_player, success= make_move(b, player, choice[0], player2, test)
                player1.points+=points
                if test:print("Player 1 points: ", player1.points)
                if success:
                    player1.move_list=temp_player.move_list
                    player1.move_calc(choice[0])
                points, temp_player, success= make_move(b, player, choice[1], player2, test)
                player1.points+=points
                if test:print("Player 1 points: ", player1.points)
                if success: 
                    player1.move_calc(choice[1])
                    player1.move_list=temp_player.move_list
                if test:print("Move Num: ", player1.move_num)
                next=player1.ai.stop(player1, turns)
            if choice==None:
                # if test:print(b, b.board)
                # if test:print(oldboard, oldboard.board)
                player1.points=old_points
                b=copy.deepcopy(oldboard)
                if test:print("BUSTED!!!!")
                # if test:print(b.board)
            if next:
                if test:print(b.board)
                player=2
                player2.move_list=[]
                player2.move_num=0
                oldboard=copy.deepcopy(b)
                if test:print(player1.points, player2.points)
                if test:print()
                if test:print("Player ", player, " turn")
                turns=0
                old_points=player2.points
        else:
            turns+=1
            next=True
            if test:print("Player 2 moves", player2.move_list)
            if test:print("Player 2 old points", old_points)
            if choice!=None:
                points, temp_player, success = make_move(b, player, choice[0], player2, test)
                player2.points+=points
                if test:print("Player 2 points: ", player2.points)
                if success: 
                    player2.move_calc(choice[0])
                    player2.move_list=temp_player.move_list
                points, temp_player, success = make_move(b, player, choice[1], player2, test)
                player2.points+=points
                if test:print("Player 2 points: ", player2.points)
                if success: 
                    player2.move_calc(choice[1])
                    player2.move_list=temp_player.move_list
                if test:print("Move Num: ", player2.move_num)
                next=player2.ai.stop(player2, turns)
            if choice==None:
                b=copy.copy(oldboard)
                player2.points=old_points
                if test:print("BUSTED!!!!")
            if next:
                if test:print(b.board)
                player=1
                player1.move_list=[]
                player1.move_num=0
                oldboard=copy.deepcopy(b)
                if test:print(player1.points, player2.points)
                if test:print()
                if test:print("Player ", player, " turn")
                turns=0
                old_points=player1.points
    if test:
        print()
        print("Columns: ",taken_columns)
        print("Player 1:", player1.points)
        print("Player 2:", player2.points)
        b.print_board()
        print(b.board)

def sim1():
    data=[]
    for x in range(10, 50):
        print(x)
        for y in range(2, 20):
            player1wins=0
            player2wins=0
            for i in range(0, years):
                player1 = Player(AI("rule", x))
                player2 = Player(AI("constant", y))
                # randomly choose who goes first
                player= random.randint(1,2)
                play_game(player, player1, player2, False)
                # if(i%(years/10)==0):
                #     print(player1wins, player2wins)
                if player1.points>player2.points:
                    player1wins+=1
                else:
                    player2wins+=1

            # print("Player 1 wins: ", player1wins, "with ",x)
            # print("Player 2 wins: ", player2wins, "with ",y)
            # print(x, y, math.trunc(player1wins/years*100))
            data.append((x, y, math.trunc(player1wins/years*100)))
            # print(data)
            # print(x, y, "{:2f}".format(player1wins/player2wins*100))
    # print("Player 1 goes first: ", player11st)
    print(data)
    # export to csv
    with open('data.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(data)

def sim2():
    global test
    test=True
    startPlayer= random.randint(1,2)
    player1 = Player(AI("rule", 28))
    player2 = Player(AI("constant", 8))
    play_game(startPlayer, player1, player2, test)

def sim3():
    global test
    test=True
    player1wins = 0
    player2wins = 0
    print("starting...")
    for i in range(0, years):
        if i % 100 == 0: print("Year: ", i)
        player1 = Player(AI("rule", 28))
        player2 = Player(AI("rule", 28))
        # randomly choose who goes first
        player = random.randint(1, 2)
        play_game(player, player1, player2, False)
        # if(i%(years/10)==0):
        #     print(player1wins, player2wins)
        if player1.points > player2.points:
            player1wins += 1
        else:
            player2wins += 1
    print("Player 1 won: ", player1wins)
    print("Player 2 won: ", player2wins)

sim2()
# sim1()
# sim3()
