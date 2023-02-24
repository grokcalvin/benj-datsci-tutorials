from base_entity import BaseHumanoidEntity, random_scale

def spawn_human(Level,is_player=False):
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

def spawn_goblin(Level,is_player=False):
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

def spawn_elf(Level,is_player=False):
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