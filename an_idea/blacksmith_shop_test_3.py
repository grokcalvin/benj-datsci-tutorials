import noise
import math
import random

# Configurations
BLACKSMITH_SKILL = 5        # 0–20
SHOP_SIZE = 10
WEAPON_SCALE = 0.3
MATERIAL_SCALE = 0.4
NOISE_SEED = random.uniform(0, 1000)  # new seed per run

# Weapon and material pools
WEAPONS = ["Dagger", "Shortsword", "Longsword", "Warhammer", "Axe", "Spear", "Mace"]
MATERIALS = ["Bronze", "Iron", "Steel", "Obsidian", "Mithril"]
QUALITY_TIERS = ["Awful", "Poor", "Normal", "Good", "Excellent", "Masterwork", "Legendary"]

# Sigmoid + quality logic
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def get_quality(skill_level, curve=2.5, strength=6, midpoint=5, power=1.5):
    skill = max(0, min(skill_level, 20))
    if skill <= midpoint:
        x = (skill - midpoint) / (midpoint - 0)
    else:
        x = (skill - midpoint) / (20 - midpoint) / 3  # soft reward curve
    shift = x * strength

    r = random.random() ** power  # biased toward center
    val = (r - 0.5) * curve + shift
    s = sigmoid(val)

    thresholds = [0.14, 0.28, 0.5, 0.68, 0.82, 0.96, 0.98]
    for i, threshold in enumerate(thresholds):
        if s <= threshold:
            return QUALITY_TIERS[i]
    return QUALITY_TIERS[-1]

# 2D noise-based selection
def select_from_noise(x, y, options, scale, octaves=2):
    val = noise.pnoise2(x * scale, y * scale, octaves=octaves)
    norm_val = val + 0.5  # [-0.5, 0.5] → [0, 1]
    index = int(norm_val * len(options))
    return options[min(index, len(options) - 1)]

# Main shop generation
def generate_blacksmith_inventory(size, skill_level):
    inventory = set()
    attempts = 0

    while len(inventory) < size and attempts < 100:
        dx = random.uniform(-1.0, 1.0)
        dy = random.uniform(-1.0, 1.0)

        wx = NOISE_SEED + dx
        wy = NOISE_SEED + dy

        weapon = select_from_noise(wx, wy, WEAPONS, WEAPON_SCALE)
        material = select_from_noise(wx + 100, wy + 100, MATERIALS, MATERIAL_SCALE)
        quality = get_quality(skill_level)

        item = f"{quality} {material} {weapon}"
        inventory.add(item)
        attempts += 1

    return list(inventory)

# Generate and print 
if __name__ == "__main__":
    shop_items = generate_blacksmith_inventory(SHOP_SIZE, BLACKSMITH_SKILL)

    print(f"🛠️  Blacksmith's Shop (Skill {BLACKSMITH_SKILL})")
    for i, item in enumerate(shop_items, 1):
        print(f"{i}. {item}")
