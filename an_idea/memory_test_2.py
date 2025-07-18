import pickle
import os
import random
from noise import pnoise2

SAVE_FILE = "cave_memory.pkl"

def save_tile_memory():
    with open(SAVE_FILE, "wb") as f:
        pickle.dump(tile_memory, f)

def load_tile_memory():
    global tile_memory
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            tile_memory = pickle.load(f)

# Cave generation settings
CHUNK_SIZE = 31
CAVE_SCALE = 0.08
CAVE_THRESHOLD = 0.1

# Emoji tiles
TILE_WALL = "⬛"
TILE_CAVE = "⬜"
TILE_COAL = "⚫"
TILE_IRON = "🪨 "
TILE_CRYSTAL = "🔷"
TILE_MUSHROOM = "🍄"
TILE_WATER = "💧"
TILE_PLAYER = "😄"

# Feature probabilities
FEATURES = [
    (TILE_COAL, 0.03),
    (TILE_IRON, 0.025),
    (TILE_CRYSTAL, 0.005),
    (TILE_MUSHROOM, 0.035),
    (TILE_WATER, 0.005),
]

# Function to determine if a tile is cave or wall based on noise
def is_cave(x, y):
    value = pnoise2(x * CAVE_SCALE, y * CAVE_SCALE)
    return value > CAVE_THRESHOLD

# Function to place a random feature (coal, iron, etc.) or return cave
def cave_tile_with_features(x, y):
    if not is_cave(x, y):
        return TILE_WALL
    random.seed((x * 928371 + y * 123457) % 9999999)  # deterministic randomness
    for tile, chance in FEATURES:
        if random.random() < chance:
            return tile
    return TILE_CAVE

# Modified rendering function with memory-aware tiles

#find nearest cave tile:
def find_nearest_cave_tile_recursive(x, y, max_depth=62, visited=None):
    if visited is None:
        visited = set()

    # Avoid rechecking the same tile
    if (x, y) in visited:
        return None
    visited.add((x, y))

    # Base case — tile is a cave
    if is_cave(x, y):
        return x, y

    # Prevent infinite depth
    if len(visited) > max_depth ** 2:
        return None

    # Explore outward (N, S, E, W)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        result = find_nearest_cave_tile_recursive(x + dx, y + dy, max_depth, visited)
        if result:
            return result

    return None


# Persistent memory for mined or altered cave tiles
tile_memory = {}

# Modified cave tile fetcher with memory lookup
def get_tile_with_memory(x, y):
    # First check memory
    if (x, y) in tile_memory:
        return tile_memory[(x, y)]
    
    # Otherwise generate the tile
    if not is_cave(x, y):
        tile = TILE_WALL
    else:
        rand_seed = (x * 928371 + y * 123457) % 999999
        random.seed(rand_seed)
        for emoji, chance in FEATURES:
            if random.random() < chance:
                tile = emoji
                break
        else:
            tile = TILE_CAVE

    return tile

# Modified rendering function with memory-aware tiles
def draw_infinite_cave_with_memory(center_x, center_y):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = ""
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            if i == center_x and j == center_y:
                row += TILE_PLAYER
            else:
                row += get_tile_with_memory(i, j)
        output.append(row)
    return "\n".join(output)

# Simulate mining at a position
def mine_tile(x, y):
    original = get_tile_with_memory(x, y)
    if original in [TILE_COAL, TILE_IRON, TILE_CRYSTAL, TILE_MUSHROOM, TILE_WATER]:
        tile_memory[(x, y)] = TILE_CAVE
        save_tile_memory()  # 🔄 Save after change


# Example position
if __name__ == "__main__":
    center_x = 0
    center_y = 0
    player_input = ""
    player_x, player_y = find_nearest_cave_tile_recursive(center_x, center_y)

    load_tile_memory()
    while player_input != "0":

        cave_chunk = draw_infinite_cave_with_memory(player_x, player_y)
        print(cave_chunk)
        raw_player_input = input("x,y:")
        if raw_player_input == "mine":
            mine_tile(player_x, player_y)
        else:
            raw_player_input = raw_player_input.split(",")
            player_input = []
            for pi in raw_player_input:
                player_input.append(int(pi))
            player_x +=player_input[0]
            player_y +=player_input[1]