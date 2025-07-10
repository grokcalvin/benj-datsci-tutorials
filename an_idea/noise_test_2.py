import noise

# Tile and world setup
TILE_WIDTH = 20
TILE_HEIGHT = 20
SCALE = 0.1  # Lower = more zoomed out noise
OCTAVES = 6

terrain = [
    "🌊",  # 0.0 - 0.2: deep water
    "🌴",  # 0.2 - 0.4: beach
    "🌾",  # 0.4 - 0.6: plains
    "🌲",  # 0.6 - 0.8: forest
    "🔺",  # 0.8 - 1.0: mountains
]

def get_emoji(value):
    index = int(value * len(terrain))
    return terrain[min(index, len(terrain)-1)]

def generate_tile(tile_x, tile_y):
    for y in range(TILE_HEIGHT):
        row = ""
        for x in range(TILE_WIDTH):
            world_x = (tile_x * TILE_WIDTH + x) * SCALE
            world_y = (tile_y * TILE_HEIGHT + y) * SCALE
            val = noise.pnoise2(world_x, world_y, octaves=OCTAVES)
            norm_val = (val + 0.5)  # Normalize from ~[-0.5, 0.5] to [0, 1]
            row += get_emoji(norm_val)
        print(row)

# Example usage: generate the center tile (0, 0)
print("Center Tile (0, 0):")
generate_tile(0, 0)

print("\nEast Neighbor Tile (1, 0):")
generate_tile(1, 0)

print("\nSouth Neighbor Tile (0, 1):")
generate_tile(0, 1)