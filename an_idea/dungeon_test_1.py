import random

# Constants
MAP_SIZE = 31
NUM_WORMS = 10
WORM_LENGTH = 20

# Tiles
TILE_WALL = "⬛"
TILE_FLOOR = "⬜"

# Directions: (dx, dy)
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Initialize map with walls
dungeon_map = [[TILE_WALL for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]

# Start worms at the center
start_x = MAP_SIZE // 2
start_y = MAP_SIZE // 2

def spawn_worm(x, y, steps):
    for _ in range(steps):
        # Carve current tile
        if 0 <= x < MAP_SIZE and 0 <= y < MAP_SIZE:
            dungeon_map[y][x] = TILE_FLOOR
        # Pick a random direction
        dx, dy = random.choice(DIRECTIONS)
        x += dx
        y += dy
        # Clamp position within bounds
        x = max(0, min(MAP_SIZE - 1, x))
        y = max(0, min(MAP_SIZE - 1, y))
    return

# Spawn all worms
for _ in range(NUM_WORMS):
    spawn_worm(start_x, start_y, WORM_LENGTH)

# Prepare map output
for row in dungeon_map:
    print("".join(row))