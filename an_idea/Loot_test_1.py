import random
import math

# --------------------------
# Core Data
# --------------------------

QUALITY_TIERS = ["Awful", "Poor", "Normal", "Good", "Excellent", "Masterwork", "Legendary"]

ROLE_PROFILES = {
    "Desert Bandit": {
        "weapons": ["Curved Sword", "Dagger", "Shortbow"],
        "armor": ["Cloth Wraps", "Leather Vest"],
        "gear_tags": ["lightweight", "cheap"],
        "personals": ["Worn Map", "Dice Set", "Desert Coin"],
    },
    "Knight": {
        "weapons": ["Longsword", "Lance", "Warhammer"],
        "armor": ["Chainmail", "Plate Armor", "Tower Shield"],
        "gear_tags": ["noble", "heavy", "refined"],
        "personals": ["Family Crest", "Polished Medal", "Vellum Prayer"],
    },
    "Wilderness Mage": {
        "weapons": ["Staff", "Wand", "Dagger"],
        "armor": ["Enchanted Robes", "Wool Cloak"],
        "gear_tags": ["arcane", "light", "rural"],
        "personals": ["Spell Notes", "Animal Bone", "Focus Crystal"],
    }
}

LOCATION_TAGS = {
    "Desert": ["sand-worn", "wrapped", "reflective"],
    "Mountains": ["cold-resistant", "fur-lined", "cracked"],
    "Swamp": ["waterlogged", "rusted", "padded"],
    "Plains": ["dusty", "well-used", "sun-bleached"]
}

MATERIAL_TIERS = ["Bronze", "Iron", "Steel", "Obsidian", "Mithril"]
MATERIAL_THRESHOLDS = [0.2, 0.45, 0.7, 0.88, 1.0]

# --------------------------
# Sigmoid Utility
# --------------------------

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def generate_scaled_value(level, midpoint=5, strength=6, curve=2.5, power=1.5):
    if level <= midpoint:
        x = (level - midpoint) / (midpoint - 0)
    else:
        x = (level - midpoint) / (20 - midpoint) / 3
    shift = x * strength

    r = random.random() ** power
    val = (r - 0.5) * curve + shift
    return sigmoid(val)

# --------------------------
# Value Selection Functions
# --------------------------

def get_quality(level):
    value = generate_scaled_value(level)
    thresholds = [0.14, 0.28, 0.5, 0.68, 0.82, 0.94, 1.0]
    for i, threshold in enumerate(thresholds):
        if value <= threshold:
            return QUALITY_TIERS[i]
    return QUALITY_TIERS[-1]

def get_material(level):
    value = generate_scaled_value(level)
    for i, threshold in enumerate(MATERIAL_THRESHOLDS):
        if value <= threshold:
            return MATERIAL_TIERS[i]
    return MATERIAL_TIERS[-1]

# --------------------------
# Loot Generator
# --------------------------

def generate_loot(role, level, location, seed=None):
    random.seed(seed)
    role_data = ROLE_PROFILES[role]
    location_mods = LOCATION_TAGS.get(location, [])

    loot = []

    # Weapon
    weapon_type = random.choice(role_data["weapons"])
    material = get_material(level)
    quality = get_quality(level)
    location_tag = random.choice(location_mods) if location_mods else ""
    weapon = f"{quality} {material} {weapon_type} ({location_tag})"
    loot.append(weapon)

    # Armor
    armor_type = random.choice(role_data["armor"])
    material = get_material(level)
    quality = get_quality(level)
    location_tag = random.choice(location_mods) if location_mods else ""
    armor = f"{quality} {material} {armor_type} ({location_tag})"
    loot.append(armor)

    # 1–2 personal items
    num_personals = random.randint(1, 2)
    personals = random.sample(role_data["personals"], num_personals)
    loot.extend(personals)

    return loot

# Example loot generation
example_loot = generate_loot(role="Knight", level=13, location="Mountains")
print(example_loot)
#skill should also add loot