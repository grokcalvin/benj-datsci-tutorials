import time
import random

class Party():
    def __init__(self,entities:list):
        self.entities = entities

def dice_roll(sides):
    return random.randint(1,sides)

def entity_died(target,party,loot_pool):
    if target.health <= 0:

        loot_pool.add_items(target.Inventory)
        loot_pool.add(target.weapon)
        loot_pool.add(target.armor)
        #if the player has nothing in there inventory it will error

        party.entities = [p for p in party.entities if p != target]
    
    return party

class battle():
    def __init__(party1:Party,party2:Party) -> None:
        Turn_Over = False

    def battle(self,party1,party2,loot_pool):
        def party_attack_party(self,attacking_party,targeted_party,loot_pool):
            for attacking_enitity in attacking_party.entities:
                #this checks if the entity is dead so it doesnt attack after death if the entity isnt out of the list.
                if attacking_enitity.health > 0:
                    time.sleep(3)
                    

                #this block lets the current player in the party select which entity from the opposite party to attack.
                    if attacking_enitity.is_player:
                        self.Turn_Over = False
                        while self.Turn_Over == False:
                            print("{attacking_entity.name} you can:\nSelect Target\nInventory\nObserve\nor\nRun")
                            move_type = input(":")
                            try:
                                if move_type == "Select Target":
                                    valid_input = False
                                    while valid_input == False:
                                        print(f"\nYour targets are:")
                                        for n,i in enumerate(targeted_party.entities):
                                            time.sleep(1)
                                            print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                                        try:
                                            target_index = int(input("enter the number of the target you want to attack:"))
                                            target = targeted_party.entities[target_index]
                                            print("found target, turning Turn_Over to True")
                                            self.Turn_Over = True
                                        except:
                                            print("invalid input, try again.")
                                        else:
                                            valid_input = True
                                            print("\n") 
                                if move_type == "Inventory":
                                    attacking_enitity.Inventory.open(Inventory_Type=self)
                            except:
                                print("invalid input try again.")

                #this selects and random target from the opposite party. This is used for none player enitiies
                    else:
                        if len(targeted_party.entities) != 0:
                            target = targeted_party.entities[random.randrange(len(targeted_party.entities))]
                        else:
                            print("Party has lost")
                            return True


                #this block gets the base attack and attack type based on which move the player selects
                    if attacking_enitity.is_player:
                        valid_input = False
                        while not valid_input:
                            print("enter the attack you would like to do (e.g:front kick):")
                            for n, move in enumerate(attacking_enitity.move_list):
                                print(f"({n}) - {move.value}")
                            try:
                                print("\n")
                                base_attack,attack_type = attacking_enitity.choose_attack()
                                valid_input = True
                            except:
                                print("\ninvalid input, try again")

                #this selects a random attack for the selected entity if they are not a player.
                    else:
                        base_attack,attack_type = attacking_enitity.random_attack()

                #this next block performs the attack on the targeted entity
                    print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} tries {attack_type}")

                    dodge = target.dexterity_check(attacker_dexterity=attacking_enitity.dexterity)
                    attack_role = dice_roll(20)

                    print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} {attacking_enitity.strength} strength + roles ({attack_role})/2   base damage {base_attack }")
                    
                    if dodge and attack_role != 20:
                        print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name}")
                    else:
                        if attack_role == 1:
                            print(f"Critical Failure! {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} missed!")
                        elif attack_role == 20:
                            attack = base_attack*(30+attacking_enitity.strength)
                            actual_damage = target.take_attack(attack)
                            print(f"Critcal Attack {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                            if target.armor is not None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.default_defence))
                            print(f"attacking_enitity does {actual_damage} actual damage")
                            print(f"target is at {target.health}HP")
                        elif attack_role > 1 and attack_role < 20:

                            attack = (base_attack*(attacking_enitity.strength)+(base_attack*attack_role/2))
                            actual_damage = target.take_attack(attack)
                            print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} for {attack} before defence")
                            if target.armor is not None:
                                print(f"armor absorbs {target.armor.damage_absorption}")
                            print("fitness absorption is "+ str(target.default_defence))
                            print(f"attacking_enitity does {actual_damage} actual damage after damage")
                            print(f"target is at {target.health}HP")
                    print("\n")
                    if target.health <= 0:
                        print(f"{target.race}:{target.name} {target.last_name} has died.")
                        targeted_party = entity_died(target,targeted_party,loot_pool)

                    #this line might add targeted party to attacking party
                    all_entities = []
            
            if len(targeted_party.entities) == 0:
                loot_pool.print_inventory()
                return True

        #defined party and all entities list happens before this

        #parties are defines in the parent function

        #for e in all_entities:
        #    if e in party_2.entities:
        #        e.health = 1
        parties = [party_1,party_2]
        Victory = False
        while len(party_1.entities) != 0 and len(party_2.entities) != 0 and not Victory:
            for selected_party in parties:
                if parties.index(selected_party) == 0:
                    Victory = party_attack_party(parties[0],parties[1],loot_pool)
                    if Victory:
                        print("party 1 wins!")
                        break
                elif parties.index(selected_party) == 1:
                    Victory = party_attack_party(parties[1],parties[0],loot_pool)
                    if Victory:
                        print("party 2 wins!")
                        break
                #round end effects.
            try:
                for entity in party_1.entities:
                    entity.round_over()
            except:
                pass
            try:
                for entity in party_2.entities:
                    entity.round_over()
            except:
                pass    


def battlev0_1(party_1:Party,party_2:Party,loot_pool):
    def party_attack_party(attacking_party,targeted_party,loot_pool):
        for attacking_enitity in attacking_party.entities:
            #this checks if the entity is dead so it doesnt attack after death if the entity isnt out of the list.
            if attacking_enitity.health > 0:
                time.sleep(3)
                

            #this block lets the current player in the party select which entity from the opposite party to attack.
                if attacking_enitity.is_player:
                    valid_input = False
                    while valid_input == False:
                        print(f"\nYour targets are:")
                        for n,i in enumerate(targeted_party.entities):
                            time.sleep(1)
                            print(f"({n}) - {i.race}:{i.name} {i.last_name} HP:{i.health}")
                        try:
                            target_index = int(input("enter the number of the target you want to attack:"))
                            target = targeted_party.entities[target_index]
                        except:
                            print("invalid input, try again.")
                        else:
                            valid_input = True
                        print("\n")

            #this selects and random target from the opposite party. This is used for none player enitiies
                else:
                    if len(targeted_party.entities) != 0:
                        target = targeted_party.entities[random.randrange(len(targeted_party.entities))]
                    else:
                        print("Party has lost")
                        return True


            #this block gets the base attack and attack type based on which move the player selects
                if attacking_enitity.is_player:
                    valid_input = False
                    while not valid_input:
                        print("enter the attack you would like to do (e.g:front kick):")
                        for n, move in enumerate(attacking_enitity.move_list):
                            print(f"({n}) - {move.value}")
                        try:
                            print("\n")
                            base_attack,attack_type = attacking_enitity.choose_attack()
                            valid_input = True
                        except:
                            print("\ninvalid input, try again")

            #this selects a random attack for the selected entity if they are not a player.
                else:
                    base_attack,attack_type = attacking_enitity.random_attack()

            #this next block performs the attack on the targeted entity
                print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} tries {attack_type}")

                dodge = target.dexterity_check(attacker_dexterity=attacking_enitity.dexterity)
                attack_role = dice_roll(20)

                print(f"{attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} {attacking_enitity.strength} strength + roles ({attack_role})/2   base damage {base_attack }")
                
                if dodge and attack_role != 20:
                    print(f"{target.race}:{target.name} {target.last_name} dodged attack from {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name}")
                else:
                    if attack_role == 1:
                        print(f"Critical Failure! {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} missed!")
                    elif attack_role == 20:
                        attack = base_attack*(30+attacking_enitity.strength)
                        actual_damage = target.take_attack(attack)
                        print(f"Critcal Attack {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} does X3 damage to {target.race}:{target.name} {target.last_name} for a total of {attack} before defence")
                        if target.armor is not None:
                            print(f"armor absorbs {target.armor.damage_absorption}")
                        print("fitness absorption is "+ str(target.default_defence))
                        print(f"attacking_enitity does {actual_damage} actual damage")
                        print(f"target is at {target.health}HP")
                    elif attack_role > 1 and attack_role < 20:

                        attack = (base_attack*(attacking_enitity.strength)+(base_attack*attack_role/2))
                        actual_damage = target.take_attack(attack)
                        print(f"{target.race}:{target.name} {target.last_name} gets hit with {attack_type} by {attacking_enitity.race}:{attacking_enitity.name} {attacking_enitity.last_name} for {attack} before defence")
                        if target.armor is not None:
                            print(f"armor absorbs {target.armor.damage_absorption}")
                        print("fitness absorption is "+ str(target.default_defence))
                        print(f"attacking_enitity does {actual_damage} actual damage after damage")
                        print(f"target is at {target.health}HP")
                print("\n")
                if target.health <= 0:
                    print(f"{target.race}:{target.name} {target.last_name} has died.")
                    targeted_party = entity_died(target,targeted_party,loot_pool)

                #this line might add targeted party to attacking party
                all_entities = []
        
        if len(targeted_party.entities) == 0:
            loot_pool.print_inventory()
            return True

    #defined party and all entities list happens before this

    #parties are defines in the parent function

    #for e in all_entities:
    #    if e in party_2.entities:
    #        e.health = 1
    parties = [party_1,party_2]
    Victory = False
    while len(party_1.entities) != 0 and len(party_2.entities) != 0 and not Victory:
        for selected_party in parties:
            if parties.index(selected_party) == 0:
                Victory = party_attack_party(parties[0],parties[1],loot_pool)
                if Victory:
                    print("party 1 wins!")
                    break
            elif parties.index(selected_party) == 1:
                Victory = party_attack_party(parties[1],parties[0],loot_pool)
                if Victory:
                    print("party 2 wins!")
                    break
            #round end effects.
        try:
            for entity in party_1.entities:
                entity.round_over()
        except:
            pass
        try:
            for entity in party_2.entities:
                entity.round_over()
        except:
            pass