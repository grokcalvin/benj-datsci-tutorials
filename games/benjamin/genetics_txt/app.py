import random
from inventory_and_items import Inventory, Consumable, Armor, silk_robe, rusty_short_sword
from dataclasses import dataclass
from enum import Enum
from base_entity import BaseHumanoidEntity
from race_functions import spawn_human, spawn_goblin, spawn_elf
from party import battlev0_1,Party

valid_input = False
while valid_input == False:
        try:
            seed = int(input("enter seed here:(0 = random)"))
            if seed != 0:
                random.seed(seed)
        except:
            print("invalid seed, try again")
        else:
            valid_input = True

#trend stat, is_male is random number, and then you test if new random number is greater than that trend stat.
#trend function, with a trend stat input and then a output

#need a initialization of players stats and name

#random loot tables that are appended to the inventory of entities

#need a way to level up and put points on things

#when not in battle, option to eat food

#damage is the weapon damage + profiency


                #if return battle_over print Party_ wins!
    #make separate function



        #this code will cycle though active effects on all entities and test if the duration is up, and remove one duration from it.
        
        
        
#for entity in all_entities:
#entity.round_over()
        
        
        
        
        #for en in all_entities:
        #    en.round_pass()


            #this does a for loop on all boost_item.round_pass() = lower rounds_active by 1 and if <= 0 then del parent.boost_items


        #if player modul, after the automation
        #actor
        #target

        #random target of opposite party

#default dodge chance
#random.random > (.95)**dexterity dodge

def random_battle_goblin(party_1):

    loot_pool = Inventory()

    #sets goblin to a party and in all_entities list

    #this is a problem, everytime I rerun the function the same dead entity is used.
    entity_one = spawn_goblin(Level=random.randint(5,10))
    entity_two = spawn_goblin(Level=random.randint(5,10))
    print(f"you are fighting 2 goblins!\n(1)- {entity_one.race}:{entity_one.name} {entity_one.last_name}\n(2)- {entity_two.race}:{entity_two.name} {entity_two.last_name}")
    party_2 = Party(entities=[entity_one,entity_two])
    battlev0_1(party_1,party_2,loot_pool)
    #sets off combat until one party is empty

        #when entity dies it gains tag "is alive = False"


def main():
    player_1 = spawn_human(Level=1, is_player = True)
    armor_1 = silk_robe()
    armor_1.damage_absorption = 1
    armor_1.entity_parent = player_1
    armor_1.equip()
    party_1 = Party(entities=[player_1])


    battle_output = random_battle_goblin(party_1)
    if battle_output == "continue":
        print("you have defeated the goblin! and this is the end of the main function")
    if battle_output == "GAME OVER":
        print("You lost to the goblin, GAME OVER, this is the end of the main function")
    #one battle with a random goblin then end
        #full auto battle THEN
        #input in entity race = player

if __name__ == "__main__":
    main()

#skill class, that gives moves and XP
#loot tables