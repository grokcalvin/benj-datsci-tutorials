class move_class():
    def __init__(self,move_type) -> None:
        self.move = move_type

        self.level = 1
        self.xp = 0
        self.next_level_xp = 50

        if move_type == "front kick":
            #legs and core
            self.muscle_group = "lower_body"
            self.level_multiplier = 0.3
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == "forward gab":
            self.muscle_group = "arms_and_chest"
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 0.7
            self.weapon = None

        if move_type == "upper cut":
            self.muscle_group = "arms_and_chest"
            self.level_multiplier = 0.2
            #the base damage used for the move
            self.move_root = 1
            self.weapon = None

        if move_type == "slash":
            self.muscle_group = "arms_and_chest_and_core"
            self.level_multiplier = 0.1
            #the base damage used for the move
            self.move_root = 0.1
            self.weapon = "Sword"

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



        if self.muscle_group == "arms":
            Damage_Factor = (parent.size**2)*(parent.arm_length**2)*parent.arm_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == "chest":
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*parent.chest_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == "core":
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*parent.core_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        if self.muscle_group == "legs":
            Damage_Factor = (parent.size**2)*(parent.leg_length**2)*parent.leg_muscle_group*self.move_root*(1+self.level_multiplier*(self.level-1))*weapon_bonus

        #have a slice move or varaitions that use a weapon object as a multiplier

        if self.muscle_group == "arms_and_chest":
            Damage_Factor = (parent.size**2)*((parent.arm_length**2)*(parent.torso_height**2)/2)*((parent.arm_muscle_group+parent.chest_muscle_group)/2)*self.move_root*(1+self.level_multiplier*(self.level-1))

        if self.muscle_group == "arms_and_chest_and_core":
            Damage_Factor = (parent.size**2)*(parent.torso_height**2)*((parent.arm_muscle_group+parent.chest_muscle_group+parent.core_muscle_group)/3)*self.move_root*(1+self.level_multiplier*(self.level-1))

        if self.muscle_group == "full_body":
            Damage_Factor = (parent.size**2)*((parent.arm_length**2)*(parent.torso_height**2)*(parent.leg_length**2)/3)*((parent.arm_muscle_group+parent.chest_muscle_group+parent.core_muscle_group+parent.leg_muscle_group)/4)*self.move_root*(1+self.level_multiplier*(self.level-1))


        if self.muscle_group == "lower_body":
            Damage_Factor = (parent.size**2)*(parent.leg_length**2)*((parent.core_muscle_group+parent.leg_muscle_group)/2)*self.move_root*(1+self.level_multiplier*(self.level-1))

        self.xp += 10
        if parent.is_player:
            print(f"{self.move} {self.xp}xp/{self.next_level_xp}xp")
        #game setting, show xp gain for all entities
        self.check_for_level_up(parent)

        parent.xp += 10
        parent.check_for_level_up()

        return ((Damage_Factor/1000)//0.1/10)

            #dont foregt xp give functions to mmoves and muscles      

        #function that runs of move set that gives the parent's move_set's object xp, move set xp is ep earned from certain types of moves that work together, martial arts is one, mastery level is added to current level.

        #give xp to parent muscles devided by (parent muscle/1000)**2 so at 10,000 xp it takes 100 times as much xp to gain 1

def main():
    pass

if __name__ == "__main__":
    main()