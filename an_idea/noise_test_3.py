import noise

# Constants
TILE_WIDTH = 10
TILE_HEIGHT = 10
SCALE_BIOME = 0.2   # Zoomed out: large smooth areas
SCALE_TERRAIN = 0.05 # Zoomed in: small features

# Define biomes
biome_defs = [
    ("desert", 0.2),
    ("plains", 0.4),
    ("forest", 0.6),
    ("tundra", 0.8),
    ("mountain", 1.0)
]

biome_tiles = {
    "desert": ["🟨", "🌵", "🌴", "  "],
    "plains": ["🌾", "🌻", "🌼", "  "],
    "forest": ["🌲", "🌳", "🍃", "  "],
    "tundra": ["❄️", "🌫️", "🌨️", "  "],
    "mountain": ["⛰️", "🪨", "🌋", "  "],
}

def get_biome(val):
    for name, threshold in biome_defs:
        if val <= threshold:
            return name
    return biome_defs[-1][0]

def get_tile_from_biome(biome, val):
    tiles = biome_tiles[biome]
    index = int(val * len(tiles))
    return tiles[min(index, len(tiles) - 1)]

def generate_tile(tile_x, tile_y):
    # 1. Determine the biome based on position
    biome_val = noise.pnoise2(tile_x * SCALE_BIOME, tile_y * SCALE_BIOME, octaves=4)
    biome_val = (biome_val + 0.5)  # Normalize
    biome = get_biome(biome_val)

    print(f"Tile ({tile_x}, {tile_y}) - Biome: {biome.upper()}")
    for y in range(TILE_HEIGHT):
        row = ""
        for x in range(TILE_WIDTH):
            # 2. Generate terrain for that biome
            world_x = (tile_x * TILE_WIDTH + x) * SCALE_TERRAIN
            world_y = (tile_y * TILE_HEIGHT + y) * SCALE_TERRAIN
            val = noise.pnoise2(world_x, world_y, octaves=6)
            norm_val = (val + 0.5)
            emoji = get_tile_from_biome(biome, norm_val)
            row += emoji
        print(row)

# Example usagage
y=0
for x in range(10):
    for y in range(10):
        generate_tile(x, y)