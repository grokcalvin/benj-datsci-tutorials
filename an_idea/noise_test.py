import noise
import random

width = 40
height = 20
scale = 0.1  # Adjust to zoom in/out

terrain = [
    "🌊",  # water
    "🌴",  # beac
    "🌾",  # plains
    "🌲",  # forest
    "⛰️",  # mountains
]

def get_emoji(value):
    index = int(value * len(terrain))
    if index == len(terrain):
        index -= 1
    return terrain[index]

for y in range(height):
    row = ""
    for x in range(width):
        val = noise.pnoise2(x * scale, y * scale, octaves=6)
        norm_val = (val + 0.5)  # Normalize from ~[-0.5, 0.5] → [0, 1]
        emoji = get_emoji(norm_val)
        row += emoji
    print(row)