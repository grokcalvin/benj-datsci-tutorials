import random
import math
from dataclasses import dataclass


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

class EntityStats:
    def __init__(self,
        type: str,
        leg_length: int,
        torso_height: int,
        arm_length: int,
        size: int,
        move_dict: dict,
        level: int,
        strength: int,
        constitution: int,
        dexterity: int,
        wisdom: int,
        intelligents: int,
        charsima: int,
        is_player: bool = False
        ) -> None:

        self.type = type
        self.leg_length = leg_length
        self.torso_height = torso_height
        self.arm_length = arm_length
        self.size = size
        self.move_dict = move_dict
        self.level = level
        self.strength = strength
        self.constitution = constitution
        self.dexterity = dexterity
        self.wisdom = wisdom
        self.intelligents = intelligents
        self.charsima = charsima
        self.is_player = is_player

        for _ in range(self.level-1):
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
            
        self.max_health = (((self.leg_length**2+self.arm_length**2+self.torso_height**2)/3)*self.size**2)*(70+(10*self.constitution))//0.001/1000
        self.health = self.max_health


def make_human(level: int, is_player: bool = False):
    entity = EntityStats(
        is_player = is_player,
        type="human",
        leg_length=random_scale_3(),
        torso_height=random_scale_3(),
        arm_length = random_scale_3(),
        size = random_scale_3(),
        move_dict = {"front_kick":{"Xp":0,"Level":1}},
        level = level,
        strength = 2,
        constitution = 2,
        dexterity = 2,
        wisdom = 2,
        intelligents = 2,
        charsima = 2,
    )
    return entity

def make_goblin(level: int, is_player: bool = False):
    entity = EntityStats(
        is_player = is_player,
        type = "goblin",
        leg_length = random_scale_3(base_multiplier=0.7),
        torso_height = random_scale_3(base_multiplier=1),
        arm_length = random_scale_3(base_multiplier=0.9),
        size = random_scale_3(base_multiplier=0.55),
        move_dict = {"front_kick":{"Xp":0,"Level":1}},
        level = level,
        strength = 4,
        constitution = 2,
        dexterity = 4,
        wisdom = 1,
        intelligents = 2,
        charsima = 1
        )
    return entity


def make_elf(level: int, is_player: bool = False):
    entity = EntityStats(
        is_player = is_player,
        type = "elf",
        leg_length = random_scale_3(base_multiplier=1.1),
        torso_height = random_scale_3(base_multiplier=1),
        arm_length = random_scale_3(base_multiplier=1),
        size =random_scale_3(base_multiplier=1),
        move_dict = {"front_kick":{"Xp":0,"Level":1}},
        level = level,
        strength = 2,
        constitution = 2,
        dexterity = 3,
        wisdom = 2,
        intelligents = 3,
        charsima = 1
        )
    return entity


def main():
    human = make_human(level=3, is_player=True)
    print(human.type)
    print(human.max_health)
    goblin = make_goblin(level=3)
    print(goblin.type)
    print(goblin.max_health)
    elf = make_elf(level=2)
    print(elf.type)
    print(elf.max_health)


if __name__ == '__main__':
    main()