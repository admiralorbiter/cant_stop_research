import random
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    BLACK = 4
    WHITE = 5

class Tile:
    def __init__(self, color):
        self.color = color

class Factory:
    def __init__(self):
        self.tiles = []

    def refill_tiles(self, tiles):
        self.tiles.extend(tiles)

    def remove_tiles(self, color):
        removed_tiles = [tile for tile in self.tiles if tile.color == color]
        self.tiles = [tile for tile in self.tiles if tile.color != color]
        return removed_tiles

    def get_available_colors(self):
        return set(tile.color for tile in self.tiles)

    def __str__(self):
        return ' '.join([tile.color.name for tile in self.tiles])

class PlayerBoard:
    def __init__(self):
        self.pattern_lines = [[] for _ in range(5)]
        self.wall = [[False for _ in range(5)] for _ in range(5)]
        self.floor_line = []
        self.score = 0

    def add_tile_to_pattern_line(self, tile, line_number):
        if len(self.pattern_lines[line_number]) < line_number + 1:
            self.pattern_lines[line_number].append(tile)
            return True
        else:
            return False

    def move_tiles_to_wall(self):
        for line_number, line in enumerate(self.pattern_lines):
            if len(line) == line_number + 1:
                tile_color = line[0].color
                wall_row = (tile_color.value - 1 - line_number) % 5
                if not self.wall[wall_row][line_number]:
                    self.wall[wall_row][line_number] = True
                    self.score += 1  # Update the score
                    self.pattern_lines[line_number] = []
        self.floor_line = []

    def get_valid_moves(self, tile_color):
        valid_moves = []
        for line_number, line in enumerate(self.pattern_lines):
            if not line or (line[0].color == tile_color and len(line) < line_number + 1):
                valid_moves.append(line_number)
        return valid_moves

    def add_tile_to_floor_line(self, tile):
        self.floor_line.append(tile)

    def calculate_score(self):
        pass

    def __str__(self):
        pass

class Bag:
    def __init__(self):
        self.tiles = []
        self.refill_bag()

    def refill_bag(self):
        self.tiles = [Tile(color) for color in Color for _ in range(20)]  # 20 tiles of each color
        random.shuffle(self.tiles)

    def draw_tiles(self, num_tiles):
        drawn_tiles = self.tiles[:num_tiles]
        self.tiles = self.tiles[num_tiles:]
        
        if len(self.tiles) == 0:
            self.refill_bag()
        
        return drawn_tiles

class DiscardPile:
    def __init__(self):
        self.tiles = []

    def add_tiles(self, tiles):
        self.tiles.extend(tiles)

    def empty(self):
        discarded_tiles = self.tiles
        self.tiles = []
        return discarded_tiles

    def __str__(self):
        return ' '.join([tile.color.name for tile in self.tiles])

def setup_game(num_players):
    bag = Bag()
    discard_pile = DiscardPile()
    player_boards = [PlayerBoard() for _ in range(num_players)]

    num_factories = 5 if num_players == 2 else (7 if num_players == 3 else 9)
    factories = [Factory() for _ in range(num_factories)]
    for factory in factories:
        factory.refill_tiles(bag.draw_tiles(4))

    center = []
    starting_player = random.randint(0, num_players - 1)

    return bag, discard_pile, player_boards, factories, center, starting_player

def player_turn(player, factories, center, player_board, discard_pile):
    display_factories(factories, center)
    display_player_board(player_board)

    selected_factory = int(get_player_input("Select factory (0 for center): "))
    if selected_factory == 0:
        source = center
    else:
        source = factories[selected_factory - 1]

    selected_color = get_player_input("Select color: ").upper()
    selected_color = Color[selected_color]

    tiles_to_take = source.remove_tiles(selected_color)
    if selected_factory != 0:
        center.extend(source.tiles)
        source.tiles = []

    valid_moves = player_board.get_valid_moves(selected_color)
    if valid_moves:
        line_number = int(get_player_input(f"Select pattern line number ({', '.join(map(str, valid_moves))}): "))
        added_to_line = player_board.add_tile_to_pattern_line(tiles_to_take.pop(0), line_number)
        if not added_to_line:
            player_board.add_tile_to_floor_line(tiles_to_take.pop(0))
    while tiles_to_take:
        player_board.add_tile_to_floor_line(tiles_to_take.pop(0))

    discard_pile.add_tiles(tiles_to_take)

def end_round(player_boards, factories, bag, discard_pile):
    for player_board in player_boards:
        player_board.move_tiles_to_wall()

    discarded_tiles = discard_pile.empty()
    bag.tiles.extend(discarded_tiles)

    for factory in factories:
        factory.refill_tiles(bag.draw_tiles(4))

    center = []

def check_game_end(player_boards):
    for player_board in player_boards:
        if any(all(row) for row in player_board.wall):
            return True
    return False

def calculate_final_score(player_board):
    # Add points for completed rows
    for row in player_board.wall:
        if all(row):
            player_board.score += 2

    # Add points for completed columns
    for col in range(5):
        if all(player_board.wall[row][col] for row in range(5)):
            player_board.score += 7

    # Add points for same-color tiles in rows and columns
    for color in Color:
        row_count = sum(row.count(color) for row in player_board.wall)
        col_count = sum(col.count(color) for col in zip(*player_board.wall))
        if row_count == 5 or col_count == 5:
            player_board.score += 10

    return player_board.score

def display_factories(factories, center):
    print("Factories:")
    for i, factory in enumerate(factories, 1):
        print(f"{i}: {factory}")

    print("Center:")
    print(center)

def display_player_board(player_board):
    print("Player board:")
    # Implement a way to display the player board in a user-friendly format

def get_player_input(prompt):
    return input(prompt)

def display_winner(winner, player_boards):
    print(f"Player {winner + 1} is the winner!")
    print("Final scores:")
    for i, player_board in enumerate(player_boards, 1):
        print(f"Player {i}: {player_board.score}")

def get_available_colors_from_source(source):
    if isinstance(source, Factory):
        return source.get_available_colors()
    elif isinstance(source, list):  # Assuming it's the center
        return set(tile.color for tile in source)

def ai_make_decision(player_board, factories, center):
    available_moves = []
    sources = [center] + factories
    for source_index, source in enumerate(sources):
        available_colors = get_available_colors_from_source(source)
        for color in available_colors:
            valid_moves = player_board.get_valid_moves(color)
            if valid_moves:
                for line_number in valid_moves:
                    available_moves.append((source_index, color, line_number))

    if available_moves:
        return random.choice(available_moves)
    else:
        return None
def remove_tiles_from_source(source, color):
    if isinstance(source, Factory):
        return source.remove_tiles(color)
    elif isinstance(source, list):  # Assuming it's the center
        tiles_to_remove = [tile for tile in source if tile.color == color]
        source[:] = [tile for tile in source if tile.color != color]
        return tiles_to_remove

def ai_turn(player, factories, center, player_board, discard_pile):
    decision = ai_make_decision(player_board, factories, center)
    if decision is None:
        return  # No valid moves available, end the turn
    
    selected_factory, selected_color, line_number = decision

    if selected_factory == 0:
        source = center
    else:
        source = factories[selected_factory - 1]

    tiles_to_take = remove_tiles_from_source(source, selected_color)
    if selected_factory != 0:
        center.extend(source.tiles)
        source.tiles = []

    added_to_line = player_board.add_tile_to_pattern_line(tiles_to_take.pop(0), line_number)
    if not added_to_line:
        player_board.add_tile_to_floor_line(tiles_to_take.pop(0))
    while tiles_to_take:
        player_board.add_tile_to_floor_line(tiles_to_take.pop(0))

    discard_pile.add_tiles(tiles_to_take)

def play_game(num_players):
    bag, discard_pile, player_boards, factories, center, current_player = setup_game(num_players)

    game_end = False
    while not game_end:
        for player in range(num_players):
            ai_turn(player, factories, center, player_boards[player], discard_pile)
            end_round(player_boards, factories, bag, discard_pile)
            game_end = check_game_end(player_boards)
            if game_end:
                break

    final_scores = [calculate_final_score(player_board) for player_board in player_boards]
    winner = final_scores.index(max(final_scores))
    display_winner(winner, player_boards)

if __name__ == "__main__":
    num_players = 2  # Change this to the desired number of players
    play_game(num_players)