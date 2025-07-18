import random
import os
import pickle
from noise import pnoise2
from collections import Counter

# Settings
CHUNK_SIZE = 31
BIOME_SCALE = 0.01
TERRAIN_SCALE = 0.1
FEATURE_CHANCE = 0.03
SAVE_FILE = "terrain_memory.pkl"

# Memory containers
tile_memory = {}
feature_memory = {}
# New memory container for dominant biome per chunk
chunk_biome_memory = {}

# Biome definitions
BIOMES = {
    "plains": {"emoji": "🌿", "tiles": [(0.3, "💧"), (0.45, "🌾"), (0.65, "🌿"), (1.0, "🌳")]},
    "desert": {"emoji": "🟨", "tiles": [(0.3, "💧"), (0.5, "⛱️"), (0.75, "🟨"), (1.0, "🦂")]},
    "forest": {"emoji": "🌲", "tiles": [(0.3, "💧"), (0.5, "🌱"), (0.7, "🌲"), (1.0, "🌳")]},
    "snow": {"emoji": "❄️ ", "tiles": [(0.3, "💧"), (0.5, "🌫️ "), (0.7, "❄️ "), (1.0, "☃️ ")]}
}

FEATURE_CHANCES = {
    "🏠": 0.0003,
    "🪨 ": 0.0007  
}

# Update save/load to include this
def load_memory():
    global tile_memory, feature_memory, chunk_biome_memory
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "rb") as f:
            data = pickle.load(f)
            tile_memory = data.get("tiles", {})
            feature_memory = data.get("features", {})
            chunk_biome_memory = data.get("chunk_biomes", {})

def save_memory():
    with open(SAVE_FILE, "wb") as f:
        pickle.dump({
            "tiles": tile_memory,
            "features": feature_memory,
            "chunk_biomes": chunk_biome_memory
        }, f)

def get_biome(x, y):
    norm = (pnoise2(x * BIOME_SCALE, y * BIOME_SCALE) + 1) / 2
    if norm < 0.25: return "snow"
    elif norm < 0.5: return "plains"
    elif norm < 0.75: return "forest"
    return "desert"

def get_biome_tile(x, y, biome_name):
    norm = (pnoise2(x * TERRAIN_SCALE, y * TERRAIN_SCALE) + 1) / 2
    for threshold, tile in BIOMES[biome_name]["tiles"]:
        if norm <= threshold:
            return tile
    return BIOMES[biome_name]["tiles"][-1][1]

def generate_chunk_data(chunk_x, chunk_y):
    base_x, base_y = chunk_x * CHUNK_SIZE, chunk_y * CHUNK_SIZE
    biome_counts = Counter()
    for y in range(base_y, base_y + CHUNK_SIZE):
        for x in range(base_x, base_x + CHUNK_SIZE):
            biome = get_biome(x, y)
            biome_counts[biome] += 1
            tile = get_biome_tile(x, y, biome)
            tile_memory[(x, y)] = tile

            # Add feature only on non-water/mountain tiles
            if tile not in ["💧", "☃️", "🦂"]:
                for feature, chance in FEATURE_CHANCES.items():
                    if random.random() < chance:
                        feature_memory[(x, y)] = feature
                        break  # only one feature per tile
    return biome_counts.most_common(1)[0][0]

def get_tile(x, y):
    if (x, y) not in tile_memory:
        generate_chunk_data(x // CHUNK_SIZE, y // CHUNK_SIZE)
        save_memory()
    return feature_memory.get((x, y), tile_memory.get((x, y), "⬛"))

# Modified get_chunk_dominant_biome with memory
def get_chunk_dominant_biome(chunk_x, chunk_y):
    if (chunk_x, chunk_y) in chunk_biome_memory:
        return chunk_biome_memory[(chunk_x, chunk_y)]

    base_x = chunk_x * CHUNK_SIZE
    base_y = chunk_y * CHUNK_SIZE
    biome_counts = Counter()

    for y in range(base_y, base_y + CHUNK_SIZE):
        for x in range(base_x, base_x + CHUNK_SIZE):
            biome = get_biome(x, y)
            biome_counts[biome] += 1
            tile = get_biome_tile(x, y, biome)
            tile_memory[(x, y)] = tile

            if tile not in ["💧", "☃️", "🦂"]:
                for feature, chance in FEATURE_CHANCES.items():
                    if random.random() < chance:
                        feature_memory[(x, y)] = feature
                        break

    dominant = biome_counts.most_common(1)[0][0]
    chunk_biome_memory[(chunk_x, chunk_y)] = dominant
    save_memory()
    return dominant

def draw_biome_map(center_chunk_x, center_chunk_y, view_chunks=11):
    output = []
    half = view_chunks // 2
    for j in range(center_chunk_y - half, center_chunk_y + half + 1):
        row = ""
        for i in range(center_chunk_x - half, center_chunk_x + half + 1):
            biome = get_chunk_dominant_biome(i, j)
            emoji = BIOMES[biome]["emoji"]
            row += "😄" if i == center_chunk_x and j == center_chunk_y else emoji
        output.append(row)
    return "\n".join(output)

def draw_chunk(center_x, center_y):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = ""
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            row += "😄" if i == center_x and j == center_y else get_tile(i, j)
        output.append(row)
    return "\n".join(output)

# Load memory and run display
if __name__ == "__main__":

    load_memory()
    center_world_x = 770
    center_world_y =-720
    center_chunk_x = center_world_x // CHUNK_SIZE
    center_chunk_y = center_world_y // CHUNK_SIZE

    print("🗺️ Biome Overview:")
    print(draw_biome_map(center_chunk_x, center_chunk_y))

    print("\n🌍 Current Chunk View:")
    print(draw_chunk(center_world_x, center_world_y))
    save_memory()