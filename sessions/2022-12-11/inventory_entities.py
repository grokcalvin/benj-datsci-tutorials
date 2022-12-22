from dataclasses import dataclass
from typing import List
class food:
    def __init__(self,name,health_increase,quantity,inventory_parent=None,entity_parent=None) -> None:
        self.name = name
        self.health_increase = health_increase
        self.quantity = quantity
        self.entity_parent = entity_parent
        self.inventory_parent = inventory_parent
        self.is_stackable = True

    def eat(self):
        self.quantity -= 1
        self.entity_parent.health += self.health_increase
        if self.entity_parent.health > self.entity_parent.max_health:
            self.entity_parent.health = self.entity_parent.max_health
        if self.quantity <= 0:
            self.inventory_parent.remove(self)


class Inventory:
    def __init__(self,parent=None) -> None:
        self.items = []
        self.parent = parent
    #certain items have info to access and thats how they have there effect, e.g. armor
    #when scaping armor you can keep one of its components

    def add(self,item):
        if item.name in [ii.names for ii in self.items]:
        #if you reduce the items in inventory by filtered list comprhension and change the object in list, does the item in non filtered list change as well.
            for i in self.items:
                if item.name == i.name and i.is_stackable and item.is_stackable:
                    i.add_quantity(item.count)
        else:
            item.inventory_parent = self
            item.entity_parent = self.parent
            self.items.append(item)

    def remove(self,item):
        #this will always for for the first of the names items first
        #this deletes from this inventory object
        name_list = [ii.name for ii in self.items]
        index1 = name_list.index[item.name]
        del self.items[index1]

    def add_items(self,items:list):
        if type(items) == list:
            for item in items:
                self.add(item)
        if type(items) == Inventory:
            for item in items.items:
                self.add(item)

    def remove_items(self,items):
        if type(items) == list:
            for item in items:
                self.remove(item)
        if type(items) == Inventory:
            for item in items.items:
                self.remove(item)

    def print_inventory(self):
        for i in self.items:
            print(f" - {i}")

Inventory_1 = Inventory
Inventory_1.add(food(
    name="burger",
    health_increase=10,
    quantity=5
))
Inventory_1.add(food(
    name="ice cream",
    health_increase=5,
    quantity=1
))
Inventory_1.add(food(
    name="popcorn",
    health_increase=30,
    quantity=2
))
Inventory_1.print_inventory()

#average 10
#change base_damage*strength

#programmable genes, what you do and focuses on grows, xp. and everyone can develope and gain ablities and just start with some.
#healer

#when calculating gained parent Xp give them the same xp as move xp increase


    #gol the entity's stats to enable easy stat changing
    #scope the variables
    #inventory.parent












































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

