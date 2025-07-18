import keyboard
import time
from village_test_4 import *
import os
from memory_test_2 import *
from paste_and_render_test_1 import *
from map_features_and_memory_test_3 import *

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def in_bounds(x, y,corner_boundary_x,corner_boundary_y,x_size,y_size):
    return corner_boundary_x <= x < x_size+corner_boundary_x and corner_boundary_y <= y < y_size+corner_boundary_y

def enter_set_area(entry_x, entry_y, tile_block, dexterity=10, on_entry_words=" You enter the placeholder name", display_name="Welcome to placeholder name",background_tile = Tile(tile_type="background",emoji="🌲")):
    # Place ladder where the player entered
    #entry needs to be calcualated before ad put in here --------------------jsadoi

    boundary_x = len(tile_block)
    boundary_y = len(tile_block[0])

    # Find valid cave tile
    player_x,player_y = entry_x,entry_y
    last_x, last_y = player_x, player_y

    # Calculate movement speed
    movement_bonus = max((dexterity - 10) // 2, 0)
    move_cooldown = (10 / ((10 + movement_bonus) / 10)/20)
    last_move_time = 0

    NO_TRAVEL_TILES = ["💧"]

    print({on_entry_words})
    time.sleep(3)

    clear_screen()
    paste_to_canvas(tile_block, entry_x, entry_y)
    tile_canvas = draw_tile_canvas(center_x=player_x, center_y=player_y, size=31,background_tile=background_tile)
    tile_canvas_w_player = insert_player_to_tile_block(tile_canvas)
    display_tiles = draw_from_tile_list(tile_canvas_w_player)
    print(display_name)
    print(display_tiles)
    while True:
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
                tile = get_tile_with_memory(player_x, player_y)

                if not in_bounds(x=player_x, y=player_y,corner_boundary_x=entry_x,corner_boundary_y=entry_y,x_size=boundary_x,y_size=boundary_y):
                    print("out of bouce")
                    return tile_block
                    
                    # return tile block then save using the same corrdinates you used to generate or recall it after. It should when you call the eneter village modudal.

                if tile in NO_TRAVEL_TILES:
                    # Revert to last position
                    player_x, player_y = last_x, last_y
                else:
                    last_x, last_y = player_x, player_y
                    last_move_time = now

                clear_screen()
                paste_to_canvas(tile_block, entry_x, entry_y)
                tile_canvas = draw_tile_canvas(center_x=player_x, center_y=player_y, size=31,background_tile=background_tile)
                tile_canvas_w_player = insert_player_to_tile_block(tile_canvas)
                display_tiles = draw_from_tile_list(tile_canvas_w_player)
                print(display_name)
           



                print(display_tiles)
                print(f"\n⛏️ Position: ({player_x}, {player_y}) | DEX: {dexterity} | Speed: {round(move_cooldown, 2)}")

        # Return to surface
        if keyboard.is_pressed("enter"):
            if get_tile_with_memory(player_x, player_y) == "🪜":
                print("🪜 You climb the ladder and return to the surface.")
                save_tile_memory()
            elif get_tile_with_memory(player_x,player_y) == TILE_COAL:
                tile_memory[(player_x, player_y)] = TILE_CAVE
                pass
            elif get_tile_with_memory(player_x,player_y) == TILE_IRON:
                tile_memory[(player_x, player_y)] = TILE_CAVE
                pass
            elif get_tile_with_memory(player_x,player_y) == TILE_CRYSTAL:
                tile_memory[(player_x, player_y)] = TILE_CAVE
                pass
            elif get_tile_with_memory(player_x,player_y) == TILE_MUSHROOM:
                tile_memory[(player_x, player_y)] = TILE_CAVE
                pass

        elapsed = time.time() - tick_start
        time.sleep(max(0, 1 / 20 - elapsed))

if __name__ == "__main__":
    player_x = 1
    player_y = 1
    tile_block = get_or_generate_village(player_x, player_y)

    biome_emoiji = get_biome(player_x,player_y)
    biome_emoiji = BIOMES[biome_emoiji]["emoji"]

    background_tile =  Tile(tile_type="background",emoji=biome_emoiji)
    enter_set_area(entry_x=player_x*31, entry_y=player_y*31, tile_block=tile_block, dexterity=10, display_name="Welcome to placeholder name",background_tile = background_tile )
    #save all tiles to dict then use the tile block to cross reference and save the data?