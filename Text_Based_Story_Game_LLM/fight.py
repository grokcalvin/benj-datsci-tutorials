import random
import Action_LM
import Inventory
#1
#[ Done ] - damage for onstitution and how low of health they have
#[ Done ] show all moves and requirements
#[ Done ] filter moves dependent on if has item and ammo
#[ Done ] smart move choosing 
#[ Done ] Loop until pass or no available moves
#[ DONE ] target selectiona
#[ Done ] make into function
#[ Done ] add movement penlty
#[ Done ] Add death delelte pile
#[ Done ] Add Loot pile
#[ Done ] add loot pickup if is controlled by player

#[ Done ] Combat 1.0 

#2
#[  ] blunt weapons chance to knockout based on damage done

class dice():
    def __init__(self,sides):
        self.sides = sides
    def roll(self):
        return random.randint(1,self.sides+1)
    
class move():
    def __init__(self,name="example move",dice=[],required_movement=10,atr_mod="dex",req_item=None,req_ammo=None,movement_penlty=2):
        self.name = name
        self.dice = dice
        self.required_movement = required_movement
        self.atr_mod = atr_mod
        self.req_item = req_item
        self.req_ammo = req_ammo
        self.movement_penlty = movement_penlty
        self.rounds_until_pently_removal = 0

    def get_total_damage(self,parent_character):
        total_damage = 0
        for i in self.dice:
            total_damage += i.roll
        
        bonus_atr_points = 0
        if self.atr_mod == "dex":
            bonus_atr_points += (2//(parent_character.stats.dexterity-10))
        total_damage + 5* bonus_atr_points

    def calculate_total_required_movement(self):
        if self.rounds_until_pently_removal > 0:
            return self.required_movement+self.movement_penlty
        else:
            return self.required_movement
        
def fight(group1,group2):
    def available_moves(character):
        available_moves = []
        available_moves_2 = []
        for i in character.move_list:
            if i.calculate_total_required_movement() >= character.movement:
                available_moves.append(i)

        compare_list = []
        for i in character.inventory:
            compare_list.append(i.name)

        for i in available_moves:
            if i.req_item:
                if i.req_item in compare_list:
                    if i.req_ammo:
                        if i.req_ammo in compare_list:
                            available_moves_2.append(i)
                    else:
                        available_moves_2.append(i)
            else:
                available_moves_2.append(i)
        return available_moves_2

    def smart_move_selection(character):
        start_str = "all moves unlocked:\n"
        full_str = character.print_move()
        full_str = start_str+full_str + f"Your current movement available {str(character.movement)}"
        SYT_PROMPT = "You are acting on behalf of a NPC in a battle, trying to make the best move. There is a certain movement required for every move. Your movement is capped at 30. Simply reply with the move name"
        Valid_Input = False
        name_list = []
        for i in character.moves:
            name_list.append(i)
        while Valid_Input == False:
            move_name = Action_LM.If_Text("",full_str,SYT_PROMPT=SYT_PROMPT,non_linear=True)
            if move_name in name_list:
                Valid_Input = True
        return move_name
    def group_attack_group(attacking_group,defending_group,Loot_Pile):
        for i in attacking_group:
            i.movement = i.stats.dexerity
        for char in attacking_group:
            Valid_Input = False
            for move in char.moves:
                if move.rounds_until_pently_removal > 0:
                    move.rounds_until_pently_removal -= 1
            if char.is_player_controlled:
                print("Select target:")
                full_str = ""
                index = 1
                for i in defending_group:
                    full_str = full_str + f"({index}) {i.name} hp {i.hp} - armor {i.armor}\n"
                    index += 1
                print(full_str)

                #while Valid_Input == False:
            else:
                target = defending_group[random.randint(1,len(defending_group)+1)]

            #is this character is controlled by player then do this
            pass_turn = False
            while available_moves(char) and not pass_turn:
                if char.is_player_controlled:
                    Valid_Input = False
                    while Valid_Input == False:
                        print(char.print_moves()+"\n")
                        selcted_move = input("What move will you use?: ")
                        if selected_move == "pass":
                            pass_turn = True
                            break
                        try:
                            selcted_move = int(selected_move)
                            try:
                                selected_move = char.move_list[selcted_move-1]
                                if char.movement >= selected_move.calculate_total_required_movement:

                                    if selected_move.req_item:
                                        compare_list = []
                                        for item in char.inventory:
                                            compare_list.append(item.name)

                                        if selected_move.req_item in compare_list:
                                            if selected_move.req_ammo:
                                                if selected_move.req_ammo in compare_list:
                                                    Valid_Input = True
                                                else:
                                                    print("you dont have enough ammo for this move")
                                            Valid_Input = True
                                        else:
                                            print(f"you need a specific item to use this move")
                                    else:
                                        Valid_Input = True
                                else:
                                    print("not enough movement")
                            except:
                                print(f"invalid index, no move is assigned to '{selcted_move}'")
                        except:
                            print("invalid input - value needs to be just numbers.")

                else:
                    Valid_Input = False
                    available_moves_list = available_moves(char)
                    index = 0
                    while Valid_Input == False:
                        selected_move=smart_move_selection(char)
                        if selected_move in available_moves_list:
                            Valid_Input = True
                        elif index > 3:
                            selected_move = available_moves_list[random.randint(0,len(available_moves_list))]
                        else:
                            index += 1
            if pass_turn == False:
                starting_damage = selected_move.get_total_damage(char)
                selected_move.rounds_until_pently_removal = 3

                target_constitution_bonus = (2//target.stats.constitution-10)
                health_defense_bonus = (10//(100-target.hp))
                damage_reduction = (target.armor + (target_constitution_bonus*3)+health_defense_bonus)
                total_damage = starting_damage-damage_reduction
                if total_damage > 0:
                        target.hp -= total_damage
                if target.hp <= 0:
                    name_list = []
                    for i in defending_group:
                        name_list.append(i.name)
                    index_name = name_list.index(target.name)
                    Loot_Pile.add_items(target.inventory)
                    del defending_group[index_name]
                if total_damage > 0 and target.hp > 0:
                        item_type = char.inventory.get_item_copy_by_name(selected_move.req_item).type
                        if item_type == "weapon blunt":
                            hits = random.randint(0,1)
                            if hits:
                                knockout_chance = total_damage*2
                                percent = random.randint(1,100)
                                if knockout_chance >= percent:

                                    # effect statud effects every round of combat


                                    target.add_status_effect("knocked_out",game=game)


    def Surviving_Group_Loots(group,loot):
        for i in group:
            if i.is_player_controlled:
                selected_item = ""
                while selected_item != "done" and loot.items:
                    print("Loot Pile")
                    loot.print_inventory()
                    selected_item = input("\ntype the number of the item you want to grab or type 'done' to exit looting mode:")
                    if selected_item != "done":
                        try:
                            selected_item = int(selected_item)
                            i.inventory.add(loot.items[selected_item-1])
                        except:
                            print("invalid input, only numbers or 'done'")
                break

    #round start
    Loot_Pile = Inventory.Inventory()
    while group1 and group2:
        for char in group1+group2:
            char.status_effect_effect("combat round")
        group_attack_group(group1,group2,Loot_Pile)
        group_attack_group(group2,group1,Loot_Pile)

    if group1:
        Surviving_Group_Loots(group1,Loot_Pile)
    elif group2:
        Surviving_Group_Loots(group2,Loot_Pile)


            #move base attack, attack modifier
            #dice for damage

            #how to make choices AI selects moves not target
            #can only attack oppoents use whole object to index