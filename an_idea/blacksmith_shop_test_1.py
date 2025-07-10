import noise
import random

# Weapon and material pools
WEAPONS = ["Dagger", "Shortsword", "Longsword", "Warhammer", "Axe", "Spear", "Mace"]
MATERIALS = ["Wood","Bronze", "Iron", "Steel", "Obsidian", "Mithril"]

# Settings
STOCK_SIZE = 1
WEAPON_SCALE = 0.5
MATERIAL_SCALE = 0.8

def select_from_noise(x, y, options, scale, octaves=2):
    val = noise.pnoise2(x * scale, y * scale, octaves=octaves)
    norm_val = val + 0.5
    index = int(norm_val * len(options))
    return options[min(index, len(options)-1)]

def generate_random_shop_inventory(count):
    # Random offset (changes every run)
    offset_x = random.uniform(0, 1000)
    offset_y = random.uniform(0, 1000)

    inventory = []
    attempts = 0
    max_attempts = 100

    while len(inventory) < count and attempts < max_attempts:
        dx = random.uniform(-1.0, 1.0)
        dy = random.uniform(-1.0, 1.0)

        wx = offset_x + dx
        wy = offset_y + dy

        weapon = select_from_noise(wx, wy, WEAPONS, WEAPON_SCALE)
        material = select_from_noise(wx + 100, wy + 100, MATERIALS, MATERIAL_SCALE)
        item = f"{material} {weapon}"

        inventory.append(item)
        attempts += 1

    return list(inventory)

# Generate and show shop inventory
inventory = generate_random_shop_inventory(STOCK_SIZE)

print("🛠️  Blacksmith’s Inventory:")
for item in inventory:
    print(f"• {item}")