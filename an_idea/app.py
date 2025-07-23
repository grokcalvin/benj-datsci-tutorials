from map_1 import *
import time
import os
import keyboard
from enter_cave_1 import *
from play_within_area_test_1 import *
from character_2 import *
from effect_and_skill_functions import *
# --- INSERT YOUR draw_chunk() AND draw_biome_map() FUNCTIONS HERE ---

# Example placeholders (comment out these if using real functions)
# def draw_chunk(x, y): return f"Chunk View at ({x}, {y})"
# def draw_biome_map(cx, cy): return f"Biome Map centered on chunk ({cx}, {cy})"

# Player state

class SaveFile:
    def __init__(self):
        # Core game state
        self.tile_memory = {}
        self.feature_memory = {}
        self.biome_memory = {}
        self.cave_chunk_memory = {}
        self.player_state = {
            "x": 0,
            "y": 0
        }
        self.structures = {}  # e.g., village/shop state
        self.filename = "defualt"
        self.player = Character("Banjo")
        self.player.dexterity = 100

def save(SaveFile):
    with open(SaveFile.filename, "wb") as f:
        pickle.dump(SaveFile, f)

def load(filename="default.pkl"):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)
    else:
        print("⚠️ No save file found. Creating a new one.")
        return SaveFile()

game_save = SaveFile()

world_x = 0
world_y = 0
dexterity = 100  # Adjust for testing
movement_bonus = max((dexterity - 10) // 2, 0)
move_cooldown = 10 / ((10 + movement_bonus) / 10)
last_move_time = 0

#save game:
# Memory containers
# New memory container for dominant biome per chunk

# Loop settings
TICK_RATE = 1 / 20  # 20 ticks per secd
running = True

# Clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_structure(tile, x, y, SaveFile, chunk_size=31):
    if tile.emoji == "🏠" or tile.emoji =="⛺":
        biome_x, biome_y = x//chunk_size, y//chunk_size
        tile_block = get_or_generate_village(x, y)

        #this places dict with list fix later <-------------------------------------------------------------------================================
        SaveFile.biome_memory[(biome_x, biome_y)].tile_block[(x,y)].tileblock = tile_block

        biome_emoiji = get_biome(x,y)
        biome_emoiji = BIOMES[biome_emoiji]["emoji"]
        background_tile =  Tile(tile_type="background",emoji=biome_emoiji)

        enter_set_area(entry_x=x*31, entry_y=y*31, tile_block=tile_block, dexterity=dexterity, display_name="The Village",background_tile = background_tile )
    if tile.emoji == "🪨 ":
        print("CAVE")
        time.sleep(3)
        enter_cave(x*31,y*31, SaveFile=SaveFile, dexterity=dexterity)
        time.sleep(5)

# Game loop
def game_loop(game_save=game_save):
    global world_x, world_y, last_move_time, running
    last_x, last_y = world_x, world_y

    while running:
        tick_start = time.time()

        if keyboard.is_pressed('esc'):
            save(game_save)
            running = False
            break

        now = time.time()
        if now - last_move_time >= move_cooldown/20:
            moved = False
            if keyboard.is_pressed('w'):
                world_y -= 1
                moved = True
            elif keyboard.is_pressed('s'):
                world_y += 1
                moved = True
            elif keyboard.is_pressed('a'):
                world_x -= 1
                moved = True
            elif keyboard.is_pressed('d'):
                world_x += 1
                moved = True

            if moved:
                current_tile = get_terrain_tile(world_x, world_y, game_save)

                # If stepped on invalid terrain, revert to last position
                if current_tile.emoji in ["💧", "☃️", "🦂"]:  # Add more if needed
                    world_x, world_y = last_x, last_y
                else:
                    last_x, last_y = world_x, world_y  # Update only if move is valid

                last_move_time = now
                chunk_x = world_x // CHUNK_SIZE
                chunk_y = world_y // CHUNK_SIZE

                #clear_screen()
                print("🗺️ Biome Overview:")
                biome_tile_block = get_biome_tiles(chunk_x, chunk_y, game_save)
                biome_tile_block_w_player = tile_block_insert_center_player(tile_block=biome_tile_block)
                print(draw_tile_block(biome_tile_block_w_player))

                print("\n🌍 Detailed Terrain View:")
                terrain_tile_block = get_terrain_tile_block(world_x,world_y, game_save)
                terrain_tile_block_w_player = tile_block_insert_center_player(tile_block=terrain_tile_block)
                print(draw_tile_block(terrain_tile_block_w_player))

                print(f"\n📍 Position: ({world_x}, {world_y}) | DEX: {dexterity} | Speed: {round(move_cooldown, 2)}s")   

        # Enter structure if player presses Enter
        if keyboard.is_pressed('enter'):
            current_tile = get_terrain_tile(world_x, world_y, game_save)
            if current_tile.emoji in ['🏠', '🪨 ']:  # Add other interactable tiles here
                enter_structure(current_tile, world_x, world_y, SaveFile=game_save)
                #clear_screen()
                print("🗺️ Biome Overview:")
                tile_block = get_biome_tiles(chunk_x, chunk_y, game_save)
                tile_block = tile_block_insert_center_player(tile_block=tile_block)
                print(draw_tile_block(tile_block))

                print("\n🌍 Detailed Terrain View:")
                tile_block = get_terrain_tile_block(world_x,world_y, game_save)
                tile_block = tile_block_insert_center_player(tile_block=tile_block)
                print(draw_tile_block(tile_block))

                print(f"\n📍 Position: ({world_x}, {world_y}) | DEX: {dexterity} | Speed: {round(move_cooldown, 2)}s")


        tick_end = time.time()
        elapsed = tick_end - tick_start
        time.sleep(max(0, TICK_RATE - elapsed))

# Run the game
if __name__ == "__main__":
    clear_screen()
    filename = input("Enter filename to load (leave blank for 'default'): ").strip()
    if not filename:
        filename = "default.pkl"
    elif not filename.endswith(".pkl"):
        filename += ".pkl"

    save_file = load(filename)
    save_file.filename = filename  # Ensure SaveFile object knows its filename

    print("🌍 Starting map... Use W/A/S/D to move. ESC to quit.")
    time.sleep(1)
    game_loop(save_file)