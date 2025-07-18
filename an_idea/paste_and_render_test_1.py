from TIle_Object_test_1 import *
from village_test_4 import *
from copy import copy
# Let's define a function that allows "pasting" a block of text into an infinite emoji map grid.
# This module can be imported and used in your other code files.

# Canvas memory
paste_canvas = {}

# Paste block of emoji text into canvas at (start_x, start_y)
def paste_to_canvas(tile_block, start_x, start_y):
    #get list
    for j, line in enumerate(tile_block):
        for i, tile in enumerate(line):
            paste_canvas[(start_x + i, start_y + j)] = tile  #for every tile
#you get locations and values, I want tile array

# Render a region around a center point (31x31)
def draw_tile_canvas(center_x, center_y, size=31,background_tile=Tile(tile_type="background",emoji="🌲")):
    output = []
    half = size // 2
    for y in range(center_y - half, center_y + half + 1):
        row = []
        for x in range(center_x - half, center_x + half + 1):
            #if (x, y) == (center_x, center_y):
            #    row += '😄'
            try:
                if paste_canvas[(x, y)] != None:
                    row.append(paste_canvas[(x, y)])
            except:
                row.append(background_tile)
        output.append(row)
    return output

def draw_from_tile_list(tile_list):
    full_emoji_canvas = ""
    for row in tile_list:
        new_line = ""
        for tile in row:
            new_line += tile.emoji
        full_emoji_canvas += new_line + "\n"
    return full_emoji_canvas

def in_bounds(x, y,corner_boundary_x,corner_boundary_y,x_size,y_size):
    return corner_boundary_x <= x < x_size+corner_boundary_x and corner_boundary_y <= y < y_size+corner_boundary_y

def insert_player_to_tile_block(tileblock):
    new_tile_block = copy(tileblock)
    half_x = len(tileblock) // 2
    half_y = len(tileblock[0]) //2
    new_tile_block[half_x][half_y] = Tile(tile_type="player",emoji="😄")
    return new_tile_block

# Example of how it might be used
if __name__ == "__main__":
    x = 4
    y = 5
    corner_bounary_x = 0
    corner_boundary_y = 0
    print(in_bounds(x,y,corner_bounary_x,corner_boundary_y,5,5))



    village_of_tiles = get_or_generate_village(0,0)
    paste_to_canvas(village_of_tiles, 0, 0 )
#    save_canvas()
    tile_list = draw_tile_canvas(20, 20)
    print(draw_from_tile_list(tile_list))