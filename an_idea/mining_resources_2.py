from Inventory import *
from blacksmith_shop_test_3 import *
from character_2 import *

def perform_mining(character, tile_mined):
    """Simulates mining a tile and adds result to character's inventory."""

    resource_map = {
        "⚫": {"name": "Coal", "base_amount": 1},
        "🪨 ": {"name": "Iron Ore", "base_amount": 1},
        "🔷": {"name": "Crystal Shard", "base_amount": 1},
        "🍄": {"name": "Cave Mushroom", "base_amount": 1}
    }

    if tile_mined not in resource_map:
        print("There's nothing to mine here.")
        return

    # Ensure mining skill exists
    if "mining" not in character.skills:
        character.add_skill("mining")

    # Determine mining quality from skill level
    skill_level = character.skills["mining"]["level"]
    quality = get_quality(skill_level)

    # Tier multiplier based on quality
    tier_multiplier = {
        "Awful": 0,
        "Poor": 5,
        "Normal": 10,
        "Good": 15,
        "Excellent": 20,
        "Masterwork": 30,
        "Legendary": 50
    }

    resource_info = resource_map[tile_mined]
    base = resource_info["base_amount"]
    quantity = int(base * tier_multiplier[quality])

    if quantity <= 0:
        print(f"{character.name} failed to mine anything ({quality} quality).")
        return

    mined_item = Item(
        name=resource_info["name"],
        parent_inventory=character.inventory,
        quantity=quantity,
        is_stackable=True
    )

    character.inventory.add(mined_item)
    print(f"{character.name} mined {mined_item.name} with {quality} quality, +{quantity} {mined_item.name}")

    # Optionally grant mining XP
    character.add_skill_xp("mining", 5)


# Example usage
if __name__ == "__main__":
    character = Character("Banjo")
    character.add_skill("mining")  # make sure the mining skill is initialized
    perform_mining(character, "🪨 ")
