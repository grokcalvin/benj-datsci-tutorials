import random
from move_class import move_class, Move_Types
from inventory_and_items import Inventory, Consumable, Armor, silk_robe, rusty_short_sword
from pathlib import Path
import time
import pools
from dataclasses import dataclass
from enum import Enum


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

PARENT_DIR = Path(__file__).parent


def random_scale(base=1):
    types_of_scale = [
        "Average",
        "Small",
        "Very Small",
        "Super Small",
        "Big",
        "Very Big",
        "Super Big"
    ]
    weights = [
        80,
        9,
        0.9,
        0.1,
        9,
        0.9,
        0.1,
    ]
    scale_type = random.choices(types_of_scale,weights)[0]

    if scale_type == "Average":
        return random.uniform(0.9,1.1)*base
    if scale_type == "Small":
        return random.uniform(0.8,0.9)*base
    if scale_type == "Very Short":
        return random.uniform(0.64,0.8)*base
    if scale_type == "Super Short":
        return random.uniform(0.51,0.64)*base
    if scale_type == "Big":
        return random.uniform(1.1,1.25)*base
    if scale_type == "Very Big":
        return random.uniform(1.25,1.56)*base
    if scale_type == "Super Big":
        return random.uniform(1.56,1.95)*base

#trend stat, is_male is random number, and then you test if new random number is greater than that trend stat.
#trend function, with a trend stat input and then a output

#need a initialization of players stats and name

#random loot tables that are appended to the inventory of entities

#need a way to level up and put points on things

#when not in battle, option to eat food

male_names_file = PARENT_DIR / "male_names.txt"
with male_names_file.open() as f:
    male_names_list = f.read().splitlines()

female_names_file = PARENT_DIR / "female_names.txt"
with female_names_file.open() as f:
    female_names_list = f.read().splitlines()

last_names_file = PARENT_DIR / "last_names.txt"
with last_names_file.open() as f:
    last_names_list = f.read().splitlines()

class Occupation(Enum):
    WARRIOR = "Warrior"
    MARTIAL_ARTIST = "Martial Artist"

class BaseHumanoidEntity:
    def __init__(self,race,leg_length,torso_height,arm_length,size,level,level_up_points,strength,constitution,dexterity,wisdom,intelligents,charisma,is_player=False,is_male=random.randint(0,1)) -> None:
        self.is_player :bool = is_player

        self.Inventory = Inventory(parent=self)


        self.level : int = level
        self.level_up_points : int = level_up_points
        self.xp = 0
        self.xp_for_next_level_up = 100
        for a in range(self.level-1):
            self.xp = self.xp_for_next_level_up
            self.xp_for_next_level_up = self.xp_for_next_level_up *1.5
        if self.is_player and self.level_up_points > 0:
            self.Use_Level_Up_Points
        if not self.is_player and self.level_up_points > 0:
            self.Auto_Add_Level_Up_Points
        #something that tracks stats that are the same for every entity
        #entity sizes
        #entity muslces

        #entity attrubites
        #this helps debugging and good practice
        #everything has clear onwership
        #debugging shows onwership
        #when you start to run into problem with complexity


        if is_male == 0:
            self.is_male = True
        else:
            self.is_male = False

        if self.is_player == False and self.is_male:
            self.name = male_names_list[random.randint(0,(len(male_names_list)-1))]

        if self.is_player == False and not self.is_male:
            self.name = female_names_list[random.randint(0,(len(female_names_list)-1))]

        self.last_name = last_names_list[random.randint(0,(len(last_names_list)-1))]

        if self.is_player:
            self.name= input("enter your first name:")
            self.last_name= input("enter your last name:")

        self.race :str = race

        self.leg_length : float = leg_length
        self.torso_height : float = torso_height
        self.arm_length : float = arm_length
        self.size : float = size
        if not self.is_male:
            self.size = self.size*0.93

        self.strength : int = strength
        self.constitution :int = constitution
        self.dexterity :int = dexterity

        self.wisdom :int = wisdom
        self.intelligents :int = intelligents
        self.charsima :int = charisma

        self.max_health = round((((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(10*self.constitution),0)
        self.health = self.max_health



        self.chest_muscle_group = random.randint(1,2000)
        self.arm_muscle_group = random.randint(1,2000)
        self.core_muscle_group = random.randint(1,2000)
        self.leg_muscle_group = random.randint(1,2000)

        #effects list

        self.effects = []

        #print(f"chest muscle group {self.chest_muscle_group}")
        #print(f"arm muscle group {self.arm_muscle_group}")
        #print(f"core muscle group {self.core_muscle_group}")
        #print(f"leg muscle group {self.leg_muscle_group}")


        #MAYBE have level ups that unlock moves.

        #gear
        self.armor = None
        self.weapon = None

        #classes
        class_list = [Occupation.WARRIOR,Occupation.MARTIAL_ARTIST]
        if not self.is_player:
            self.character_class = class_list[random.randint(0,(len(class_list))-1)]

        else:
            valid_input = False
            while not valid_input:
                try:
                    print("enter the class that you would like.")
                    for n,s in enumerate(class_list):
                        print(f"({n}) {s.value}")
                    input1 = input()
                    self.character_class = class_list[int(input1)]
                except:
                    print("invalid input try again!\n")
                else:
                    valid_input = True
                    print(f"you are now a {self.character_class}\n")

        #moves
        if self.character_class == Occupation.WARRIOR:
            self.move_list = [
                Move_Types.SLASH,
                Move_Types.STAB,
                Move_Types.PUNCH
                ]
        if self.character_class == Occupation.MARTIAL_ARTIST:
            self.move_list = [
                Move_Types.FRONT_KICK,
                Move_Types.FORWARD_GAB,
                Move_Types.UPPER_CUT
                ]           

            #grabs a specifcially names move based on "move", then adds to dictionary and gives a object as value from the add_moves function.
            #body usage types
            #function that uses the info of the object to filter through which body type to use
            #.action is used on the dictionary value object to give back a damage value
            #will need a armor devider of damage
            #make size a slight aborber armor - attack
            #average attack is 10, average aborbsion is size**2

            #object will have xp and level attributes

        self.move_dict = {}

        #use list comprhension to only display  the moves you can do filtering throught each move based on the weapon equiped

        for move in self.move_list:
            self.move_dict[move] = move_class(move_type=move)
            print(self.move_dict)



        self.get_loot()
        if not self.is_player:
            print(f"{self.race} {self.level} weapon {self.weapon.name}")
            print(f"{self.race} {self.level} armor {self.armor.name}")

    def get_loot(self):
        if not self.is_player:
            if self.level >=15:
                weapon = pools.select_from_pool(pools.teir_3_weapon_pool,roles=1)[0]
                weapon.add_parent_entity(parent=self)
                weapon.equip()
            elif self.level >=10:
                weapon = pools.select_from_pool(pools.teir_2_weapon_pool,roles=1)[0]
                weapon.add_parent_entity(parent=self)
                weapon.equip()
            elif self.level >=5:
                weapon = pools.select_from_pool(pools.teir_1_weapon_pool,roles=1)[0]
                weapon.add_parent_entity(parent=self)
                weapon.equip()


            if self.level >=15:
                armor = pools.select_from_pool(pools.teir_3_armor_pool,roles=1)[0]
                armor.add_parent_entity(parent=self)
                armor.equip()
            elif self.level >=10:
                armor = pools.select_from_pool(pools.teir_2_armor_pool,roles=1)[0]
                armor.add_parent_entity(parent=self)
                armor.equip()
            elif self.level >=5:
                armor = pools.select_from_pool(pools.teir_1_armor_pool,roles=10)[0]
                armor.add_parent_entity(parent=self)
                armor.equip()
        if self.is_player:
                weapon = rusty_short_sword()
                weapon.add_parent_entity(parent=self)
                weapon.equip()

        #later have a loot table that has chances for swords and armor then select the best one.
    def Set_Health(self):
        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health        

    def Auto_Add_Level_Up_Points(self):
        #you want a separate Level_up_points stat so if you rerun this function it doesnt re add the level up points suing your current level
        while self.level_up_points > 0:
            random_attribute = random.randint(1,6)
            if random_attribute == 1:
                self.strength += 1
            elif random_attribute == 2:
                self.constitution +=1
            elif random_attribute == 3:
                self.dexterity +=1
            elif random_attribute == 4:
                self.wisdom +=1
            elif random_attribute == 5:
                self.intelligents +=1
            elif random_attribute == 6:
                self.charsima +=1
            self.level_up_points -= 1

            #tied to level up points not level
            if not self.is_player:
                self.arm_muscle_group += round(250/((self.arm_muscle_group/1000)**2),0)
                self.chest_muscle_group += round(250/((self.chest_muscle_group/1000)**2),0)
                self.core_muscle_group += round(250/((self.core_muscle_group/1000)**2),0)
                self.leg_muscle_group += round(250/((self.leg_muscle_group/1000)**2),0)

#a mvoe class like warrior that desides how you xp is spent on moves

    def Use_Level_Up_Points(self):
        while self.level_up_points > 0:
            print("You have a available level up point type what stat you would like to increase:")
            print(f"(0)strength {self.strength}")
            print(f"(1)constitution {self.constitution}")
            print(f"(2)dexterity {self.dexterity}")
            print(f"(3)wisdom {self.wisdom}")
            print(f"(4)intelligents {self.intelligents}")
            print(f"(5)charsima {self.charsima}")

            attribute_input = int(input(":"))
            if attribute_input == 0:
                self.strength += 1
            elif attribute_input == 1:
                self.constitution +=1
            elif attribute_input == 2:
                self.dexterity +=1
            elif attribute_input == 3:
                self.wisdom +=1
            elif attribute_input == 4:
                self.intelligents +=1
            elif attribute_input == 5:
                self.charsima +=1
            self.level_up_points -= 1

    def check_for_level_up(self):
        while self.xp >= self.xp_for_next_level_up:
            self.level += 1
            if self.is_player:
                print(f"{self.race} {self.name} {self.last_name} is now level {self.level}")
            #if self is in party of player
            self.level_up_points += 1
            self.xp_for_next_level_up = round(self.xp_for_next_level_up*1.5,1)
            if not self.is_player:
                self.Auto_Add_Level_Up_Points()
            else:
                self.Use_Level_Up_Points()

    def random_attack(self):
        #random number based on the len of move types, then use that indexed item from list to find the matching dictionary value which is a object that has damage multiplier, and need to accept parent entity values to perform a function for a output.
        #also calculate the damage then use that a a weight to calculate what move they will do adding up all the values that came before it and one after it to see if it falls in that range.
        #random item in a list, thats used as a dictionary key, and do a function on that object with the entity being passed as a argument.
        #class with need, body types that are used in calculating, muscle groups, and then xp level of move, this will give the damage output that can be blocked.
        #players get to veiw their move list and then if input in list then use input as key for dictionary.
        #when run the function, also add xp to move, and xp to muslce groups
        ###attack = self.move_dict[self.move_list[random.randint(0,len(self.move_list))-1]].action(self)#maybe pass limb size and muscle groups to this#test if self works
        #do we want a separate moves list vs a dictionary, call and print the moves from the dictionary keys

        #make the role come separate from random attack
        #also have if role 20, dodges dont work.
        attack_type = self.move_list[random.randrange(0,(len(self.move_list)))]
        attack = self.move_dict[attack_type].action(parent=self)
        attack_type = attack_type.value
        return (attack,attack_type)

#does having a main class for everything make more sense compared to functions because of all the inputs you need to change in the function.
#instead have all classes inherit from a main one the functions, but give them different innit functions.

    def choose_attack(self):
        #print("\nplayer avialable moves:")
        #for m in self.move_list:
        #    print(f" - {m}")
        attack_type = input("Which attack move will you use?")
        #dictionary keys makes a list then index that list with text input
        for k,v in self.move_dict.items():


            #this ling errors
            if k.value == attack_type:
                print(k.value)
                attack = v.action(parent=self)
                return (attack,attack_type)
        #attack = self.move_dict[attack_type].action(parent=self)


        #pass in the target and attacker dexterity values
    def Dexterity_Check(self,attacker_dexterity):
        #attacker.random_attack role, this gets rid of the need for a incoming attack variable
        #but will need a is player arguement for if the player wants to do a specific attack
        if (0.10)*(self.dexterity-attacker_dexterity) < random.random():
            #dexterity shouldnt be running combact it should check dexerity
            #if you want it to run combact then rename it
            #refactor
            #where does role come from?
            return False
        else:
            return True

    def take_attack(self,attack):
        if not self.armor == None:
            attack -= self.armor.damage_absorption

        self.defualt_defence = round(((((self.arm_muscle_group+self.chest_muscle_group+self.core_muscle_group+self.leg_muscle_group)/4)/1000)**2),2)

        attack = attack - self.defualt_defence
        if attack <= 0:
            attack = 0.01

        self.health -= attack
        return attack

    def print_stats(self):
        print(f"chest muscle group {self.chest_muscle_group}")
        print(f"arm muscle group {self.arm_muscle_group}")
        print(f"core muscle group {self.core_muscle_group}")
        print(f"leg muscle group {self.leg_muscle_group}")

        print(f"Leg length {self.leg_length}")
        print(f"torso height  {self.torso_height}")
        print(f"arm length {self.arm_length}")
        print(f"size {self.size}")

        print(f"")

        print(f"level - {self.level}")

    def round_over(self):
        try:
            for E_I in self.effects:
                if E_I.is_recurring:
                    E_I.recurring()
                E_I.round_duration -= 1
                if E_I.round_duration <= 0:
                    E_I.remove()
        except Exception as exc:
            #does this work?
            print(exc)


def summon_human(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Human",
                                leg_length= random_scale(1),
                                torso_height = random_scale(1),
                                arm_length = random_scale(1),
                                size = random_scale(1),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 10,
                                constitution = 10,
                                dexterity = 10,

                                wisdom = 10,
                                intelligents = 10,
                                charisma =10
                                )
    entity.Auto_Add_Level_Up_Points()
    return entity

def summon_goblin(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Goblin",
                                leg_length= random_scale(0.8),
                                torso_height = random_scale(1),
                                arm_length = random_scale(1),
                                size = random_scale(0.7),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 15,
                                constitution = 10,
                                dexterity = 12,

                                wisdom = 6,
                                intelligents = 8,
                                charisma =8
                                )
    entity.Auto_Add_Level_Up_Points()
    return entity

def summon_elf(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Elf",
                                leg_length= random_scale(1),
                                torso_height = random_scale(1.1),
                                arm_length = random_scale(1),
                                size = random_scale(1.1),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 12,
                                constitution = 10,
                                dexterity = 13,

                                wisdom = 12,
                                intelligents = 12,
                                charisma =8
                               )
    entity.Auto_Add_Level_Up_Points()
    return entity

#damage is the weapon damage + profiency

def d(number):
    return random.randint(1,number)

class party():
    def __init__(self,entities:list):
        self.entities = entities


def entity_died(target,all_entities,party,loot_pool):
    if target.health <= 0:

        loot_pool.add_items(target.Inventory)
        loot_pool.add(target.weapon)
        loot_pool.add(target.armor)
        #if the player has nothing in there inventory it will error

        party.entities = [p for p in party.entities if p != target]

        all_entities = [p for p in all_entities if p != target]


def entity_died_1(target,party,loot_pool):
    if target.health <= 0:

        loot_pool.add_items(target.Inventory)
        loot_pool.add(target.weapon)
        loot_pool.add(target.armor)
        #if the player has nothing in there inventory it will error

        party.entities = [p for p in party.entities if p != target]
    #you will need to add a system to add the died players armor and weapon to there inventory

    return party

def battle(all_entities,party_1,party_2,loot_pool):
    #defined party and all entities list happens before this

    #parties are defines in the parent function

    #for e in all_entities:
    #    if e in party_2.entities:
    #        e.health = 1


    while len(party_1.entities) > 0 and len(party_2.entities) > 0:
        #does this update mid iteration>
        #when a level up happens if strength stat in increased it ups all muscle groups by 250
        for attacker in all_entities:
            party_1_attacking = attacker in party_1.entities
            if attacker.health > 0:
                time.sleep(5)
                if party_1_attacking:
                    #if attacker is_player
                    #if is player, see the opposite party and type which one to attacks
                    if attacker.is_player:
                        valid_input = False
                        while valid_input == False:
                            print(f"\nYour targets are:")
                            for n,i in enumerate(party_2.entities):
                                time.sleep(1)
                                print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                            try:
                                target_index = int(input("enter the number of the target you want to attack:"))
                                target = party_2.entities[target_index]
                            except:
                                print("invalid input, try again.")
                            else:
                                valid_input = True
                            print("\n")
                    else:
                        target = party_2.entities[random.randrange(len(party_2.entities))]
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print("enter the attack you would like to do (e.g:front kick):")
                            for n, move in enumerate(attacker.move_list):
                                print(f"({n}) - {move.value}")
                            try:
                                base_attack,attack_type = attacker.choose_attack()
                                valid_input = True
                            except:
                                print("\ninvalid input, try again")
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target
                    #gives a dead tag if Hp is greater than 0

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} {attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            actual_damage = target.take_attack(attack)
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:

                            attack = (base_attack*(attacker.strength)+(base_attack*attack_role/2))
                            actual_damage = target.take_attack(attack)
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage after damage")
                            print(f"target is at {target.health}HP")

                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
                    #pass in i.dexterity
                    #dodge = True/False
                    print('\n')
                    #target.health = target.health - i.Random_Attack_Damage()
                    if target.health <= 0:
                        print(f"{target.race}:{target.name} {target.last_name} has died.")
                        all_entities,party_2 = entity_died(target,all_entities,party_2,loot_pool)
                else:
                    #if attacker is_player
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print(f"\nYour targets are:")
                            for n,i in enumerate(party_1.entities):
                                print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                            target_index = int(input("enter the number of the target you want to attack:"))
                            try:
                                target = party_1.entities[target_index]
                            except:
                                print("invalid number, try again:")
                            else:
                                valid_input = True
                            print("\n")
                    else:
                        target = party_1.entities[random.randrange(len(party_1.entities))]
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print("enter the attack you would like to do (e.g:front kick):")
                            for n, move in enumerate(attacker.move_list):
                                print(f"({n}) - {move.value}")
                            try:
                                base_attack,attack_type = attacker.choose_attack()
                                valid_input = True
                            except:
                                print("\ninvalid input, try again\n")
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} {attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            actual_damage = target.take_attack(attack)
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:

                            attack = (base_attack*(attacker.strength)+(base_attack*attack_role/2))
                            actual_damage = target.take_attack(attack)
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage after")
                            print(f"target is at {target.health}HP")
                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
    #problem that when a character dies they still get one more attack becuase they finish the loop.
                print('\n')
                if target.health <= 0:
                    print(f"{target.race}:{target.name} {target.last_name} has died.")
                    all_entities,party_1 = entity_died(target,all_entities,party_1,loot_pool)
            if len(party_1.entities) == 0:
                print("Party 2 has Wins")
                loot_pool.print_inventory()
                return "Party 2 wins"
            elif len(party_2.entities) == 0:
                print("Party 1 has Wins")
                loot_pool.print_inventory()
                return "Party 1 wins"
        print("-------")

        #this code will cycle though active effects on all entities and test if the duration is up, and remove one duration from it.
        for entity in all_entities:
            entity.round_over()
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
    entity_one = summon_goblin(Level=random.randint(5,10))
    entity_two = summon_goblin(Level=random.randint(5,10))
    print(f"you are fighting 2 goblins!\n(1)- {entity_one.race}:{entity_one.name} {entity_one.last_name}\n(2)- {entity_two.race}:{entity_two.name} {entity_two.last_name}")
    party_2 = party(entities=[entity_one,entity_two])
    all_entities = party_1.entities + party_2.entities
    winner = battle(all_entities,party_1,party_2,loot_pool)
    if winner == "Party 1 wins":
        return "continue"
    elif winner == "Party 2 wins":
        return "GAME OVER"
    #sets off combat until one party is empty

        #when entity dies it gains tag "is alive = False"


def main():
    random_scale(1)
    player_1 = summon_human(Level=1, is_player = True)
    armor_1 = silk_robe()
    armor_1.damage_absorption = 1
    armor_1.entity_parent = player_1
    armor_1.equip()
    party_1 = party(entities=[player_1])
    print(party_1.entities)


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

def battle(all_entities,party_1,party_2,loot_pool):
    #defined party and all entities list happens before this

    #parties are defines in the parent function

    #for e in all_entities:
    #    if e in party_2.entities:
    #        e.health = 1
    while len(party_1.entities) > 0 and len(party_2.entities) > 0:
        for selected_party in [party_1,party_2]:
            for attacker in selected_party.entities:
                pass
    def party_attack_party(attacking_party,targeted_party,loot_pool):
        for attacking_enitity in attacking_party.entity:
            #this checks if the entity is dead so it doesnt attack after death if the entity isnt out of the list.
            if attacking_enitity.health > 0:
                time.sleep(5)
                

            #this block lets the current player in the party select which entity from the opposite party to attack.
                if attacking_enitity.is_player:
                    valid_input = False
                    while valid_input == False:
                        print(f"\nYour targets are:")
                        for n,i in enumerate(targeted_party.entities):
                            time.sleep(1)
                            print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                            try:
                                target_index = int(input("enter the number of the target you want to attack:"))
                                target = targeted_party.entities[target_index]
                            except:
                                print("invalid input, try again.")
                            else:
                                valid_input = True
                            print("\n")

            #this selects and random target from the opposite party. This is used for none player enitiies
                else:
                    target = targeted_party.entities[random.randrange(len(targeted_party.entities))]


            #this block gets the base attack and attack type based on which move the player selects
                if attacking_enitity.is_player:
                    valid_input = False
                    while not valid_input:
                        print("enter the attack you would like to do (e.g:front kick):")
                        for n, move in enumerate(attacking_enitity.move_list):
                            print(f"({n}) - {move.value}")
                        try:
                            base_attack,attack_type = attacking_enitity.choose_attack()
                            valid_input = True
                        except:
                            print("\ninvalid input, try again")

            #this selects a random attack for the selected entity if they are not a player.
                else:
                    base_attack,attack_type = attacking_enitity.random_attack()

            #this next block performs the attack on the targeted entity
                print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} tries {attack_type}")

                dodge = target.Dexterity_Check(attacking_enitity_dexterity=attacking_enitity.dexterity)
                attack_role = d(20)

                print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} {attacking_enitity.strength} strength + roles ({attack_role})/2   base damage {base_attack }")
                
                if dodge and attack_role != 20:
                    print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name}")
                else:
                    if attack_role == 1:
                        print(f"Critical Failure! {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} missed!")
                    elif attack_role == 20:
                        attack = base_attack*(30+attacking_enitity.strength)
                        actual_damage = target.take_attack(attack)
                        print(f"Critcal Attack {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                        if target.armor != None:
                            print(f"armor absorbs {target.armor.damage_absorption}")
                        print("fitness absorption is "+ str(target.defualt_defence))
                        print(f"attacking_enitity does {actual_damage} actual damage")
                        print(f"target is at {target.health}HP")
                    elif attack_role > 1 and attack_role < 20:

                        attack = (base_attack*(attacking_enitity.strength)+(base_attack*attack_role/2))
                        actual_damage = target.take_attack(attack)
                        print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} for {attack} before defence")
                        if target.armor != None:
                            print(f"armor absorbs {target.armor.damage_absorption}")
                        print("fitness absorption is "+ str(target.defualt_defence))
                        print(f"attacking_enitity does {actual_damage} actual damage after damage")
                        print(f"target is at {target.health}HP")

                if target.health <= 0:
                    print(f"{target.race}:{target.name} {target.last_name} has died.")
                    targeted_party = entity_died_1(target,targeted_party,loot_pool)

                if len(targeted_party.entities) == 0:
                    loot_pool.print_inventory()
                    return None







    while len(party_1.entities) > 0 and len(party_2.entities) > 0:
        #does this update mid iteration>
        #when a level up happens if strength stat in increased it ups all muscle groups by 250
        for attacker in all_entities:
            party_1_attacking = attacker in party_1.entities
            if attacker.health > 0:
                time.sleep(5)
                if party_1_attacking:
                    #if attacker is_player
                    #if is player, see the opposite party and type which one to attacks
                    if attacker.is_player:
                        valid_input = False
                        while valid_input == False:
                            print(f"\nYour targets are:")
                            for n,i in enumerate(party_2.entities):
                                time.sleep(1)
                                print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                            try:
                                target_index = int(input("enter the number of the target you want to attack:"))
                                target = party_2.entities[target_index]
                            except:
                                print("invalid input, try again.")
                            else:
                                valid_input = True
                            print("\n")
                    else:
                        target = party_2.entities[random.randrange(len(party_2.entities))]
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print("enter the attack you would like to do (e.g:front kick):")
                            for n, move in enumerate(attacker.move_list):
                                print(f"({n}) - {move.value}")
                            try:
                                base_attack,attack_type = attacker.choose_attack()
                                valid_input = True
                            except:
                                print("\ninvalid input, try again")
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target
                    #gives a dead tag if Hp is greater than 0

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} {attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            actual_damage = target.take_attack(attack)
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:

                            attack = (base_attack*(attacker.strength)+(base_attack*attack_role/2))
                            actual_damage = target.take_attack(attack)
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage after damage")
                            print(f"target is at {target.health}HP")

                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
                    #pass in i.dexterity
                    #dodge = True/False
                    print('\n')
                    #target.health = target.health - i.Random_Attack_Damage()
                    if target.health <= 0:
                        print(f"{target.race}:{target.name} {target.last_name} has died.")
                        all_entities,party_2 = entity_died(target,all_entities,party_2,loot_pool)
                else:
                    #if attacker is_player
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print(f"\nYour targets are:")
                            for n,i in enumerate(party_1.entities):
                                print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                            target_index = int(input("enter the number of the target you want to attack:"))
                            try:
                                target = party_1.entities[target_index]
                            except:
                                print("invalid number, try again:")
                            else:
                                valid_input = True
                            print("\n")
                    else:
                        target = party_1.entities[random.randrange(len(party_1.entities))]
                    if attacker.is_player:
                        valid_input = False
                        while not valid_input:
                            print("enter the attack you would like to do (e.g:front kick):")
                            for n, move in enumerate(attacker.move_list):
                                print(f"({n}) - {move.value}")
                            try:
                                base_attack,attack_type = attacker.choose_attack()
                                valid_input = True
                            except:
                                print("\ninvalid input, try again\n")
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} {attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            actual_damage = target.take_attack(attack)
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:

                            attack = (base_attack*(attacker.strength)+(base_attack*attack_role/2))
                            actual_damage = target.take_attack(attack)
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack} before defence")
                            if target.armor != None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.defualt_defence))
                            print(f"attacker does {actual_damage} actual damage after")
                            print(f"target is at {target.health}HP")
                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
    #problem that when a character dies they still get one more attack becuase they finish the loop.
                print('\n')
                if target.health <= 0:
                    print(f"{target.race}:{target.name} {target.last_name} has died.")
                    all_entities,party_1 = entity_died(target,all_entities,party_1,loot_pool)
            if len(party_1.entities) == 0:
                print("Party 2 has Wins")
                loot_pool.print_inventory()
                return "Party 2 wins"
            elif len(party_2.entities) == 0:
                print("Party 1 has Wins")
                loot_pool.print_inventory()
                return "Party 1 wins"
        print("-------")

        #this code will cycle though active effects on all entities and test if the duration is up, and remove one duration from it.
        for entity in all_entities:
            entity.round_over()