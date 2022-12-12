from entity_class_Dec_2_2022 import random_scale_3

class EntityFramework():
    def __intit__(self):
        self.is_player : bool = False
        
        self.type : str

        self.leg_length : float
        self.torso_height : float
        self.arm_length : float
        self.size : float
        #need to deep copy when you input new values
        self.move_dict : dict
        #moves have directories that decid how the math works

        self.level : int
        self.Level_Up_Points : int

        self.strength : int
        self.constitution :int
        self.dexterity :int

        self.wisdom :int
        self.intelligents :int
        self.charsima :int

def spawn_human(Level):
    new_entity = EntityFramework(
        type = "Human",
        leg_length = random_scale_3(),
        torso_height = random_scale_3(),
        arm_length = random_scale_3(),
        size = random_scale_3(),
        level = Level,

        strength = 2,
        constitution = 2,
        dexterity = 2,

        wisdom = 2,
        intelligents = 2,
        charsima = 2,
    )
    return new_entity