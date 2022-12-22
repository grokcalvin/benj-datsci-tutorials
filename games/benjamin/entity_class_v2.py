import random
from entity_class_Dec_2_2022 import random_scale_3
from move_class import move_class
from inventory_and_items import Inventory, food


#trend stat, is_male is random number, and then you test if new random number is greater than that trend stat.
#trend function, with a trend stat input and then a output

#need a initialization of players stats and name

#random loot tables that are appended to the inventory of entities

#need a way to level up and put points on things

#when not in battle, option to eat food

with open("male_names.txt","r") as a:
    male_names_list = a.read().splitlines()

with open("female_names.txt","r") as a:
    female_names_list = a.read().splitlines()

with open("last_names.txt","r") as a:
    last_names_list = a.read().splitlines()

class BaseHumanoidEntity:
    def __init__(self,race,leg_length,torso_height,arm_length,size,level,level_up_points,strength,constitution,dexterity,wisdom,intelligents,charisma,is_player=False,is_male=random.randint(0,1)) -> None:
        self.is_player :bool = is_player

        self.Inventory = Inventory(parent=self)
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


        self.level : int = level
        self.level_up_points : int = level_up_points

        self.strength : int = strength
        self.constitution :int = constitution
        self.dexterity :int = dexterity

        self.wisdom :int = wisdom
        self.intelligents :int = intelligents
        self.charsima :int = charisma

        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health



        self.neck_muscle_group = random.randint(1,2000)
        self.chest_muscle_group = random.randint(1,2000)
        self.arm_muscle_group = random.randint(1,2000)
        self.core_muscle_group = random.randint(1,2000)
        self.leg_muscle_group = random.randint(1,2000)

        if not self.is_player:
            self.move_list = ["front kick","forward gab","upper cut"]
        else:
            self.move_list = ["front kick","forward gab","upper cut"]




        def load_move(move:str):
            #grabs a specifcially names move based on "move", then adds to dictionary and gives a object as value from the add_moves function.
            #body usage types
            #function that uses the info of the object to filter through which body type to use
            #.action is used on the dictionary value object to give back a damage value
            #will need a armor devider of damage
            #make size a slight aborber armor - attack
            #average attack is 10, average aborbsion is size**2

            #object will have xp and level attributes
            return move_class(move_type=move)

        self.move_dict = {}

        for move in self.move_list:
            self.move_dict[move] = load_move(move=move)
            #print(self.move_dict)

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

#

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
        return (attack,attack_type)

#does having a main class for everything make more sense compared to functions because of all the inputs you need to change in the function.
#instead have all classes inherit from a main one the functions, but give them different innit functions.

    def choose_attack(self):
        #print("\nplayer avialable moves:")
        #for m in self.move_list:
        #    print(f" - {m}")
        attack_type = input("Which attack move will you use?")
        attack = self.move_dict[attack_type].action(parent=self)
        return (attack,attack_type)


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

def summon_human(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Human",
                                leg_length= random_scale_3(1),
                                torso_height = random_scale_3(1),
                                arm_length = random_scale_3(1),
                                size = random_scale_3(1),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 2,
                                constitution = 2,
                                dexterity = 2,

                                wisdom = 2,
                                intelligents = 2,
                                charisma =2
                                )
    entity.Auto_Add_Level_Up_Points()
    return entity

def summon_goblin(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Goblin",
                                leg_length= random_scale_3(0.8),
                                torso_height = random_scale_3(1),
                                arm_length = random_scale_3(1),
                                size = random_scale_3(0.7),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 4,
                                constitution = 2,
                                dexterity = 4,

                                wisdom = 1,
                                intelligents = 2,
                                charisma =2
                                )
    entity.Auto_Add_Level_Up_Points()
    return entity

def summon_elf(Level,is_player=False):
    entity = BaseHumanoidEntity(is_player=is_player,
                                race= "Elf",
                                leg_length= random_scale_3(1),
                                torso_height = random_scale_3(1.1),
                                arm_length = random_scale_3(1),
                                size = random_scale_3(1.1),

                                level = Level,
                                level_up_points = Level - 1,

                                strength = 2,
                                constitution = 2,
                                dexterity = 3,

                                wisdom = 2,
                                intelligents = 3,
                                charisma =1
                                )
    entity.Auto_Add_Level_Up_Points()
    return entity

#damage is the weapon damage + profiency

def d(number):
    return random.randint(1,number)

class party():
    def __init__(self,entities:list):
        self.entities = entities


def player_died(target,all_entities,party):
    if target.health <= 0:

        party.entities = [p for p in party.entities if p != target]

        all_entities = [p for p in all_entities if p != target]

    return all_entities,party

def battle(all_entities,party_1,party_2):
    #defined party and all entities list happens before this

    #parties are defines in the parent function
    while len(party_1.entities) > 0 and len(party_2.entities) > 0:
        #does this update mid iteration>
        #when a level up happens if strength stat in increased it ups all muscle groups by 250
        for attacker in all_entities:
            party_1_attacking = attacker in party_1.entities
            if attacker.health > 0:

                if party_1_attacking:
                    #if attacker is_player
                    #if is player, see the opposite party and type which one to attacks
                    if attacker.is_player:
                        print(f"\nYour targets are:")
                        for n,i in enumerate(party_2.entities):
                            print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                        target_index = int(input("enter the number of the target you want to attack:"))
                        target = party_2.entities[target_index]
                        print("\n")
                    else:
                        target = party_2.entities[random.randrange(len(party_2.entities))]
                    if attacker.is_player:
                        print("enter the attack you would like to do (e.g:front kick):")
                        for n, move in enumerate(attacker.move_list):
                            print(f"({n}) - {move}")

                        base_attack,attack_type = attacker.choose_attack()
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target
                    #gives a dead tag if Hp is greater than 0

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} 10 +{attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            target.health = target.health - attack
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack}")
                            print(f"target is at {target.health}HP")

                        elif attack_role > 1 and attack_role < 20:
                            attack = (base_attack*(10+attacker.strength)+(base_attack*attack_role/2))

                            target.health = target.health - attack
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack}")
                            print(f"target is at {target.health}HP")

                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
                    #pass in i.dexterity
                    #dodge = True/False
                    print('\n')
                    #target.health = target.health - i.Random_Attack_Damage()
                    if target.health <= 0:
                        print(f"{target.race}:{target.name} {target.last_name} has died.")
                        all_entities,party_2 = player_died(target,all_entities,party_2)
                else:
                    #if attacker is_player
                    if attacker.is_player:
                        print(f"\nYour targets are:")
                        for n,i in enumerate(party_1.entities):
                            print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                        target_index = int(input("enter the number of the target you want to attack:"))
                        target = party_1.entities[target_index]
                        print("\n")
                    else:
                        target = party_1.entities[random.randrange(len(party_1.entities))]
                    if attacker.is_player:
                        print("enter the attack you would like to do (e.g:front kick):")
                        for n, move in enumerate(attacker.move_list):
                            print(f"({n}) - {move}")

                        base_attack,attack_type = attacker.choose_attack()
                    else:
                        base_attack,attack_type = attacker.random_attack()

                    #attacker tries ____(front kick) on target

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} tries {attack_type}")

                    dodge = target.Dexterity_Check(attacker_dexterity=attacker.dexterity)
                    attack_role = d(20)

                    print(f"{attacker.race}:{attacker.name} {attacker.last_name} 10 +{attacker.strength} strength + roles ({attack_role})/2   base damage {base_attack }")

                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacker.race}:{attacker.name} {attacker.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacker.race}:{attacker.name} {attacker.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacker.strength)
                            target.health = target.health - attack
                            print(f"Critcal Attack {attacker.race}:{attacker.name} {attacker.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack}")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:
                            attack = (base_attack*(10+attacker.strength)+(base_attack*attack_role/2))


                            target.health = target.health - attack
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacker.race}:{attacker.name} {attacker.last_name} for {attack}")
                            print(f"target is at {target.health}HP")
                            #test the movement with front kick input  
                            #later use the type of attack in the attack prints
    #problem that when a character dies they still get one more attack becuase they finish the loop.

                print('\n')
                if target.health <= 0:
                    print(f"{target.race}:{target.name} {target.last_name} has died.")
                    all_entities,party_1 = player_died(target,all_entities,party_1)
            if len(party_1.entities) == 0:
                print("Party 2 has Wins")
                return "Party 2 wins"
            elif len(party_2.entities) == 0:
                print("Party 1 has Wins")
                return "Party 1 wins"
        print("-------")
        #if player modul, after the automation
        #actor
        #target

        #random target of opposite party

#default dodge chance
#random.random > (.95)**dexterity dodge

def random_battle_goblin(party_1):
    #sets goblin to a party and in all_entities list

    #this is a problem, everytime I rerun the function the same dead entity is used.
    entity_one = summon_goblin(Level=random.randint(1,3))
    entity_two = summon_goblin(Level=random.randint(1,3))
    print(f"you are fighting 2 goblins!\n(1)- {entity_one.race}:{entity_one.name} {entity_one.last_name}\n(2)- {entity_two.race}:{entity_two.name} {entity_two.last_name}")
    party_2 = party(entities=[entity_one,entity_two])
    all_entities = party_1.entities + party_2.entities
    winner = battle(all_entities,party_1,party_2)
    if winner == "Party 1 wins":
        return "continue"
    elif winner == "Party 2 wins":
        return "GAME OVER"
    #sets off combat until one party is empty

        #when entity dies it gains tag "is alive = False"


def main():
    player_1 = summon_human(Level=1, is_player = True)
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