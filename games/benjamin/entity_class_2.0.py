import random
from entity_class_Dec_2_2022 import random_scale_3

#trend stat, is_male is random number, and then you test if new random number is greater than that trend stat.
#trend function, with a trend stat input and then a output

#need a initialization of players stats and name

with open("male_names.txt","r") as a:
    male_names_list = a.read().splitlines()
print(male_names_list)

with open("female_names.txt","r") as a:
    female_names_list = a.read().splitlines()
print(female_names_list)

with open("last_names.txt","r") as a:
    last_names_list = a.read().splitlines()
print(last_names_list)

class BaseHumanoidEntity():
    def __init__(self,race,leg_length,torso_height,arm_length,size,level,level_up_points,strength,constitution,dexterity,wisdom,intelligents,charisma,is_player=False,is_male=random.randint(0,1)) -> None:
        self.is_player :bool = is_player
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

        #do i want a separate function modifying the gender and stats of an entity this way different modifiers per race

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

    def random_attack(self):
        #random number based on the len of move types, then use that indexed item from list to find the matching dictionary value which is a object that has damage multiplier, and need to accept parent entity values to perform a function for a output.
        #also calculate the damage then use that a a weight to calculate what move they will do adding up all the values that came before it and one after it to see if it falls in that range.
        #random item in a list, thats used as a dictionary key, and do a function on that object with the entity being passed as a argument.
        #class with need, body types that are used in calculating, muscle groups, and then xp level of move, this will give the damage output that can be blocked.
        #players get to veiw their move list and then if input in list then use input as key for dictionary.
        return (1,random.randint(1,20))

#does having a main class for everything make more sense compared to functions because of all the inputs you need to change in the function.
#instead have all classes inherit from a main one the functions, but give them different innit functions.

    def choose_attack(self):
        pass


    def Dexterity_Check(self,attacker):
        #attacker.random_attack role, this gets rid of the need for a incoming attack variable
        #but will need a is player arguement for if the player wants to do a specific attack
        if attacker.is_player:
            #attack,role = attacker.choose_attack()
            attack,role = attacker.random_attack()
              
        else:
            attack,role = attacker.random_attack()
        
        if (0.10)*(self.dexterity-attacker.dexterity) < random.random():
            if role == 20:
                self.health = self.health - attack*2
                print(f"Critical Hit x2 damage")
                print(f"{attacker.race} - {attacker.name} {attacker.last_name} does {attack*2} damage to {self.race} - {self.name} {self.last_name}\n{self.race} - {self.name} {self.last_name} is at {self.health}HP.")
            elif role == 1:
                print(f"{attacker.race} - {attacker.name} {attacker.last_name} critcal failure, clean miss, {self.race} - {self.name} {self.last_name} takes 0 damage.")
            else:
                self.health = self.health - attack
                print(f"{attacker.race} - {attacker.name} {attacker.last_name} does {attack} damage to {self.race} - {self.name} {self.last_name}\n{self.race} - {self.name} {self.last_name} is at {self.health}HP.")
        else:
            print(self.race+" dodged")

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
                                leg_length= random_scale_3(0.9),
                                torso_height = random_scale_3(1.1),
                                arm_length = random_scale_3(1),
                                size = random_scale_3(0.5),

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


human_bob = summon_human(10)

print(human_bob.max_health)
print(human_bob.level)
print(human_bob.size)
print(human_bob.wisdom)
print(human_bob.race)



class party():
    def __init__(self,entities:list):
        self.entities = entities




player_1 = summon_human(Level=1, is_player = False)
party_1 = party(entities=[player_1])
print(party_1.entities)

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

        for i in all_entities:
            party_1_attacking = i in party_1.entities
            if party_1_attacking:
                target = party_2.entities[random.randrange(len(party_2.entities))]
                target.Dexterity_Check(i)
                print('\n')
                #target.health = target.health - i.Random_Attack_Damage()
                if target.health <= 0:
                   all_entities,party_2 = player_died(target,all_entities,party_2)
            else:
                target = party_1.entities[random.randrange(len(party_1.entities))]
                target.Dexterity_Check(i)
                print('\n')
                #target.health = target.health - i.Random_Attack_Damage()
                if target.health <= 0:
                    all_entities,party_1 = player_died(target,all_entities,party_1)
            if len(party_1.entities) == 0:
                print("Party 1 has lost")
                return "Party 2 wins"
            elif len(party_2.entities) == 0:
                print("Party 2 has lost")
                return "Party 1 wins"
        print("-------")
        #if player modul, after the automation
        #actor
        #target

        #random target of opposite party


def random_battle_goblin(party_1):
    #sets goblin to a party and in all_entities list

    #this is a problem, everytime I rerun the function the same dead entity is used.
    entity_one = summon_goblin(Level=random.randint(1,3))
    entity_two = summon_goblin(Level=random.randint(1,3))
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