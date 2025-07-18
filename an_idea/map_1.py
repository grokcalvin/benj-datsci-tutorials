import random
from noise import pnoise2
from collections import Counter
from TIle_Object_test_1 import *

# Settings
CHUNK_SIZE = 31
BIOME_SCALE = 0.01
TERRAIN_SCALE = 0.1

# Biome definitions
BIOMES = {
    "plains": {
        "emoji": Tile(tile_type="plains biome", emoji="🌿"),
        "tiles": [
            (0.3, Tile(tile_type="water", emoji="💧")),
            (0.45, Tile(tile_type="tall_grass", emoji="🌾")),
            (0.65, Tile(tile_type="grass", emoji="🌿")),
            (1.0, Tile(tile_type="tree", emoji="🌳")),
        ]
    },
    "desert": {
        "emoji": Tile(tile_type="desert biome", emoji="🟨"),
        "tiles": [
            (0.3, Tile(tile_type="oasis", emoji="💧")),
            (0.5, Tile(tile_type="shade_umbrella", emoji="⛱️ ")),
            (0.75, Tile(tile_type="sand", emoji="🟨")),
            (1.0, Tile(tile_type="scorpion", emoji="🦂")),
        ]
    },
    "forest": {
        "emoji": Tile(tile_type="forest biome", emoji="🌲"),
        "tiles": [
            (0.3, Tile(tile_type="water", emoji="💧")),
            (0.5, Tile(tile_type="seedling", emoji="🌱")),
            (0.7, Tile(tile_type="pine_tree", emoji="🌲")),
            (1.0, Tile(tile_type="tree", emoji="🌳")),
        ]
    },
    "snow": {
        "emoji": Tile(tile_type="snow biome", emoji="❄️ "),
        "tiles": [
            (0.3, Tile(tile_type="ice_water", emoji="💧")),
            (0.5, Tile(tile_type="fog", emoji="🌫️ ")),
            (0.7, Tile(tile_type="snow", emoji="❄️ ")),
            (1.0, Tile(tile_type="snowman", emoji="☃️ ")),
        ]
    }
}

FEATURE_CHANCES = {
    Tile(tile_type="village",emoji="🏠"): 0.0003,
    Tile(tile_type="cave",emoji="🪨 "): 0.0007  
}

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

def get_biome_for_chunk_w_terrain_render(chunk_x, chunk_y, SaveFile, chunk_size=31):
    #will need to pass in the save data, and pass out to save on the outside
    if (chunk_x, chunk_y) in SaveFile.biome_memory:
        return SaveFile.biome_memory[(chunk_x, chunk_y)]
    base_x, base_y = chunk_x * chunk_size, chunk_y * chunk_size
    biome_counts = Counter()
    for y in range(base_y, base_y + chunk_size):
        for x in range(base_x, base_x + chunk_size):
            biome = get_biome(x, y)
            biome_counts[biome] += 1

    dominant = biome_counts.most_common(1)[0][0]
    SaveFile.biome_memory[(chunk_x, chunk_y)] = BIOMES[dominant]["emoji"]

    for y in range(base_y, base_y + chunk_size):
        for x in range(base_x, base_x + chunk_size):
            biome = get_biome(x, y)
            tile = get_biome_tile(x, y, biome)
            SaveFile.biome_memory[(chunk_x, chunk_y)].tile_block[(x, y)] = tile

            # Add feature only on non-water/mountain tiles
            if tile.emoji not in ["💧", "☃️ ", "🦂 "]:
                for feature, chance in FEATURE_CHANCES.items():
                    if random.random() < chance:
                        SaveFile.biome_memory[(chunk_x, chunk_y)].tile_block[(x, y)] = feature
                        break  # only one feature per tile

    return SaveFile.biome_memory[(chunk_x, chunk_y)]

def get_terrain_tile(x, y, SaveFile, chunk_size = 31):
    x_biome, y_biome = x//chunk_size, y//chunk_size
    if (x_biome, y_biome) not in SaveFile.biome_memory:

        get_biome_for_chunk_w_terrain_render(x_biome, y_biome, SaveFile)



    return SaveFile.biome_memory[(x_biome, y_biome)].tile_block.get((x, y)) # dont need to return memory bank because it follows up the chain

# Modified get_chunk_dominant_biome with memory

def get_biome_tiles(center_chunk_x, center_chunk_y, SaveFile, view_chunks=11):
    output = []
    half = view_chunks // 2
    for j in range(center_chunk_y - half, center_chunk_y + half + 1):
        row = []
        for i in range(center_chunk_x - half, center_chunk_x + half + 1):
            biome_tile = get_biome_for_chunk_w_terrain_render(i, j, SaveFile=SaveFile)
            row.append(biome_tile)
        output.append(row)
    return output

def tile_block_insert_center_player(tile_block,player=Tile(tile_type="player icon",emoji="😄")):
    center_x = len(tile_block) //2
    center_y = len(tile_block[0]) //2
    tile_block[center_x][center_y] = player
    return tile_block

def draw_tile_block(tile_block):
    output = ""
    for j in range(len(tile_block)):
        row = ""
        for i in range(len(tile_block[j])):
            emoji = tile_block[j][i].emoji
            row += emoji
        output += "\n"+row
    return output


def get_terrain_tile_block(center_x, center_y, SaveFile):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = []
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            row.append(get_terrain_tile(i, j, SaveFile))
        output.append(row)
    return output

# Load memory and run display
if __name__ == "__main__":
        pass