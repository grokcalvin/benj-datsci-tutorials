from dataclasses import dataclass
from typing import List



class HealthIncrease:
    def __init__(self, name: str, health_amount: int, quantity: int) -> None:
        self.name = name
        self.health_amount = health_amount
        self.quantity = quantity

    def action(self, entity):
        new_health = entity.health  + self.health_amount
        # don't add more health than the maximum allowed
        entity.health = min(new_health, entity.max_health)
        self.quantity -= 1
        return entity




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

