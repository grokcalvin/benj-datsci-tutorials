import random

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

from noise import pnoise2

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

# Infinite cave map generator centered on (center_x, center_y)
def draw_infinite_cave(center_x, center_y):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = ""
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            if i == center_x and j == center_y:
                row += TILE_PLAYER
            else:
                row += cave_tile_with_features(i, j)
        output.append(row)
    return "\n".join(output)

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



# Example position
if __name__ == "__main__":
    center_x = 0
    center_y = 3000

    is_cave_x, is_cave_y = find_nearest_cave_tile_recursive(center_x, center_y)

    cave_chunk = draw_infinite_cave(is_cave_x, is_cave_y)
    print(cave_chunk)
