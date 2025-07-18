import random
from TIle_Object_test_1 import *

# Cave generation settings
CHUNK_SIZE = 31
CAVE_SCALE = 0.08
CAVE_THRESHOLD = 0.1

# Emoji tiles
TILE_WALL = Tile(tile_type="cave wall", emoji="⬛")
TILE_CAVE = Tile(tile_type="open cave", emoji="⬜")
TILE_COAL = Tile(tile_type="coal", emoji="⚫")
TILE_IRON = Tile(tile_type="iron", emoji="🪨 ")
TILE_CRYSTAL = Tile(tile_type="crystal", emoji="🔷")
TILE_MUSHROOM = Tile(tile_type="mushroom", emoji="🍄")
TILE_WATER = Tile(tile_type="underground water", emoji="💧")
TILE_PLAYER = Tile(tile_type="player", emoji="😄")

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



def get_cave_chunk_w_cave_terrain_render(chunk_x, chunk_y, SaveFile, chunk_size=31):
    #will need to pass in the save data, and pass out to save on the outside
    if (chunk_x, chunk_y) in SaveFile.cave_chunk_memory:
        return SaveFile.cave_chunk_memory[(chunk_x, chunk_y)]
    else:
        SaveFile.cave_chunk_memory[(chunk_x, chunk_y)] = Tile(tile_type="cave chunk",emoji="⬛")

    base_x, base_y = chunk_x * chunk_size, chunk_y * chunk_size
    for y in range(base_y, base_y + chunk_size):
        for x in range(base_x, base_x + chunk_size):
            if is_cave(x, y):
                tile = TILE_CAVE
                for feature, chance in FEATURES:
                    if random.random() < chance:
                        tile = feature
                        break  # only one feature per tile
            else:
                tile = TILE_WALL
            SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(x, y)] = tile
    return SaveFile.cave_chunk_memory[(chunk_x, chunk_y)]



def get_cave_tile(x, y, SaveFile, chunk_size = 31):
    x_chunk, y_chunk = x//chunk_size, y//chunk_size
    if (x_chunk, y_chunk) not in SaveFile.cave_chunk_memory:
        
        get_cave_chunk_w_cave_terrain_render(x_chunk, y_chunk, SaveFile)



    return SaveFile.cave_chunk_memory[(x_chunk, y_chunk)].tile_block.get((x, y)) # dont need to return memory bank because it follows up the chain



# Infinite cave map generator centered on (center_x, center_y)
def get_cave_tile_block(center_x, center_y, SaveFile):
    output = []
    for j in range(center_y - CHUNK_SIZE // 2, center_y + CHUNK_SIZE // 2):
        row = []
        for i in range(center_x - CHUNK_SIZE // 2, center_x + CHUNK_SIZE // 2):
            row.append(get_cave_tile(i, j, SaveFile))
        output.append(row)
    return output

#find nearest cave tile:
def find_nearest_cave_tile_recursive(x, y, SaveFile, max_depth=62, visited=None):
    if visited is None:
        visited = set()

    # Avoid rechecking the same tile
    if (x, y) in visited:
        return None
    visited.add((x, y))

    # Base case — tile is a cave
    tile = get_cave_tile(x,y, SaveFile=SaveFile)
    if tile == TILE_CAVE:
        return x, y

    # Prevent infinite depth
    if len(visited) > max_depth ** 2:
        return None

    # Explore outward (N, S, E, W)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        result = find_nearest_cave_tile_recursive(x + dx, y + dy, SaveFile, max_depth, visited)
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
