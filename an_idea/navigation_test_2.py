from noise import pnoise2
from collections import Counter

# Settings
CHUNK_SIZE = 31
BIOME_SCALE = 0.01
TERRAIN_SCALE = 0.1

# Biome types and visual emoji
BIOMES = {
    "plains": {
        "emoji": "🌿",
        "tiles": [(0.3, "💧"), (0.45, "🌾"), (0.65, "🌿"), (1.0, "🌳")]
    },
    "desert": {
        "emoji": "🏜️ ",
        "tiles": [(0.3, "💧"), (0.5, "⛱️ "), (0.75, "🏜️ "), (1.0, "🦂")]
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

# Get biome at a specific coordinate using Perlin noise
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

# Get terrain tile within biome using smaller-scale noise
def get_biome_tile(x, y, biome_name):
    biome = BIOMES[biome_name]
    noise_val = pnoise2(x * TERRAIN_SCALE, y * TERRAIN_SCALE)
    norm = (noise_val + 1) / 2
    for threshold, tile in biome["tiles"]:
        if norm <= threshold:
            return tile
    return biome["tiles"][-1][1]

# Get dominant biome in a specific chunk
def get_chunk_dominant_biome(chunk_x, chunk_y):
    base_x = chunk_x * CHUNK_SIZE
    base_y = chunk_y * CHUNK_SIZE
    biome_counts = Counter()

    for y in range(base_y, base_y + CHUNK_SIZE):
        for x in range(base_x, base_x + CHUNK_SIZE):
            biome = get_biome(x, y)
            biome_counts[biome] += 1

    dominant_biome = biome_counts.most_common(1)[0][0]
    return dominant_biome

# Draw the biome map (each tile is one chunk)
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

# Draw the current chunk's tile map (terrain detail)
def draw_chunk(center_x, center_y):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = ""
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            if i == center_x and j == center_y:
                row += "😄"
            else:
                biome = get_biome(i, j)
                tile = get_biome_tile(i, j, biome)
                row += tile
        output.append(row)
    return "\n".join(output)

# Example usage
if __name__== "__main__":
    center_world_x = 225
    center_world_y = 45
    center_chunk_x = center_world_x // CHUNK_SIZE
    center_chunk_y = center_world_y // CHUNK_SIZE

# Biome map around player (emoji map, one emoji per chunk)
    print("🗺️ Biome Overview:")
    print(draw_biome_map(center_chunk_x, center_chunk_y))

# Detailed view of the chunk player is in
    print("\n🌍 Current Chunk View:")
    print(draw_chunk(center_world_x, center_world_y))
