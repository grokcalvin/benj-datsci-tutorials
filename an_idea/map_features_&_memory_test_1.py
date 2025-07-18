import random
from noise import pnoise2
from collections import Counter
import pickle
import os

# Settings
CHUNK_SIZE = 31
BIOME_SCALE = 0.01
TERRAIN_SCALE = 0.1

SAVE_FILE = "world_memory.pkl"

SAVE_FILE = "world_data.pkl"

def save_world_data():
    with open(SAVE_FILE, "wb") as f:
        pickle.dump({
            "terrain_memory": terrain_memory,
            "feature_memory": feature_memory,
            "biome_chunk_memory": biome_chunk_memory
        }, f)

def load_world_data():
    global terrain_memory, feature_memory, biome_chunk_memory
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
            terrain_memory = data.get("terrain_memory", {})
            feature_memory = data.get("feature_memory", {})
            biome_chunk_memory = data.get("biome_chunk_memory", {})
    else:
        terrain_memory = {}
        feature_memory = {}
        biome_chunk_memory = {}

#load_memory
#access_memory
#save_memory

# Memory caches
terrain_memory = {}
feature_memory = {}
biome_chunk_memory = {}

# Biome types and visual emoji
BIOMES = {
    "plains": {
        "emoji": "🌿",
        "tiles": [(0.3, "💧"), (0.45, "🌾"), (0.65, "🌿"), (1.0, "🌳")]
    },
    "desert": {
        "emoji": "🏜️ ",
        "tiles": [(0.3, "💧"), (0.5, "⛱️"), (0.75, "🏜️ "), (1.0, "🦂")]
    },
    "forest": {
        "emoji": "🌲",
        "tiles": [(0.3, "💧"), (0.5, "🌱"), (0.7, "🌲"), (1.0, "🌳")]
    },
    "snow": {
        "emoji": "❄️ ",
        "tiles": [(0.3, "💧"), (0.5, "🌫️ "), (0.7, "❄️ "), (1.0, "☃️ ")]
    }
}

# Features
FEATURES = [
    ("🏠", 0.001),  # village
    ("🪨 ", 0.0015),  # Rock pile or ancient ruin
]

# Determine biome from noise
def get_biome(x, y):
    noise_val = pnoise2(x * BIOME_SCALE, y * BIOME_SCALE)
    norm = (noise_val + 1) / 2
    if norm < 0.25:
        return "snow"
    elif norm < 0.5:
        return "plains"
    elif norm < 0.75:
        return "forest"
    else:
        return "desert"

# Determine tile within a biome, cache in terrain_memory
def get_biome_tile(x, y):
    if (x, y) in terrain_memory:
        return terrain_memory[(x, y)]

    biome = get_biome(x, y)
    biome_data = BIOMES[biome]
    noise_val = pnoise2(x * TERRAIN_SCALE, y * TERRAIN_SCALE)
    norm = (noise_val + 1) / 2

    for threshold, tile in biome_data["tiles"]:
        if norm <= threshold:
            terrain_memory[(x, y)] = (tile, biome)
            return tile, biome

    terrain_memory[(x, y)] = (biome_data["tiles"][-1][1], biome)
    return biome_data["tiles"][-1][1], biome

# Place features based on deterministic randomness, only if tile is not water or mountain
def get_tile_with_feature(x, y):
    if (x, y) in feature_memory:
        return feature_memory[(x, y)]

    tile, biome = get_biome_tile(x, y)
    if tile in ("💧", "⛰️"):
        feature_memory[(x, y)] = tile
        return tile

    seed = (x * 928371 + y * 123457) % 999999
    random.seed(seed)
    for emoji, chance in FEATURES:
        if random.random() < chance:
            feature_memory[(x, y)] = emoji
            return emoji

    feature_memory[(x, y)] = tile
    return tile

# Get dominant biome in a chunk
def get_chunk_dominant_biome(chunk_x, chunk_y):
    if (chunk_x, chunk_y) in biome_chunk_memory:
        return biome_chunk_memory[(chunk_x, chunk_y)]

    base_x = chunk_x * CHUNK_SIZE
    base_y = chunk_y * CHUNK_SIZE
    biome_counts = Counter()

    for y in range(base_y, base_y + CHUNK_SIZE):
        for x in range(base_x, base_x + CHUNK_SIZE):
            _, biome = get_biome_tile(x, y)
            biome_counts[biome] += 1

    dominant_biome = biome_counts.most_common(1)[0][0]
    biome_chunk_memory[(chunk_x, chunk_y)] = dominant_biome
    return dominant_biome

# Draw biome map (chunk view)
def draw_biome_map(center_chunk_x, center_chunk_y, view_chunks=11):
    output = []
    half = view_chunks // 2
    for j in range(center_chunk_y - half, center_chunk_y + half + 1):
        row = ""
        for i in range(center_chunk_x - half, center_chunk_x + half + 1):
            biome = get_chunk_dominant_biome(i, j)
            emoji = BIOMES[biome]["emoji"]
            if i == center_chunk_x and j == center_chunk_y:
                row += "😄"
            else:
                row += emoji
        output.append(row)
    return "\n".join(output)

# Draw detailed tile map with features
def draw_chunk(center_x, center_y):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = ""
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            if i == center_x and j == center_y:
                row += "😄"
            else:
                row += get_tile_with_feature(i, j)
        output.append(row)
    return "\n".join(output)

# Display
if __name__ == "__main__":
    load_world_data()
    center_world_x = 225
    center_world_y = 45
    center_chunk_x = center_world_x // CHUNK_SIZE
    center_chunk_y = center_world_y // CHUNK_SIZE

    print("🗺️ Biome Overview:")
    print(draw_biome_map(center_chunk_x, center_chunk_y))

    print("\n🌍 Current Chunk View:")
    print(draw_chunk(center_world_x, center_world_y))
    save_world_data()
