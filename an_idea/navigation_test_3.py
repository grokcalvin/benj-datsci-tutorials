from navigation_test_2 import *
import time
import os
import keyboard

# --- INSERT YOUR draw_chunk() AND draw_biome_map() FUNCTIONS HERE ---

# Example placeholders (comment out these if using real functions)
# def draw_chunk(x, y): return f"Chunk View at ({x}, {y})"
# def draw_biome_map(cx, cy): return f"Biome Map centered on chunk ({cx}, {cy})"

# Player state
world_x = 0
world_y = 0
dexterity = 14  # Adjust for testing
movement_bonus = max((dexterity - 10) // 2, 0)
move_cooldown = 10 / ((10 + movement_bonus) / 10)
last_move_time = 0

# Loop settings
TICK_RATE = 1 / 20  # 20 ticks per secd
running = True

# Clear terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Game loop
def game_loop():
    global world_x, world_y, last_move_time, running

    while running:
        tick_start = time.time()

        if keyboard.is_pressed('esc'):
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
                last_move_time = now
                chunk_x = world_x // CHUNK_SIZE
                chunk_y = world_y // CHUNK_SIZE

                clear_screen()
                print("🗺️ Biome Map View:")
                print(draw_biome_map(chunk_x, chunk_y))
                print("\n🌍 Detailed Chunk View:")
                print(draw_chunk(world_x, world_y))
                print(f"\n📍 Position: ({world_x}, {world_y}) | DEX: {dexterity} | Speed: {round(move_cooldown, 2)}s")

        tick_end = time.time()
        elapsed = tick_end - tick_start
        time.sleep(max(0, TICK_RATE - elapsed))

# Run the game
clear_screen()
print("🌍 Starting map... Use W/A/S/D to move. ESC to quit.")
time.sleep(1)
game_loop()
