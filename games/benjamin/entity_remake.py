from entity_class_Dec_2_2022 import random_scale_3
from dataclasses import dataclass

@dataclass
class EntityFramework:
    type : str

    leg_length : float
    torso_height : float
    arm_length : float
    size : float
    #need to deep copy when you input new values
    move_dict : dict
    #moves have directories that decid how the math works

    level : int
    Level_Up_Points : int

    strength : int
    constitution :int
    dexterity :int

    wisdom :int
    intelligents :int
    charsima :int


    is_player : bool = False

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
human_1 = spawn_human(10)

print(human_1.size)