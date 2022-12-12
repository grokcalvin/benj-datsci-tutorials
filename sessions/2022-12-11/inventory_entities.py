"""
Consumable

Weapons

Armor

"""

from dataclasses import dataclass
from typing import List

@dataclass
class Item:
    name: str
    quantity: int = 1


class Inventory:
    def __init__(self) -> None:
        self.storage: List[Item]
    
    def add(self, item: Item):
        names = [item.name for item in self.storage]
        for i, name in enumerate(names):
            if item.name == name:
                self.storage[i].quantity += item.quantity
        
        if item.name not in names:
            self.storage.append(item)


class HealthIncrease:
    name: str
    health_amount: int

    def action(self, entity):
        new_health = entity.health  + self.add_health
        # don't add more health than the maximum allowed
        entity.health = min(new_health, self.max_health)



# class Consumable: 
#     pass

# class Weapon:
#     pass

# class Armor:
#     pass
