import itertools
import random
import random
from termcolor import colored
import itertools
import copy

blue = 1
red = 2
yellow = 3
black = 4
white = 5

#board state empty 5 by 5 array
board_state = [[0 for x in range(5)] for y in range(5)]
#5 factory displays, each an array of 4 with a max of 4 different colors
factory_displays = [[0 for x in range(4)] for y in range(5)]
#middle display
middle_display = []
#pattern line, array of 5 arrays starting with 1 and going to 5
pattern_line = [[0 for x in range(y+1)] for y in range(5)]
#tile bag, array of 100 tiles with 20 of each color
tile_bag = [blue for x in range(20)] + [red for x in range(20)] + [yellow for x in range(20)] + [black for x in range(20)] + [white for x in range(20)]
#player 1 tile array - list of the tiles drawn and the order they were drawn
player1_tiles = []
#player 2 tile array - list of the tiles drawn and the order they were drawn
player2_tiles = []

# print(board_state)
# print(factory_displays)
# print(middle_display)
# print(pattern_line)

def print_board():
    print("Board State:")
    for i in range(0, 5):
        for j in range(0, 5):
            print(board_state[i][j], end=" ")
        print()

def print_pattern_line():
    for i in range(0, 5):
        for j in range(0, i+1):
            print(pattern_line[i][j], end=" ")
        print()

def draw_tiles(number_of_tiles):
    tiles = []
    for i in range(0, number_of_tiles):
        tiles.append(tile_bag.pop(random.randint(0, len(tile_bag)-1)))
    return tiles
    
def match_color(color):
    if color == 1:
        return "blue"
    elif color == 2:
        return "red"
    elif color == 3:
        return "yellow"
    elif color == 4:
        return "black"
    elif color == 5:
        return "white"

def print_factory_displays():
    for i in range(0, len(factory_displays[0])):
       print(colored(factory_displays[0][i], match_color(factory_displays[0][i])), end=" ")
    print()
    for i in range(0, len(factory_displays[1])):
       print(colored(factory_displays[1][i], match_color(factory_displays[1][i])), end=" ")
    print()
    for i in range(0, len(factory_displays[2])):
       print(colored(factory_displays[2][i], match_color(factory_displays[2][i])), end=" ")
    print()
    for i in range(0, len(factory_displays[3])):
       print(colored(factory_displays[3][i], match_color(factory_displays[3][i])), end=" ")
    print()
    for i in range(0, len(middle_display)):
         print(colored(middle_display[i], match_color(middle_display[i])), end=" ")
    print()

# def draw_from_factory(factory_number, color):
#     if color in factory_displays[factory_number]:
#         count = factory_displays[factory_number].count(color)
#         factory_displays[factory_number].remove(color)
#         for i in range(0, 4-count):
#             middle_display.append(factory_displays[factory_number].pop(0))
#         factory_displays[factory_number]= []
#         return count
#     else:
#         return 0
    
def draw_from_factory(display, color):
    if color in display:
        count = display.count(color)
        display.remove(color)
        for i in range(0, 4-count):
            if display:  # Check if the display is not empty
                middle_display.append(display.pop(0))
        display= []
        return count
    else:
        return 0
    
def draw_permutations(factory_displays, middle_display):
    all_permutations = []
    middle_display_index = len(factory_displays)

    for n in range(len(factory_displays), 0, -1):
        for factory_permutation in itertools.permutations(range(n)):
            permutation = factory_permutation + (middle_display_index,)
            hand_states = [[], []]

            # Reset factory displays and middle_display for each permutation
            factory_displays_copy = copy.deepcopy(factory_displays)
            middle_display_copy = []
            middle_display = []

            for draw_location in permutation:
                if draw_location < middle_display_index:
                    selected_tile = random.choice(factory_displays_copy[draw_location])
                    count = draw_from_factory(factory_displays_copy[draw_location], selected_tile)
                    hand_states[0].extend([selected_tile] * count)
                else:
                    while middle_display_copy:
                        selected_tile = random.choice(middle_display_copy)
                        hand_states[0].append(selected_tile)
                        middle_display_copy.remove(selected_tile)

            all_permutations.append((permutation, hand_states))

    return all_permutations

factory_displays[0] = draw_tiles(4)
factory_displays[1] = draw_tiles(4)
factory_displays[2] = draw_tiles(4)
factory_displays[3] = draw_tiles(4)
factory_displays[4] = draw_tiles(4)
print_factory_displays()
permutations_and_hand_states = draw_permutations(factory_displays, middle_display)
for i, (permutation, hand_states) in enumerate(permutations_and_hand_states):
    print(f"Permutation {i + 1}: {permutation}")
    print(f"Hand states: {hand_states}\n")