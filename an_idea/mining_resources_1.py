from Inventory import *
from blacksmith_shop_test_3 import *
from character_2 import *

def perform_mining(character, tile_mined, skill_quality):
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

    resource_info = resource_map[tile_mined]
    base = resource_info["base_amount"]

    # Amount multiplier by quality
    tier_multiplier = {
        "Awful": 0,
        "Poor": 5,
        "Normal": 10,
        "Good": 15,
        "Excellent": 20,
        "Masterwork": 30,
        "Legendary": 50
    }
    quality = get_quality(5)
    quantity = int(base * tier_multiplier[quality])

    if quantity <= 0:
        print(f"{character.name} failed to mine anything ({skill_quality} quality).")
        return

    mined_item = Item(
        name=resource_info["name"],
        parent_inventory=character.inventory,
        quantity=quantity,
        is_stackable=True
    )

    character.inventory.add(mined_item)
    print(f"{character.name} mined {mined_item.name} with {quality} quality, +{quantity} {mined_item.name}")


if __name__ == "__main__":
    character = Character("Banjo")
    perform_mining(character,"🪨 ", 5)
