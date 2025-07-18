import random
from map_features_and_memory_test_3 import *
import pickle
import os

# Memory for saved villages
village_memory = {}

# File path
VILLAGE_MEMORY_FILE = "village_memory.pkl"


def save_villages():
    with open(VILLAGE_MEMORY_FILE, 'wb') as f:
        pickle.dump(village_memory, f)

def load_villages():
    global village_memory
    if os.path.exists(VILLAGE_MEMORY_FILE):
        with open(VILLAGE_MEMORY_FILE, 'rb') as f:
            village_memory = pickle.load(f)
    else:
        village_memory = {}


def village_exists_at(chunk_x, chunk_y):
    return (chunk_x, chunk_y) in village_memory


# Village settings
VILLAGE_WIDTH = 31
VILLAGE_HEIGHT = 31
PATH = "🟫"

# Building emojis with weights
BUILDINGS = {
    "🏠": 16,   # house
    "🌽": 4,    # farm
    "⚒️ ": 2,    # blacksmith
    "🛒": 3,    # market
    "🏨": 3,    # inn
    "⛪": 2,    # church
    "🐄": 2,    # barn
    "🛡️ ": 2     # guardpost
}

# Generate a weighted list for random.choices
BUILDING_EMOJIS = list(BUILDINGS.keys())
BUILDING_WEIGHTS = list(BUILDINGS.values())

# Directions (no diagonals)
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]  # N, E, S, W

# Check if coordinates are within bounds
def in_bounds(x, y):
    return 0 <= x < VILLAGE_WIDTH and 0 <= y < VILLAGE_HEIGHT

# Check if there's already a parallel path next to this one
def has_parallel_path(village, x, y, dx, dy):
    if dx == 0:
        for offset in [-1, 1]:
            if in_bounds(x + offset, y) and village[y][x + offset] == PATH:
                return True
    if dy == 0:
        for offset in [-1, 1]:
            if in_bounds(x, y + offset) and village[y + offset][x] == PATH:
                return True
    return False

# Generate the village
def generate_village(width, height, biome_name):

    # Get default background tile from biome terrain palette
    default_tile = BIOMES[biome_name]["emoji"]  # e.g., 💧 or 🌾
    
    # Initialize the grid with biome-based background
    village = [[default_tile for _ in range(width)] for _ in range(height)]

    # ... your existing village logic for paths/buildings ...
    
    center_x, center_y = VILLAGE_WIDTH // 2, VILLAGE_HEIGHT // 2
    village[center_y][center_x] = "⛲"  # central fountain

    # Randomly select 2–4 starting directions
    num_start_paths = random.randint(2, 4)
    start_dirs = random.sample(DIRECTIONS, num_start_paths)
    paths = [(center_x, center_y, dx, dy,7) for dx, dy in start_dirs]

    visited = set()

    while paths:
        x, y, dx, dy, base_length = paths.pop()
        length = max(3, base_length + random.randint(-3, 3))  # add a bit of variety
        for _ in range(length):
            x += dx
            y += dy
            if not in_bounds(x, y):
                break
            if (x, y) in visited:
                continue
            if has_parallel_path(village, x, y, dx, dy):
                break  # cancel this path segment to avoid 2-wide paths
            village[y][x] = PATH
            visited.add((x, y))

            # Chance to add an offshoot in the perpendicular direction, with reduced length
            if random.random() < 0.10:
                perp_dx, perp_dy = -dy, dx
                paths.append((x, y, perp_dx, perp_dy, max(3, base_length - 2)))
            if random.random() < 0.10:
                perp_dx, perp_dy = dy, -dx
                paths.append((x, y, perp_dx, perp_dy, max(3, base_length - 2)))

            # Chance to place a building next to path
            for adj_dx, adj_dy in DIRECTIONS:
                adj_x, adj_y = x + adj_dx, y + adj_dy
                if in_bounds(adj_x, adj_y) and village[adj_y][adj_x] == default_tile:
                    if random.random() < 0.30:
                        village[adj_y][adj_x] = random.choices(BUILDING_EMOJIS, weights=BUILDING_WEIGHTS, k=1)[0]

    return village

def get_or_generate_village(chunk_x, chunk_y):
    load_villages()
    if not village_exists_at(chunk_x, chunk_y):
        biome = get_biome(chunk_x, chunk_y)
        village_grid = generate_village(CHUNK_SIZE, CHUNK_SIZE, biome)
        village_memory[(chunk_x, chunk_y)] = village_grid
        save_villages()
    return village_memory[(chunk_x, chunk_y)]

# Render the village
def draw_village(village):
    return "\n".join("".join(row) for row in village)

if __name__ == "__main__":
    # Generate and display the village
    X,Y = 0,4
    village = get_or_generate_village(X,Y)
    village_map = draw_village(village)
    print(village_map)
