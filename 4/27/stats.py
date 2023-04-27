#Estimate for the number of rolls to make for a statistically safe move in the game of Can't Stop
#Given the columns, it will predict how many moves you can safely make before you should stop without taking in account the current state of the board

import random
import itertools
import numpy as np

columns = [2, 6, 7]

def roll_dice():
    dice = [random.randint(1, 6) for _ in range(4)]
    return dice

def possible_moves(dice):
    return set(a + b for a, b in itertools.combinations(dice, 2))

def can_move(columns, moves):
    return any(move in columns for move in moves)

def average_safe_rolls(columns, num_trials=100000):
    total_rolls = 0
    for _ in range(num_trials):
        rolls = 0
        while can_move(columns, possible_moves(roll_dice())):
            rolls += 1
        total_rolls += rolls
    return total_rolls / num_trials

num_trials = 100000
average_rolls = average_safe_rolls(columns, num_trials)
print(f"The statistically safe number of rolls to make for columns {columns} is approximately {average_rolls:.2f}.")