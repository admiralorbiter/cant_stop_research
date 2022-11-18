from player import Player
from board import Board
from ai import AI
import copy
import random

### Make Choice ###
# Implements an algorithm for making a choice based on your options after the dice roll
#TODO: Implement an AI that carefully chooses moves
def make_choice(results, player):
    if len(player.move_list)<2:                     # if the player has less than 3 moves, randomly choose a move
        return results[random.randint(0,2)]
    else:                                           # If the player has 3 moves, then they have to pick a move that is the move list
        choices=[]
        #Create a list of all possible moves
        for i in range(0, len(results)):
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

def complete_turn(b, player, player_num):
    turn = 0
    oldboard = copy.deepcopy(b.board)               # copy the board so if they go bust, we can revert
    dice = b.roll_dice(4, 6)                        # roll the dice
    results = b.dice_combinations(dice)             # calculate all possible combinations
    choice = make_choice(results, player)           # choose a combination
    turn+=1
    if choice!=None:
        make_move(b, choice, player_num, player)
        if type(choice) is tuple:
            for i in range(0, len(choice)):
                player.move_calc(choice[i])
        else:
            player.move_calc(choice)
        next = player.ai.stop(player, turn)
    elif choice==None:
        b=copy.deepcopy(oldboard)                   # if they go bust, revert the board
        player.temp_cols=0
    
    if next:
        player.cols=player.temp_cols                # if the player chooses to stop, add their points to their total
        oldboard=copy.deepcopy(b)                   # copy the board so if they go bust, we can revert
        turns=0                                     # reset the turn counter
        return next;
               

def play_game(player1, player2):
    player_num = random.randint(1,2)                # randomly select who goes first, 1=Player 1 and 2=Player 2
    b = Board()                                     # initialize new board
    while player1.cols<3 and player2.cols<3:
        print("Player 1: ", player1.cols, "Player 2: ", player2.cols)
        if player_num==1:
            next=complete_turn(b, player1, player_num)
            if next:
                player_num=2
                player2.move_list=[]
                player2.move_num=0
                player2.temp_cols=0
        else:
            next=complete_turn(b, player2, player_num)
            if next:
                player_num=1
                player1.move_list=[]
                player1.move_num=0
                player1.temp_cols=0
    print("Player 1: ", player1.points)
    print("Player 2: ", player2.points)
    print(b.board)


# def sim1():
#     data=[]
#     for x in range(10, 50):
#         print(x)
#         for y in range(2, 20):
#             player1wins=0
#             player2wins=0
#             for i in range(0, years):
#                 player1 = Player(AI("rule", x))
#                 player2 = Player(AI("constant", y))
#                 # randomly choose who goes first
#                 player= random.randint(1,2)
#                 play_game(player, player1, player2, False)
#                 # if(i%(years/10)==0):
#                 #     print(player1wins, player2wins)
#                 if player1.points>player2.points:
#                     player1wins+=1
#                 else:
#                     player2wins+=1

#             # print("Player 1 wins: ", player1wins, "with ",x)
#             # print("Player 2 wins: ", player2wins, "with ",y)
#             # print(x, y, math.trunc(player1wins/years*100))
#             data.append((x, y, math.trunc(player1wins/years*100)))
#             # print(data)
#             # print(x, y, "{:2f}".format(player1wins/player2wins*100))
#     # print("Player 1 goes first: ", player11st)
#     print(data)
#     # export to csv
#     with open('data.csv', 'w', newline='') as myfile:
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         wr.writerow(data)

def sim_play_one_game():
    player1 = Player(AI("rule", 28))
    player2 = Player(AI("constant", 8))
    play_game(player1, player2)

# def sim3():
#     global test
#     test=True
#     player1wins = 0
#     player2wins = 0
#     print("starting...")
#     for i in range(0, years):
#         if i % 100 == 0: print("Year: ", i)
#         player1 = Player(AI("rule", 28))
#         player2 = Player(AI("rule", 28))
#         # randomly choose who goes first
#         player = random.randint(1, 2)
#         play_game(player, player1, player2, False)
#         # if(i%(years/10)==0):
#         #     print(player1wins, player2wins)
#         if player1.points > player2.points:
#             player1wins += 1
#         else:
#             player2wins += 1
#     print("Player 1 won: ", player1wins)
#     print("Player 2 won: ", player2wins)

# sim_play_one_game()
