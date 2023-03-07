from player import Player
from board import Board
from ai import AI
import copy
import random
import csv

def check_taken_columns(board):
    taken_columns = []
    for i in range(2, len(board)+2):
        if i==7:
            if board[i-2][1]>=8 or board[i-2][2]>=8:
                taken_columns.append(i)
        elif i==8 or i==6:
            if board[i-2][1]>=7 or board[i-2][2]>=7:
                taken_columns.append(i)
        elif i==9 or i==5:
            if board[i-2][1]>=6 or board[i-2][2]>=6:
                taken_columns.append(i)
        elif i==10 or i==4:
            if board[i-2][1]>=5 or board[i-2][2]>=5:
                taken_columns.append(i)
        elif i==11 or i==3:
            if board[i-2][1]>=4 or board[i-2][2]>=4:
                taken_columns.append(i)
        elif i==12 or i==2:
            if board[i-2][1]>=3 or board[i-2][2]>=3:
                taken_columns.append(i)
    return taken_columns

def valid_choices(results, taken_columns):
    for i in range(0, len(results)):
        if results[i][0] not in taken_columns or results[i][1] not in taken_columns:
            return True
    return False

### Make Choice ###
# Implements an algorithm for making a choice based on your options after the dice roll
#TODO: Implement an AI that carefully chooses moves
def make_choice(results, player, board):
    taken_columns = check_taken_columns(board)
    if valid_choices(results, taken_columns)==False: 
        return None
    if len(player.move_list)<2:                     # if the player has less than 3 moves, randomly choose a move
        choice = results[random.randint(0,2)]
        while choice[0] in taken_columns and choice[1] in taken_columns:
            choice = results[random.randint(0,2)]
        return choice
    else:                                           # If the player has 3 moves, then they have to pick a move that is the move list
        choices=[]
        #Create a list of all possible moves
        for i in range(0, len(results)):
            if results[i][0] not in taken_columns or results[i][1] not in taken_columns:
                if results[i][0] in player.move_list or results[i][1] in player.move_list:
                    choices.append(results[i])
        
        #Start by checking if both moves are in the move list, if so choose the first
        #TODO: If there are more than 1, choose the one that will give the most points
        for i in range(0, len(choices)):
            if choices[i][0] in player.move_list and choices[i][1] in player.move_list:
                return choices[i]
        #Checks if the first move is in the move list, if so choose the first, then the second
        #based on order of the choice list
        #TODO: If there are more than 1 possible move, choose the one that will give the most points
        for i in range(0, len(choices)):
            if choices[i][0] in player.move_list:
                return choices[i][0]
            elif choices[i][1] in player.move_list:
                return choices[i][1]
        # The other cases for move_list==2 are caught by previous branches, the only case left is when none of the choices are in the move list
        if len(player.move_list)==2:                #Pick a random move if there are no moves that are in the move list
            return results[random.randint(0,2)][0]  #Returns a random, single element
        if len(choices)==0:return None
        return choices

### Make Move ###
# Implements the functionality for making the move once a choice has been made
def make_move(b, choice, player_num, player):
    if type(choice) is tuple:
        eval = b.evaluate_move(choice[0])           # evaluate if the first move is valid
        if eval == True: 
            b.board[choice[0]-2][player_num]+=1     # add a piece to the board
            player.add_move(choice[0])              # add the move to the player's move list
            eval = b.evaluate_move(choice[0])       # re-evaluate the move to check if they took a column
            if eval == False: player.temp_cols+=1   # if they took a column, add a point
        eval = b.evaluate_move(choice[1])           # Repeat the steps with the second move
        if eval == True: 
            b.board[choice[1]-2][player_num]+=1
            player.add_move(choice[1])
            eval = b.evaluate_move(choice[1])
            if eval == False: player.temp_cols+=1
    else:
        eval = b.evaluate_move(choice)              # If choice is a single move, validate one move
        if eval == True:
            b.board[choice-2][player_num]+=1
            player.add_move(choice)
            eval = b.evaluate_move(choice)
            if eval == False: player.temp_cols+=1

def complete_turn(b, player, player_num, turn_num):
    global oldboard
    if turn_num==0: oldboard = copy.deepcopy(b)     # copy the board so if they go bust, we can revert
    dice = b.roll_dice(4, 6)                        # roll the dice
    results = b.dice_combinations(dice)             # calculate all possible combinations
    choice = make_choice(results, player, b.board)  # choose a combination
    next = False
    if choice!=None:
        make_move(b, choice, player_num, player)
        if type(choice) is tuple:
            for i in range(0, len(choice)):
                player.move_calc(choice[i])
        else:
            player.move_calc(choice)
        next = player.ai.stop(player, turn_num)
    elif choice==None:
        b=copy.deepcopy(oldboard)                   # if they go bust, revert the board
        player.temp_cols=0
        next = True
    if next:
        oldboard=copy.deepcopy(b)                   # copy the board so if they go bust, we can revert
        player.cols+=player.temp_cols               # add the points to the player's total
        player.temp_cols=0                          # reset the temp points
        next = True
    return next, b;
               

def play_game(player1, player2):
    player_num = random.randint(1,2)                # randomly select who goes first, 1=Player 1 and 2=Player 2
    b = Board()                                     # initialize new board
    turn_num = 0
    while player1.cols<3 and player2.cols<3:
        if player_num==1:
            next, b=complete_turn(b, player1, player_num, turn_num)
            turn_num+=1
            if next:
                player_num=2
                player2.move_list=[]
                player2.move_num=0
                player2.temp_cols=0
                turn_num=0                          # reset the turn counter
        else:
            next, b=complete_turn(b, player2, player_num, turn_num)
            turn_num+=1
            if next:
                player_num=1
                player1.move_list=[]
                player1.move_num=0
                player1.temp_cols=0
                turn_num=0                          # reset the turn counter

def sim_play_one_game():
    player1 = Player(AI("random", 8))
    player2 = Player(AI("random", 8))
    play_game(player1, player2)
    print("Player 1: ", player1.cols)
    print("Player 2: ", player2.cols)

def sim_multiple_games(ai1=AI("random", 8), ai2=AI("random", 8)):
    years = 10000
    player1wins=0
    player2wins=0
    for i in range(0, years):
        # if i%(years/10)==0: print(i)
        player1 = Player(ai1)
        player2 = Player(ai2)
        play_game(player1, player2)
        if player1.cols>player2.cols:
            player1wins+=1
        else:
            player2wins+=1
    print("AI Constant", ai1.num, "wins: ", round(player1wins/years*100), "%")
    print("AI Constant", ai2.num, "wins: ", round(player2wins/years*100), "%")
    print("")
    return round(player1wins/years*100)

def test_muliple_ai():
    data=[]
    for x in range(2, 15):
        print(x)
        for y in range(2, 15):
            data.append((x, y, sim_multiple_games(AI("random", x), AI("random", y))))
        print(data)
        # export to csv
        with open('data.csv', 'w', newline='') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
            wr.writerow(data)
# sim_play_one_game()
# sim_multiple_games()
test_muliple_ai()