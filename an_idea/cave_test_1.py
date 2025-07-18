from noise import pnoise2
import random

# Cave generation settings
MAP_WIDTH = 60
MAP_HEIGHT = 30
CAVE_SCALE = 0.08
FEATURE_SCALE = 0.15

# Emoji tiles
TILE_WALL = "⬛"
TILE_CAVE = "⬜"
TILE_COAL = "⚫"
TILE_IRON = "🪨"
TILE_CRYSTAL = "🔷"
TILE_MUSHROOM = "🍄"
TILE_WATER = "💧"

# Noise threshold for carving open space
CAVE_THRESHOLD = 0.25

# Probabilities for placing features (if in open space)
FEATURES = [
    (TILE_COAL, 0.03),
    (TILE_IRON, 0.025),
    (TILE_CRYSTAL, 0.01),
    (TILE_MUSHROOM, 0.01),
    (TILE_WATER, 0.008),
]

# Generate cave map with features
def generate_cave_map(width, height):
    cave_map = []
    for y in range(height):
        row = ""
        for x in range(width):
            # Determine open space or wall
            cave_val = pnoise2(x * CAVE_SCALE, y * CAVE_SCALE)
            if cave_val > CAVE_THRESHOLD:
                # Open space — check for features
                feature_val = pnoise2(x * FEATURE_SCALE, y * FEATURE_SCALE, base=42)
                placed = False
                for emoji, prob in FEATURES:
                    # Use value to pseudo-randomly pick
                    if feature_val > 0 and feature_val % 1 < prob:
                        row += emoji
                        placed = True
                        break
                if not placed:
                    row += TILE_CAVE
            else:
                row += TILE_WALL
        cave_map.append(row)
    return "\n".join(cave_map)

# Generate and print the cave
cave_output = generate_cave_map(MAP_WIDTH, MAP_HEIGHT)
print(cave_output)
