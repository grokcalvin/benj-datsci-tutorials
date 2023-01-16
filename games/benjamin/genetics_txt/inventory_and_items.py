from dataclasses import dataclass
from typing import List
import copy

class Armor:
    def __init__(self,name,damage_absorption,value=0,inventory_parent=None,entity_parent=None,lore=None,quantity=1) -> None:
        self.name = name
        self.damage_absorption = damage_absorption
        self.quantity = quantity
        self.entity_parent = entity_parent
        self.inventory_parent = inventory_parent
        self.is_stackable = False
        self.lore = lore
        self.value = value

    def equip(self):
        if self.entity_parent.armor != None:
            self.entity_parent.Inventory.add(self.entity_parent.armor)
        if self.entity_parent.armor == None:
            self.entity_parent.armor = self
        else:
            print(f"A unknown item is in Armor slot for {self.entity_parent.name} {self.entity_parent.last_name}")

class Weapon:
    def __init__(self,name,damage,inventory_parent=None,value=0,entity_parent=None,lore=None,quantity=1) -> None:
        self.name = name
        self.base_damage = damage
        self.quantity = quantity
        self.entity_parent = entity_parent
        self.inventory_parent = inventory_parent
        self.is_stackable = False
        self.lore = lore
        self.value = value

    def equip(self):
        if self.entity_parent.weapon != None:
            self.entity_parent.Inventory.add(self.entity_parent.weapon)
        if self.entity_parent.weapon == None:
            self.entity_parent.weapon = self
        else:
            print(f"A unknown item is in weapon slot for {self.entity_parent.name} {self.entity_parent.last_name}")

class Consumable:
    def __init__(self,name,damage_absorption,quantity,inventory_parent=None,entity_parent=None,lore=None) -> None:
        self.name = name
        self.health_increase = damage_absorption
        self.quantity = quantity
        self.entity_parent = entity_parent
        self.inventory_parent = inventory_parent
        self.is_stackable = True
        self.lore = lore

    #pass the owner to the eat method

    def eat(self):
        self.quantity -= 1
        self.entity_parent.health += self.health_increase
        if self.entity_parent.health > self.entity_parent.max_health:
            self.entity_parent.health = self.entity_parent.max_health
        if self.quantity <= 0:
            self.inventory_parent.remove(self)
    def add_quantity(self,item_quantity):
        self.quantity += item_quantity

class Inventory:
    def __init__(self,parent=None) -> None:
        self.items = []
        self.parent = parent
        #you are passing the parent to the innit not creating it
    #certain items have info to access and thats how they have there effect, e.g. Armor
    #when scaping Armor you can keep one of its components

    def add(self,item):
        if item.name in [ii.name for ii in self.items] and item.is_stackable:
        #if you reduce the items in inventory by filtered list comprhension and change the object in list, does the item in non filtered list change as well.
            for i in self.items:
                if item.name == i.name and i.is_stackable and item.is_stackable:
                    i.add_quantity(item.quantity)
                    break
        else:
            item.inventory_parent = self
            item.entity_parent = self.parent
            self.items.append(item)

#if equipment == object del just like, all entities

    def remove(self,item):
        #this will always for for the first of the names items first
        #this deletes from this inventory object
        deep_item = copy.deepcopy(item)
        if item.name in [ii.name for ii in self.items]:

            name_list = [ii.name for ii in self.items]
            index1 = name_list.index(deep_item.name)
            self.items[index1].quantity -= item.quantity
            if self.items[index1].quantity <= 0:
                del self.items[index1]
        else:
            print("this item cant be removed from this inventory becuase none exist in this Inventory")

#a stat that changes based on gear, when you remove the gear it takes back the stats.
    def add_items(self,items:list):
        if type(items) == list:
            for item in items:
                self.add(item)
        if type(items) == Inventory:
            for item in items.items:
                self.add(item)

    def remove_items(self,items):
        deep_copy_items = copy.deepcopy(items)

        if type(items) == list:
            for item in deep_copy_items:
                self.remove(item)
        if type(items) == Inventory:
            for item in deep_copy_items.items:
                self.remove(item)

    def print_inventory(self):
        for i in self.items:
            print(f" - {i.name} x{i.quantity}")

#weapon definitions
def rusty_short_sword():
    rusty_short_sword = Weapon(name="rusty_short_sword",damage=5)
    return rusty_short_sword

def short_sword():
    short_sword = Weapon(name="short_sword",damage=7)
    return short_sword

def quality_short_sword():
    quality_short_sword = Weapon(name="quality_short_sword",damage=9)
    return quality_short_sword



def typical_rusty_sword():
    typical_rusty_sword = Weapon(name="typical_rusty_sword",damage=8)
    return typical_rusty_sword

def typical_sword():
    typical_sword = Weapon(name="typical_sword",damage=10)
    return typical_sword

def quality_typical_sword():
    quality_typical_sword = Weapon(name="quality_typical_sword",damage=10)
    return quality_typical_sword



def rusty_long_sword():
    rusty_long_sword = Weapon(name="rusty_long_sword",damage=12)
    return rusty_long_sword

def long_sword():
    long_sword = Weapon(name="long_sword",damage=12)
    return long_sword

def quality_long_sword():
    quality_long_sword = Weapon(name="quality_long_sword",damage=14)
    return quality_long_sword



def basic_rags():
    basic_rags = Armor(name="basic_rags",damage_absorption= 1)
    return basic_rags

def warriors_leather():
    warriors_leather = Armor(name="warriors_leather",damage_absorption= 3)
    return warriors_leather

def leather_armor():
    leather_armor = Armor(name="leather_armor",damage_absorption= 5)
    return leather_armor



def basic_rope():
    basic_rope = Armor(name="v",damage_absorption= 2)
    return basic_rope

def silk_robe():
    silk_robe = Armor(name="silk_robe",damage_absorption= 10)
    return silk_robe



def broken_chain_armor():
    broken_chain_armor = Armor(name="broken_chain_armor",damage_absorption= 10)
    return broken_chain_armor

def chain_armor():
    chain_armor = Armor(name="chain_armor",damage_absorption= 12.5)
    return chain_armor



def metal_and_leather_armor():
    metal_and_leather_armor = Armor(name="metal_and_leather_armor",damage_absorption= 12.5)
    return metal_and_leather_armor
    
def metal_arrmor():
    metal_arrmor = Armor(name="metal_arrmor",damage_absorption= 20)
    return metal_arrmor
    
def main():
    Inventory_1 = Inventory()
    Inventory_1.add(item=Consumable(
        name="burger",
        health_increase=10,
        quantity=5
    ))
    Inventory_1.add(item=Consumable(
        name="ice cream",
        health_increase=5,
        quantity=1
    ))
    Inventory_1.add(item=Consumable(
        name="popcorn",
        health_increase=30,
        quantity=2
    ))
    Inventory_1.print_inventory()
    print("---------------")
    Inventory_1.add(item=Consumable(
        name="ice cream",
        health_increase=5,
        quantity=1
    ))
    Inventory_1.print_inventory()





    Inventory_2 = Inventory()
    Inventory_2.add(item=Consumable(
        name="hamburger",
        health_increase=10,
        quantity=2
    ))
    Inventory_2.add(item=Consumable(
        name="ice cream",
        health_increase=5,
        quantity=3
    ))
    Inventory_2.add(item=Consumable(
        name="carmel_popcorn",
        health_increase=30,
        quantity=1
    ))
    print("---------------")
    Inventory_2.print_inventory()


    Inventory_1.add_items(Inventory_2)
    print("------------")
    Inventory_1.print_inventory()




    print("--------Old Inventory-----")
    Inventory_2.print_inventory()
    print("----New Inventory 2-----")
    Inventory_2.remove_items(Inventory_2)
    Inventory_2.print_inventory()

    human_1 = summon_human(Level=3)
    print(human_1.max_health)
    human_1.health -= 30
    print(human_1.health)
    print(Inventory_1.items[1].name)
    Inventory_1.items[1].entity_parent = human_1
    Inventory_1.items[1].eat()
    print(human_1.health)

    print("\n")
    Inventory_3 = Inventory()
    Inventory_3.add(item=Consumable(
        name="burger",
        health_increase=10,
        quantity=5
    ))
    #code thats easy to test is good, if its hard to test then bad
    Inventory_4 = Inventory()
    Inventory_4.add(item=Consumable(
        name="burger",
        health_increase=10,
        quantity=4
    ))
    Inventory_4
    Inventory_3.remove(Inventory_4.items[0])
    Inventory_3.print_inventory()

# if __name__ == "__main__":
#     main()

#loot tables