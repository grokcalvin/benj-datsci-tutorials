# Updated version that stores Tile objects with emoji + name instead of just emoji characters

import pickle
import os
from TIle_Object_test_1 import *
from village_test_4 import *

CANVAS_FILE = "emoji_canvas.pkl"

# Memory
emoji_canvas = {}

# Tile class to represent each tile with emoji and name
class Tile:
    def __init__(self, name, emoji):
        self.name = name
        self.emoji = emoji

    def __repr__(self):
        return f"Tile({self.name!r}, {self.emoji!r})"

# Save and load canvas
def save_canvas():
    with open(CANVAS_FILE, 'wb') as f:
        pickle.dump(emoji_canvas, f)

def load_canvas():
    global emoji_canvas
    if os.path.exists(CANVAS_FILE):
        with open(CANVAS_FILE, 'rb') as f:
            emoji_canvas = pickle.load(f)

# Paste text block as Tile objects into the canvas
def paste_to_canvas(object_block, start_x, start_y):
    for j, row in enumerate(object_block):
        for i, tile in enumerate(row):
            if isinstance(tile, Tile):  # ensure it's a valid Tile
                emoji_canvas[(start_x + i, start_y + j)] = tile

# Draw a canvas region centered on player
def draw_canvas(center_x, center_y, size=31, background_tile="🌲"):
    output = []
    half = size // 2
    for y in range(center_y - half, center_y + half + 1):
        row = ''
        for x in range(center_x - half, center_x + half + 1):
            if (x, y) == (center_x, center_y):
                row += '😄'
            else:
                tile = emoji_canvas.get((x, y))
                if isinstance(tile, Tile):
                    row += tile.emoji
                else:
                    row += str(tile)
        output.append(row)
    return "\n".join(output)

# Run example
load_canvas()

text = """
🌲🌲🌲🌲🌲
🌲🏠🏠🌲🌲
🌲🏠⛲🏠🌲
🌲🏠🏠🌲🌲
🌲🌲🌲🌲🌲
"""
if __name__ == "__main__":
    village = get_or_generate_village(1,1)
    paste_to_canvas(village, 100, 100)
    save_canvas()
    draw_canvas(102, 102)
