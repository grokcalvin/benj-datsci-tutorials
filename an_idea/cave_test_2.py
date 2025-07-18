from noise import pnoise2

# Settings
CHUNK_SIZE = 31
CAVE_SCALE = 0.04
FEATURE_SCALE = 0.15
CAVE_THRESHOLD = -0.25

# Emojis
TILE_WALL = "⬛"
TILE_CAVE = "⬜"
FEATURES = [
    ("⚫", 0.03),   # Coal
    ("🪨", 0.025),  # Iron
    ("🔷", 0.01),   # Crystal
    ("🍄", 0.01),   # Mushroom
    ("💧", 0.008),  # Water
]

# Get a single tile at a global (x, y)
def get_cave_tile(x, y):
    base_noise = pnoise2(x * CAVE_SCALE, y * CAVE_SCALE)
    if base_noise > CAVE_THRESHOLD:
        feature_noise = pnoise2(x * FEATURE_SCALE, y * FEATURE_SCALE, base=42)
        for symbol, chance in FEATURES:
            if feature_noise > 0 and feature_noise % 1 < chance:
                return symbol
        return TILE_CAVE
    else:
        return TILE_WALL

# Draw a 31x31 infinite cave centered on (center_x, center_y)
def draw_infinite_cave(center_x, center_y):
    output = []
    half = CHUNK_SIZE // 2
    for y in range(center_y - half, center_y + half + 1):
        row = ""
        for x in range(center_x - half, center_x + half + 1):
            if x == center_x and y == center_y:
                row += "😄"
            else:
                row += get_cave_tile(x, y)
        output.append(row)
    return "\n".join(output)

# Example usage
print(draw_infinite_cave(3000, 0))
