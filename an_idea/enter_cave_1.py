import keyboard
import time
from cave_4 import *
import os
from TIle_Object_test_1 import *
from map_1 import *
from mining_resources_3 import *


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

entrance = Tile(tile_type="cave exit",emoji="🪜 ")

def enter_cave(entry_x, entry_y, SaveFile, chunk_size=31, dexterity=10):
    # Place ladder where the player entered
    chunk_x, chunk_y = entry_x // chunk_size, entry_y // chunk_size
    # Find valid cave tile
    player_x, player_y = find_nearest_cave_tile_recursive(entry_x, entry_y, SaveFile=SaveFile)
    SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(player_x, player_y)] = entrance             
    last_x, last_y = player_x, player_y

    # Calculate movement speed
    movement_bonus = max((dexterity - 10) // 2, 0)
    move_cooldown = (10 / ((10 + movement_bonus) / 10)/20)
    last_move_time = 0

    NO_TRAVEL_TILES = ["⬛","💧"]

    in_cave = True
    print("🕳️ You descend into the cave...")
    time.sleep(3)
    while in_cave:
        tick_start = time.time()
        now = time.time()

        if now - last_move_time >= move_cooldown:
            moved = False

            if keyboard.is_pressed('w'):
                player_y -= 1
                moved = True
            elif keyboard.is_pressed('s'):
                player_y += 1
                moved = True
            elif keyboard.is_pressed('a'):
                player_x -= 1
                moved = True
            elif keyboard.is_pressed('d'):
                player_x += 1
                moved = True

            if moved:
                chunk_x, chunk_y = player_x // chunk_size, player_y // chunk_size
                tile = get_cave_tile(player_x, player_y, SaveFile=SaveFile)

                if tile.emoji in NO_TRAVEL_TILES:
                    # Revert to last position
                    player_x, player_y = last_x, last_y
                else:
                    last_x, last_y = player_x, player_y
                    last_move_time = now

                clear_screen()
                print("🕳️ Cave Interior")
                cave_tile_block = get_cave_tile_block(player_x, player_y, SaveFile)
                cave_tile_block_w_player = tile_block_insert_center_player(tile_block=cave_tile_block)
                print(draw_tile_block(cave_tile_block_w_player))
                print(f"\n⛏️ Position: ({player_x}, {player_y}) | DEX: {dexterity} | Speed: {round(move_cooldown, 2)}s")

        # Return to surface
        if keyboard.is_pressed("enter"):
            if get_cave_tile(player_x, player_y, SaveFile=SaveFile) == entrance:
                print("🪜 You climb the ladder and return to the surface.")
                in_cave = False
            # test if in ____ then loop through so you can easily add new ores later.
            elif get_cave_tile(player_x, player_y, SaveFile=SaveFile) == TILE_COAL:
                perform_mining(SaveFile.player, TILE_COAL.emoji)
                SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(player_x, player_y)] = TILE_CAVE             
    
            elif get_cave_tile(player_x, player_y, SaveFile=SaveFile) == TILE_IRON:
                perform_mining(SaveFile.player, TILE_IRON.emoji)
                SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(player_x, player_y)] = TILE_CAVE             
            
            elif get_cave_tile(player_x, player_y, SaveFile=SaveFile) == TILE_CRYSTAL:
                perform_mining(SaveFile.player, TILE_CRYSTAL.emoji)
                SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(player_x, player_y)] = TILE_CAVE             
            
            elif get_cave_tile(player_x, player_y, SaveFile=SaveFile) == TILE_MUSHROOM:
                perform_mining(SaveFile.player, TILE_MUSHROOM.emoji)
                SaveFile.cave_chunk_memory[(chunk_x, chunk_y)].tile_block[(player_x, player_y)] = TILE_CAVE             
        elapsed = time.time() - tick_start
        time.sleep(max(0, 1 / 20 - elapsed))

if __name__ == "__main__":
    center_x = 0
    center_y = 0
    player_input = ""
    player_x, player_y = find_nearest_cave_tile_recursive(center_x, center_y)
    enter_cave(player_x,player_y,100)