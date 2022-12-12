import random
import math
from dataclasses import dataclass

#%20 short, %60 average %20percent tall then recurively select where you are one the board, output changes per recursion and then do an operation on the remaining value that starts 0-1 float each level changes output by 1.25

#make classes in a different modual
class Human():
    def __init__(self,level:int,is_player=False):
        self.is_player = is_player
        
        self.type = "Human"

        self.leg_length = random_scale_3()
        self.torso_height = random_scale_3()
        self.arm_length = random_scale_3()
        self.size = random_scale_3()
        #need to deep copy when you input new values
        self.move_dict = {"front_kick":{"Xp":0,"Level":1}}

        #moves have directories that decid how the math works

        self.level = level
        self.Level_Up_Points = self.level

        self.strength = 2
        self.constitution = 2
        self.dexterity = 2

        self.wisdom = 2
        self.intelligents = 2
        self.charsima = 2

    #when one a item, you have options based on the items stats, then run function on item.
    #have multipliers that you use when calucating functions outputs.
    #tags that can be added and are used for default calculations

        while self.Level_Up_Points > 0:
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
            self.Level_Up_Points -= 1
            
        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health

    def Random_Attack_Damage(self):
        return 1
    
    #def Dexterity_Check(incoming_attack,entity_being_attacked)
    def Dexterity_Check(self,incoming_attack_Damage):
        if (0.95)**self.dexterity > random.random():
            self.health = self.health - int(incoming_attack_Damage)
            print(self.type+" takes {}".format(incoming_attack_Damage))
        else:
            print(self.type+" dodged")

            #rewrite this in function mode where you do all these in functionss


class goblin():
    def __init__(self,level:int,is_player=False):
        self.is_player = is_player
        
        self.type = "goblin"


#       have a function accept the target and self and use the attackers stats to change the resievers role of dexterity
#       function accepts the target entity as arguement and uses targets attributes to change main calculations

        self.leg_length = random_scale_3(base_multiplier=0.7)
        self.torso_height = random_scale_3(base_multiplier=1)
        self.arm_length = random_scale_3(base_multiplier=0.9)
        self.size = random_scale_3(base_multiplier=0.55)
        #need to deep copy when you input new values
        self.move_dict = {"front_kick":{"Xp":0,"Level":1}}

        self.level = level
        self.Level_Up_Points = self.level -1

        self.strength = 4
        self.constitution = 2
        self.dexterity = 4

        self.wisdom = 1
        self.intelligents = 2
        self.charsima = 1

        while self.Level_Up_Points > 0:
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
            self.Level_Up_Points -= 1

        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health
        

    def Random_Attack_Damage(self):
        return 1

    def Dexterity_Check(self,incoming_attack_Damage):
        if (0.95)**self.dexterity > random.random():
            self.health = self.health - int(incoming_attack_Damage)
            print(self.type+" takes {}".format(incoming_attack_Damage))
        else:
            print(self.type+" dodged")

class elf():
    def __init__(self,level:int,is_player=False):
        self.is_player = is_player

        self.type = "elf"
        
        self.leg_length = random_scale_3(base_multiplier=1.1)
        self.torso_height = random_scale_3(base_multiplier=1)
        self.arm_length = random_scale_3(base_multiplier=1)
        self.size = random_scale_3(base_multiplier=1)
        #need to deep copy when you input new values
        self.move_dict = {"front_kick":{"Xp":0,"Level":1}}

        self.level = level
        self.Level_Up_Points = self.level -1

        self.strength = 2
        self.constitution = 2
        self.dexterity = 3

        self.wisdom = 2
        self.intelligents = 3
        self.charsima = 1

        while self.Level_Up_Points > 0:
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
            self.Level_Up_Points -= 1


        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health

    def Random_Attack_Damage(self):
        return 1

    def Dexterity_Check(self,incoming_attack_Damage):
        if (0.95)**self.dexterity > random.random():
            self.health = self.health - incoming_attack_Damage
            print(self.type+" takes {}".format(incoming_attack_Damage))
        else:
            print(self.type+" dodged")
#base damage * role
#class goblin()


#mucle xp takes xp gained/((muscle_group_xp/1000)^2)
#strength adds 1000 xp to every muscle group when in combact

def random_scale():
    testfor_num = 1
    base = random.random()
    output = 1
    baseline = 0
    #changing number to test for based on the changing base
    while True: 
        testfor_num = testfor_num/10
        if base <= testfor_num:
            output = output*0.8
                    #0+0.1  next is 0.9 + 0.1        #0+0.9  next needs to be 0.9+ 0.09
        if base > baseline+testfor_num and base < baseline+testfor_num*9:
            return output
        if base >= baseline+testfor_num*9:
            baseline = baseline+testfor_num*9
            output = output*1.25



def random_scale_2():
    testfor_num = 1
    base = random.random()
    output = 1
    baseline = 0
    testfor_num = testfor_num/10
    def random_scale_short(base,testfor_num,output):
        while True:
            if base <= testfor_num:
                output = output*0.8
                testfor_num = testfor_num/10
            else:
                return output
    def random_scale_tall(base,testfor_num,output,baseline):
        while True:
            if base >= baseline+testfor_num*9:
                baseline = baseline+testfor_num*9
                output = output*1.25
                testfor_num = testfor_num/10
            else:
                return output

    if base <= testfor_num:
        return random_scale_short(base,testfor_num,output)
                #0+0.1  next is 0.9 + 0.1        #0+0.9  next needs to be 0.9+ 0.09
    if base > baseline+testfor_num and base < baseline+testfor_num*9:
        return output
    if base >= baseline+testfor_num*9:
        return random_scale_tall(base,testfor_num,output,baseline)

def random_scale_3(base_multiplier=1):
    testfor_num = 1
    base = (random.random()//0.001)/1000
    output = 1
    baseline = 0
    testfor_num = testfor_num/10
    def random_scale_short(base,testfor_num,output):
        while True:
            if base <= testfor_num:
                output = output*0.8
            elif base <= testfor_num*2:
                output = output*0.84
                return output
            elif base <= testfor_num*4:
                output = output*0.88
                return output
            elif base <= testfor_num*6:
                output = output*0.92
                return output
            elif base <= testfor_num*8:
                output = output*0.96
                return output
            else:
                return output
            testfor_num = testfor_num/10

    def random_scale_average(base,testfor_num,output,baseline):
        change_scale = 1
        for i in range(2):
            if base >= baseline+testfor_num*8:
                #output = output*(1+change_scale*0.1)
                output = output*1.1
                baseline = baseline+testfor_num*8
            elif base >= baseline+testfor_num*6:
                output = output*1.05
                baseline = baseline+testfor_num*6
            elif base >= baseline+testfor_num*4:
                output = output
                baseline = baseline+testfor_num*4
            elif base >= baseline+testfor_num*2:
                output = output*0.96
                baseline = baseline+testfor_num*2
            elif base >= 0:
                output = output*0.92
            testfor_num= testfor_num/10
            change_scale = change_scale/10
        return (output//0.001)/1000

    def random_scale_tall(base,testfor_num,output,baseline):
        while True:
            if base >= baseline+testfor_num*9:
                baseline = baseline+testfor_num*9
                output = output*1.25
            elif base >= baseline+testfor_num*8:
                output = output*1.20
                return output
            elif base >= baseline+testfor_num*6:
                output = output*1.15
                return output
            elif base >= baseline+testfor_num*4:
                output = output*1.10
                return output
            elif base >= baseline+testfor_num*2:
                output = output*1.05
                return output
            else:
                return output
            testfor_num = testfor_num/10

    if base <= testfor_num:
        return base_multiplier*((random_scale_short(base,testfor_num,output)//0.001)/1000)
                #0+0.1  next is 0.9 + 0.1        #0+0.9  next needs to be 0.9+ 0.09
    if base > baseline+testfor_num and base < baseline+testfor_num*9:
        return base_multiplier*(random_scale_average(base,testfor_num,output,baseline))
    if base >= baseline+testfor_num*9:
        return base_multiplier*((random_scale_tall(base,testfor_num,output,baseline)//0.001)/1000)


        #function tall, this loops in itself until it doesnt pass the if statment of  base >= testfor_num*9 and also change testfor_num everytime
        #function short

#if you set a init variable to something when an object is being defined, does it redefine that variable?

#we want a party system that contains entities, then we want to iterate through all entities for moves until all all entities are gone from one party

class party():
    def __init__(self,entities:list):
        self.entities = entities



#define player
player_1 = Human(level=1, is_player = True)
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
        
        for i in all_entities:
            party_1_attacking = i in party_1.entities
            if party_1_attacking:
                target = party_2.entities[random.randrange(len(party_2.entities))]
                target.Dexterity_Check(i.Random_Attack_Damage)
                #target.health = target.health - i.Random_Attack_Damage()
                print(str(target.type)+" "+str(target.health))
                if target.health <= 0:
                    all_entities,party_2 = player_died(target,all_entities,party_2)
            else:
                target = party_1.entities[random.randrange(len(party_1.entities))]
                target.Dexterity_Check(i.Random_Attack_Damage)
                #target.health = target.health - i.Random_Attack_Damage()
                print(str(target.type)+" "+str(target.health))
                if target.health <= 0:
                    all_entities,party_1 = player_died(target,all_entities,party_1)
            if len(party_1.entities) == 0:
                print("Party 1 has lost")
                return "Party 2 wins"
            elif len(party_2.entities) == 0:
                print("Party 2 has lost")
                return "Party 1 wins"
        #if player modul, after the automation
        #actor
        #target

        #random target of opposite party


def random_battle_goblin(party_1):
    #sets goblin to a party and in all_entities list

    #this is a problem, everytime I rerun the function the same dead entity is used.
    entity_one = goblin(level=random.randint(1,3))
    entity_two = goblin(level=random.randint(1,3))
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
        #input in entity type = player

if __name__ == "__main__":
    main()
