from dataclasses import dataclass
from typing import List
import copy
import random

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
            self.entity_parent.armor = self
        if self.entity_parent.armor == None:
            self.entity_parent.armor = self
        else:
            print(f"A unknown item is in Armor slot for {self.entity_parent.name} {self.entity_parent.last_name}")

    def add_parent_entity(self,parent):
        self.inventory_parent = parent.Inventory
        self.entity_parent = parent

class Weapon:
    def __init__(self,name,damage,inventory_parent=None,value=0,entity_parent=None,lore=None,quantity=1) -> None:
        self.name = name
        self.base_damage = damage
        self.quantity = quantity
        self.entity_parent = entity_parent #the entity it belongs to
        self.inventory_parent = inventory_parent #the inventory it belongs to
        self.is_stackable = False
        self.lore = lore
        self.value = value

    def equip(self):
        if self.entity_parent.weapon != None:
            self.entity_parent.Inventory.add(self.entity_parent.weapon)
            self.entity_parent.weapon = self
        if self.entity_parent.weapon == None:
            self.entity_parent.weapon = self
        else:
            print(f"A unknown item is in weapon slot for {self.entity_parent.name} {self.entity_parent.last_name}")

    def add_parent_entity(self,parent):
        self.inventory_parent = parent.Inventory
        self.entity_parent = parent

class Consumable:
    def __init__(self,name,health_increase,quantity,inventory_parent=None,entity_parent=None,lore=None) -> None:
        self.name = name
        self.health_increase = health_increase
        self.quantity = quantity
        self.entity_parent = entity_parent
        self.inventory_parent = inventory_parent
        self.is_stackable = True
        self.lore = lore

    #pass the owner to the use method

    def use(self):
        self.quantity -= 1
        self.entity_parent.health += self.health_increase
        if self.entity_parent.health > self.entity_parent.max_health:
            self.entity_parent.health = self.entity_parent.max_health
        if self.quantity <= 0:
            self.inventory_parent.remove(self)
    def add_quantity(self,item_quantity):
        self.quantity += item_quantity

    def add_parent_entity(self,parent):
        self.inventory_parent = parent.Inventory
        self.entity_parent = parent

#effects are placed in an entities effect list and every round in a battle it is subtracted 
#reorruring and one and done when cycling through the effects in the effects list, if an effect has Is_recurring it runs the reorrering method
#on round durration <= 0 activate remove
#the use function is ran externally when you use the item

class effect_item():
    def __init__(self,parent_entity,name,is_recurring=False,round_duration=1,health_increase:int=None,strength:int=None,constitution:int=None,dexterity:int=None,wisdom:int=None,intelligents:int=None,charsima:int=None,size_increase=None):
        self.parent = parent_entity
        self.round_durarion = round_duration
        self.name = name
        self.is_recurring = is_recurring

        self.health_increase = health_increase

        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligents = intelligents
        self.charisma = charsima

        self.size_increase = size_increase
    #pass the owner to the use method
            #print(f"(0)strength {self.strength}")
            #print(f"(1)constitution {self.constitution}")
            #print(f"(2)dexterity {self.dexterity}")
            #print(f"(3)wisdom {self.wisdom}")
            #print(f"(4)intelligents {self.intelligents}")
            #print(f"(5)charsima {self.charsima}")
    def use(self):
        if self.health_increase != None:
            self.parent.health += self.health_increase
            if self.parent.health >= self.parent.max_health:
                self.parent.health = self.parent.max_health


        if self.strength != None:
            self.parent.strength += self.strength

        if self.constitution != None:
            self.parent.constitution += self.constitution

        if self.dexterity != None:
            self.parent.dexterity += self.dexterity

        if self.wisdom != None:
            self.parent.wisdom += self.wisdom

        if self.intelligents != None:
            self.parent.intelligents += self.intelligents

        if self.charisma != None:
             self.parent.charisma += self.charisma     

        if self.size_increase != None:
             self.parent.size =  self.parent.size * self.size_increase       

    def recurring(self):
        if self.health_increase != None:
            self.parent.health += self.health_increase
            if self.parent.health >= self.parent.max_health:
                self.parent.health = self.parent.max_health

#for E_I in effects 
    #if recuring function recuring
    #if rounds == 0
        #remove

#on use of item
    #add to effects
    #remove one from inventory

#every round
    #during battle
    #function round_over
        #iterate through all entities
            #iterate through all effects per entity
                #subtract from round duration
                #test is recurring if so then effect


        if self.strength != None:
            self.parent.strength += self.strength

        if self.constitution != None:
            self.parent.constitution += self.constitution

        if self.dexterity != None:
            self.parent.dexterity += self.dexterity

        if self.wisdom != None:
            self.parent.wisdom += self.wisdom

        if self.intelligents != None:
            self.parent.intelligents += self.intelligents

        if self.charisma != None:
             self.parent.charisma += self.charisma     

        if self.size_increase != None:
             self.parent.size =  self.parent.size * self.size_increase

    def remove(self):
        name_list = [e.name for e in self.parent.effects]
        index = name_list.index(self.name)
        self.parent.effects.pop(index)

        #add a lore system on items to be viewed on item inspection

        if self.is_is_recurring:
            pass
        else:
            if self.health_increase != None:
                self.parent.health -= self.health_increase
                if self.parent.health >= self.parent.max_health:
                    self.parent.health = self.parent.max_health


            if self.strength != None:
                self.parent.strength -= self.strength

            if self.constitution != None:
                self.parent.constitution -= self.constitution

            if self.dexterity != None:
                self.parent.dexterity -= self.dexterity

            if self.wisdom != None:
                self.parent.wisdom -= self.wisdom

            if self.intelligents != None:
                self.parent.intelligents -= self.intelligents

            if self.charisma != None:
                self.parent.charisma -= self.charisma     

            if self.size_increase != None:
                self.parent.size =  self.parent.size / self.size_increase

#have a armor effects list or have a effect be linked to armor

#add effects variable in entity class

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
            if item != None:
                self.items.append(item)
            else:
                pass

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

    def open(self,parent=None):
        page_length = 20
        pages = (len(self.items)//page_length)+1
        last_page_number_of_items = len(self.items) % page_length
        open = True
        current_page = 1
        while open == True:
            index = (current_page-1)*page_length
            if current_page == pages:
                print_x_items = last_page_number_of_items
            else:
                print_x_items = page_length


            for i in range(print_x_items):
                index += 1
                print(f"{index} {self.items[index-1].name} x{self.items[index-1].quantity}")
            print(f"page {current_page}/{pages}\ntype p then the page number you want get to. example:p2")
            print("to select a item enter its number. or type \"close\" to exit inventory.")
            valid_input = False
            while valid_input == False:
                try:
                    input1 = input()
                    if input1 == "close":
                        open = False
                        break
                    elif input1[0] == "p":
                        print(input1[1:])
                        if int(input1[1:]) <= pages and int(input1[1:]) > 0:
                            current_page = int(input1[1:])
                            valid_input = True
                        else:
                            print("number out of range, try again.")
                    elif int(input1) > 0 and int(input1) <= len(self.items):
                        print(f"interact with {self.items[int(input1)-1].name}")
                        self.items[int(input1)-1].interact
                        #or have a interact with inventory with an input of item?
                    elif int(input1) <= 0 or int(input1) > len(self.items):
                        print("invalid index try again.")
                    else:
                        print("invalid input")

                        #a tag that inventory has and is set to when/before inventoryis being used.
                            #if tag = in battle inventory then on item use close inventory and change battle object.turn_state = over.
                except:
                    pass
                else:
                    pass



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

#armor definitions

def basic_rags():
    basic_rags = Armor(name="basic_rags",damage_absorption= 1)
    return basic_rags

def warriors_leather():
    warriors_leather = Armor(name="warriors_leather",damage_absorption= 3)
    return warriors_leather

def leather_armor():
    leather_armor = Armor(name="leather_armor",damage_absorption= 5)
    return leather_armor



def basic_robe():
    basic_robe = Armor(name="v",damage_absorption= 2)
    return basic_robe

def silk_robe():
    silk_robe = Armor(name="silk_robe",damage_absorption= 10)
    return silk_robe



def broken_chain_armor():
    broken_chain_armor = Armor(name="broken_chain_armor",damage_absorption= 7.5)
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
    for item in range(151):
        random_num = random.randint(1,3)
        if random_num == 1:
            Inventory_1.add(rusty_short_sword())
        if random_num == 2:
            Inventory_1.add(short_sword())
        if random_num == 3:
            Inventory_1.add(silk_robe())
    Inventory_1.open()



    print("--------Old Inventory-----")
    Inventory_2.print_inventory()
    print("----New Inventory 2-----")
    Inventory_2.remove_items(Inventory_2)
    Inventory_2.print_inventory()

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

if __name__ == "__main__":
    main()

#loot tables