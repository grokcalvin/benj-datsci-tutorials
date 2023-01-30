from enum import Enum
class Move_Types(Enum):
    FRONT_KICK = "front kick"
    FORWARD_GAB = "foward gab"
    UPPER_CUT = 'upper cut'

    SLASH = "slash"
    STAB = "stab"
    PUNCH = "punch"

    KARATE_FRONT_KICK = "karate front kick"
    KARATE_GAB = "karate gab"
    KARATE_UPPER_CUT = "karate upper cut"
    KARATE_SIDE_KICK = "karate side kick"
    KARATE_FLYING_SIDE_KICK = "karate flying side kick"
    KARATE_POWER_PUNCH = "karate power punch"

class Used_Muscle_Groups(Enum):
    ARMS = "core"
    CHEST = "chest"
    CORE = "core"
    LEGS = "legs"

    ARMS_AND_CHEST = "arms and chest"
    ARMS_CHEST_AND_CORE = "arms and chest and core"
    FULL_BODY = "full body"
    LOWER_BODY = "lower body"

class move_class():
    def __init__(self,move_type) -> None:
        self.move = move_type

        self.level = 1
        self.xp = 0
        self.next_level_xp = 50

        if move_type == Move_Types.FRONT_KICK:
            #legs and core
            self.muscle_group = Used_Muscle_Groups.LOWER_BODY
            self.level_multiplier = 0.3
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.FORWARD_GAB:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 0.7
            self.weapon = None

        if move_type == Move_Types.UPPER_CUT:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.SLASH:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 0.1
            self.weapon = "Sword"

        if move_type == Move_Types.STAB:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.4
            #the base damage used for the move
            self.move_root = 0.75
            self.weapon = "Sword"

        if move_type == Move_Types.PUNCH:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 0.7
            self.weapon = None



        if move_type == Move_Types.KARATE_FRONT_KICK:
            #legs and core
            self.muscle_group = Used_Muscle_Groups.LOWER_BODY
            self.level_multiplier = 0.3
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.KARATE_GAB:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 0.7
            self.weapon = None

        if move_type == Move_Types.KARATE_UPPER_CUT:
            self.muscle_group = Used_Muscle_Groups.ARMS_AND_CHEST
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.KARATE_SIDE_KICK:
            self.muscle_group = Used_Muscle_Groups.LOWER_BODY
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.KARATE_FLYING_SIDE_KICK:
            self.muscle_group = Used_Muscle_Groups.LOWER_BODY
            self.level_multiplier = 0.35
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == Move_Types.KARATE_POWER_PUNCH:
            self.muscle_group = Used_Muscle_Groups.ARMS_CHEST_AND_CORE
            self.level_multiplier = 0.3
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        #Sameri
        #karate
        #ty quand0
        #

    def check_for_level_up(self,parent):
        while self.xp >= self.next_level_xp:
            self.level += 1
            self.next_level_xp = round(self.next_level_xp*1.5,1)

            if parent.is_player:
                print(f"{self.move} is now level {self.level}")

#filter avialable move with self.weapon and self.weapon of move
#skill loot table

    def action(self,parent):
        #increase muscle groups xp +=(xp/((muscle_group//1000)**2)
        #increase move xp
        #test for level up of move
        #on kill of enememy give the killing blow move a percentage of the killed target player the xp if the killing blow move

        weapon_bonus = 1
        if self.weapon != None and parent.weapon != None:
            weapon_bonus = parent.weapon.base_damage



        if self.muscle_group == Used_Muscle_Groups.ARMS:
            Damage_Factor = (parent.size**2)*(parent.arm_length**2)*parent.arm_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == Used_Muscle_Groups.CHEST:
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*parent.chest_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == Used_Muscle_Groups.CORE:
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*parent.core_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == Used_Muscle_Groups.LEGS:
            Damage_Factor = (parent.size**2)*(parent.leg_length**2)*parent.leg_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        #have a slice move or varaitions that use a weapon object as a multiplier

        if self.muscle_group == Used_Muscle_Groups.ARMS_AND_CHEST:
            Damage_Factor = (parent.size**2)*((parent.arm_length**2)*(parent.torso_height**2)/2)*((parent.arm_muscle_group+parent.chest_muscle_group)/2)*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus


        if self.muscle_group == Used_Muscle_Groups.ARMS_CHEST_AND_CORE:
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*((parent.arm_muscle_group+parent.chest_muscle_group+parent.core_muscle_group)/3)*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus


        if self.muscle_group == Used_Muscle_Groups.FULL_BODY:
            Damage_Factor = (parent.size**2)*((parent.arm_length**2)*(parent.torso_height**2)*(parent.leg_length**2)/3)*((parent.arm_muscle_group+parent.chest_muscle_group+parent.core_muscle_group+parent.leg_muscle_group)/4)*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus



        if self.muscle_group == Used_Muscle_Groups.LOWER_BODY:
            Damage_Factor = (parent.size**2)*(parent.leg_length**2)*((parent.core_muscle_group+parent.leg_muscle_group)/2)*self.move_root*(1+self.level_multiplier*(self.level-1))

        self.xp += 10
        if parent.is_player:
            print(f"{self.move} {self.xp}xp/{self.next_level_xp}xp")
        #game setting, show xp gain for all entities
        self.check_for_level_up(parent)

        parent.xp += 10
        parent.check_for_level_up()

        return ((Damage_Factor/1000)//0.1/10)

            #dont foregt xp give functions to moves and muscles      

        #function that runs of move set that gives the parent's move_set's object xp, move set xp is ep earned from certain types of moves that work together, martial arts is one, mastery level is added to current level.

        #give xp to parent muscles devided by (parent muscle/1000)**2 so at 10,000 xp it takes 100 times as much xp to gain 1

def main():
    pass

if __name__ == "__main__":
    main()