
import random
import math
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

# Constants for difficulty visualization----------------------------
DIFFICULTY_EMOJIS = {
    1: "1️⃣ ", 2: "2️⃣ ", 3: "3️⃣ ", 4: "4️⃣ ", 5: "5️⃣ ",
    6: "6️⃣ ", 7: "7️⃣ ", 8: "8️⃣ ", 9: "9️⃣ ", 10: "🔟 "
}

MAX_DIFFICULTY = 10
CENTER_X = MAP_SIZE // 2
CENTER_Y = MAP_SIZE // 2
STARTING_DIFFICULTY = 7

# Function to calculate difficulty based on distance from center
def calculate_difficulty_with_start(x, y, start_difficulty=STARTING_DIFFICULTY, max_difficulty=10):
    dx = abs(x - CENTER_X)
    dy = abs(y - CENTER_Y)
    distance = (dx**2 + dy**2) ** 0.5
    max_distance = math.sqrt((MAP_SIZE // 2) ** 2 + (MAP_SIZE // 2) ** 2)

    # Scale down from starting difficulty instead of from 10
    difficulty = start_difficulty - (int((distance / max_distance) * start_difficulty)+1)
    return max(1, min(max_difficulty, difficulty))

# Generate difficulty map over the carved dungeon floor
difficulty_map = [["⬛" for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
for y in range(MAP_SIZE):
    for x in range(MAP_SIZE):
        if dungeon_map[y][x] == TILE_FLOOR:
            level = calculate_difficulty_with_start(x, y, STARTING_DIFFICULTY)
            difficulty_map[y][x] = DIFFICULTY_EMOJIS[level]
difficulty_map[CENTER_X][CENTER_Y] = DIFFICULTY_EMOJIS[STARTING_DIFFICULTY]
# Print final difficulty map
for row in difficulty_map:
    print("".join(row))
