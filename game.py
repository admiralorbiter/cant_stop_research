from player import Player
from board import Board
import copy
import random

def make_move(b, choice):
    if type(choice) is tuple:
        eval = b.evaluate_move(choice[0])
        print(eval)
        eval = b.evaluate_move(choice[1])
        print(eval)
    else:
        eval = b.evaluate_move(choice)
        print(eval)
#     if choice not in player.move_list and len(player.move_list)>=3:
#         return 0, player
#     eval = b.evaluate_move(player_num, choice)
#     if eval==True:
#         b.board[choice-2][player_num]+=1
#         player.add_move(choice)
#         if test:print("New Move List: ",player.move_list)
#         eval = b.evaluate_move(player_num, choice)
#     if eval==False:
#         if test:print("Player took column ", choice)
#         taken_columns.append(choice)
#         return 1, player
#     else:
#         return 0, player

#TODO: Implement an AI that carefully chooses moves
def make_choice(results, player):
    if len(player.move_list)<3:                # if the player has less than 3 moves, randomly choose a move
        return results[random.randint(0,2)]
    else:                                       # If the player has 3 moves, then they have to pick a move that is the move list
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
        return choices

def complete_turn(b, player):
    turn = 0
    oldboard = copy.deepcopy(b.board)          # copy the board so if they go bust, we can revert
    dice = b.roll_dice(4, 6)                   # roll the dice
    results = b.dice_combinations(dice)        # calculate all possible combinations
    choice = make_choice(results, player)      # choose a combination
    turn+=1
    if choice!=None:
        points= make_move(b, choice)
        # player.points+=points
        # if points>0:
        #     player1.move_list=temp_player.move_list
        #     player1.move_calc(choice[0])
        # points, temp_player= make_move(b, player, choice[1], player2, test)
        # player1.points+=points
        # if points>0: 
        #     player1.move_calc(choice[1])
        #     player1.move_list=temp_player.move_list
        # next=player1.ai.stop(player1, turns)

def play_game(player1, player2):
    player = random.randint(1,2)                # randomly select who goes first, 1=Player 1 and 2=Player 2
    b = Board()                                 # initialize new board
    while player1.points<3 and player2.points<3:
        if player==1:
            complete_turn(b, player1)
        else:
            complete_turn(b, player2)

# def play_game(player, player1, player2, test):
#     global taken_columns
#     taken_columns=[]
#     b = Board()
#     if test:print(b.board)
#     if test:print("Player ", player, " turn")
#     turns=0
#     oldboard=copy.deepcopy(b)
#     while player1.points<3 and player2.points<3:
#         dice=b.roll_dice(4, 6)
#         # print(dice)
#         results=b.calc_single_odds(dice)
#         #randomly pick a result
#         # choice=results[random.randint(0,2)]
#         # print("Results: ", results)
#         if player==1:
#             choice = make_choice(results, player1)
#         else:
#             choice = make_choice(results, player2)
#         if test:print("Choice: ",choice)
#         next=False
#         # if random.randint(0, 3)==0:
#         #     next=True
#         if player==1:
#             turns+=1
#             next=True
#             if test:print("Player 1 moves", player1.move_list)
#             if choice!=None:
#                 points, temp_player= make_move(b, player, choice[0], player2, test)
#                 player1.points+=points
#                 if points>0:
#                     player1.move_list=temp_player.move_list
#                     player1.move_calc(choice[0])
#                 points, temp_player= make_move(b, player, choice[1], player2, test)
#                 player1.points+=points
#                 if points>0: 
#                     player1.move_calc(choice[1])
#                     player1.move_list=temp_player.move_list
#                 if test:print("Move Num: ", player1.move_num)
#                 next=player1.ai.stop(player1, turns)
#             if choice==None:
#                 # if test:print(b, b.board)
#                 # if test:print(oldboard, oldboard.board)
#                 b=copy.deepcopy(oldboard)
#                 if test:print("BUSTED!!!!")
#                 # if test:print(b.board)
#             if next:
#                 if test:print(b.board)
#                 player=2
#                 player2.move_list=[]
#                 player2.move_num=0
#                 oldboard=copy.deepcopy(b)
#                 if test:print(player1.points, player2.points)
#                 if test:print()
#                 if test:print("Player ", player, " turn")
#                 turns=0
#         else:
#             turns+=1
#             next=True
#             if test:print("Player 2 moves", player2.move_list)
#             if choice!=None:
#                 points, temp_player = make_move(b, player, choice[0], player2, test)
#                 player2.points+=points
#                 if points>0: 
#                     player2.move_calc(choice[0])
#                     player2.move_list=temp_player.move_list
#                 points, temp_player = make_move(b, player, choice[1], player2, test)
#                 player2.points+=points
#                 if points>0: 
#                     player2.move_calc(choice[1])
#                     player2.move_list=temp_player.move_list
#                 if test:print("Move Num: ", player2.move_num)
#                 next=player2.ai.stop(player2, turns)
#             if choice==None:
#                 b=copy.copy(oldboard)
#                 if test:print("BUSTED!!!!")
#             if next:
#                 if test:print(b.board)
#                 player=1
#                 player1.move_list=[]
#                 player1.move_num=0
#                 oldboard=copy.deepcopy(b)
#                 if test:print(player1.points, player2.points)
#                 if test:print()
#                 if test:print("Player ", player, " turn")
#                 turns=0
#     if test:
#         print()
#         print("Columns: ",taken_columns)
#         print("Player 1:", player1.points)
#         print("Player 2:", player2.points)
#         b.print_board()
#         print(b.board)

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

# def sim2():
#     global test
#     test=True
#     startPlayer= random.randint(1,2)
#     player1 = Player(AI("rule", 28))
#     player2 = Player(AI("constant", 8))
#     play_game(startPlayer, player1, player2, test)

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

# sim2()
# # sim1()
# # sim3()
