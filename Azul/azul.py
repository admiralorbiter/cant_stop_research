import random
from termcolor import colored
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
        return "green"
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
    for i in range(0, len(factory_displays[4])):
         print(colored(factory_displays[4][i], match_color(factory_displays[4][i])), end=" ")
    print()

def draw_from_factory(player, factory_number, color):
    if color in factory_displays[factory_number]:
        count = factory_displays[factory_number].count(color)
        factory_displays[factory_number].remove(color)
        if player == 1:
            for i in range(0, count):
                player1_tiles.append(color)
        else:
            for i in range(0, count):
                player2_tiles.append(color)
        # for i in range(0, 4-count):
        #     middle_display.append(factory_displays[factory_number].pop(0))
        middle_display.append(factory_displays[factory_number])
        factory_displays[factory_number]= []
        return count
    else:
        return 0


def number_of_colors_in_factory(factory_number):
    return len(set(factory_displays[factory_number]))

def init():
    factory_displays[0] = draw_tiles(4)
    factory_displays[1] = draw_tiles(4)
    factory_displays[2] = draw_tiles(4)
    factory_displays[3] = draw_tiles(4)
    factory_displays[4] = draw_tiles(4)

# create a copy of the states to be used
def create_copy_of_states():
    board_state_copy = copy.deepcopy(board_state)
    factory_displays_copy = copy.deepcopy(factory_displays)
    middle_display_copy = []
    pattern_line_copy = copy.deepcopy(pattern_line)
    tile_bag_copy = copy.deepcopy(tile_bag)
    player1_tiles_copy = []
    player2_tiles_copy = []
    return board_state_copy, factory_displays_copy, middle_display_copy, pattern_line_copy, tile_bag_copy, player1_tiles_copy, player2_tiles_copy



#resets the states based on the copies created
def reset_states_based_on_copies(board_state_copy, factory_displays_copy, pattern_line_copy, tile_bag_copy, player1_tiles_copy, player2_tiles_copy):
    middle_display = []
    board_state = copy.deepcopy(board_state_copy)
    factory_displays = copy.deepcopy(factory_displays_copy)
    pattern_line = copy.deepcopy(pattern_line_copy)
    tile_bag = copy.deepcopy(tile_bag_copy)
    player1_tiles = copy.deepcopy(player1_tiles_copy)
    player2_tiles = copy.deepcopy(player2_tiles_copy)
    return board_state, factory_displays, middle_display, pattern_line, tile_bag, player1_tiles, player2_tiles

if __name__ == "__main__":
    init()
    zero = number_of_colors_in_factory(0)
    one = number_of_colors_in_factory(1)
    two = number_of_colors_in_factory(2)
    three = number_of_colors_in_factory(3)
    board_state_copy, factory_displays_copy, middle_display_copy, pattern_line_copy, tile_bag_copy, player1_tiles_copy, player2_tiles_copy = create_copy_of_states()
    #Start of simulation
    print(factory_displays_copy)
    print_factory_displays()
    draw_from_factory(1, 0, 1)
    draw_from_factory(2, 1, 1)
    draw_from_factory(1, 2, 1)
    draw_from_factory(2, 3, 1) 
    print("Player 1 ", player1_tiles)
    print("Player 2 ",player2_tiles)
    print(middle_display)
    print_factory_displays()
    print(factory_displays_copy)
    #end of simulation
    board_state, factory_displays, middle_display, pattern_line, tile_bag, player1_tiles, player2_tiles=reset_states_based_on_copies(board_state_copy, factory_displays_copy, pattern_line_copy, tile_bag_copy, player1_tiles_copy, player2_tiles_copy)
    print_factory_displays()
