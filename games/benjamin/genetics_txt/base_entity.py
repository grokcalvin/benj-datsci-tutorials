import random
from inventory_and_items import Inventory, Consumable, Armor, silk_robe, rusty_short_sword
from move_class import move_class, Move_Types
from pathlib import Path
import pools
from enum import Enum


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
    def dexterity_check(self,attacker_dexterity):
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
        if not self.armor is None:
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
