
import random
import math
import noise

# Constants
MAP_SIZE = 31
NUM_WORMS = 10
WORM_LENGTH = 15

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
    6: "6️⃣ ", 7: "7️⃣ ", 8: "8️⃣ ", 9: "9️⃣ ", 10: "🔟"
}

MAX_DIFFICULTY = 10
CENTER_X = MAP_SIZE // 2
CENTER_Y = MAP_SIZE // 2
STARTING_DIFFICULTY = 7

# Function to calculate difficulty based on distance from center
def calculate_difficulty_with_noise(x, y, start_difficulty=STARTING_DIFFICULTY, max_difficulty=10, noise_scale=0.5, noise_strength=2.0):
    dx = abs(x - CENTER_X)
    dy = abs(y - CENTER_Y)
    distance = math.sqrt(dx ** 2 + dy ** 2)
    max_distance = math.sqrt((MAP_SIZE // 2) ** 2 + (MAP_SIZE // 2) ** 2)

    # Base difficulty decreases with distance from center
    base_difficulty = start_difficulty - (((distance / max_distance) * start_difficulty)+1)

    # Add noise for variety
    noise_val = noise.pnoise2(x * noise_scale, y * noise_scale) -0.25
    noise_adjustment = noise_val * noise_strength  # can be positive or negative

    difficulty = int(round(base_difficulty + noise_adjustment))
    return max(1, min(max_difficulty, difficulty))

# Rebuild the difficulty map with noise-enhanced values
difficulty_map = [["⬛" for _ in range(MAP_SIZE)] for _ in range(MAP_SIZE)]
for y in range(MAP_SIZE):
    for x in range(MAP_SIZE):
        if dungeon_map[y][x] == TILE_FLOOR:
            level = calculate_difficulty_with_noise(x, y)
            difficulty_map[y][x] = DIFFICULTY_EMOJIS[level]
difficulty_map[CENTER_X][CENTER_Y] = DIFFICULTY_EMOJIS[STARTING_DIFFICULTY]
# Print final difficulty map
for row in difficulty_map:
    print("".join(row))
