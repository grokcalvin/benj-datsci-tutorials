import random
import os
import time
import keyboard
import copy

map_item = ["🟩","🟥","🔥","💢","💕"]
player_skin = "🙂"
player_X = 0
player_Y = 0
Map_X, Map_Y = (0,0)
#item pickup - 

print('practicing merging')

class player_object():
    hp = 20
    upper_body_strength = 1
    lower_body_strength = 1
    Damage = 3

class globlin_object():
    hp = 10
    damage = 1
    name = "goblin"

class speedy_object():
    hp = 15
    damage = 1
    name = "speedy boi"

class brute_object():
    hp = 20
    damage = 2
    name = "brute"

def Map_gen(x,y,map_background="🟩"):
    #this runs for every Y level
    map_original = []
    for aaa in range(y):
        Y_layer = []
        for aaaaa in range(x):
            random_texture = random.randint(1,100)
            if random_texture <90:
                Y_layer.append([map_background])
            elif random_texture >=90 and random_texture < 95:
                Y_layer.append([map_item[1]])
            elif random_texture >=95 and random_texture < 97:
                Y_layer.append([map_item[2]])
            elif random_texture >=97 and random_texture < 101:
                Y_layer.append([map_item[3]])
        map_original.append(Y_layer)
    global Map_X, Map_Y
    Map_X = x
    Map_Y = y
    return map_original

def print_map(Map):
    print_map_string = ""
    for xxx in range(len(Map)):
        Strip = ""
        for x in range(len(Map[player_Y])):
            Strip += Map[xxx][x][0]
        Strip += "\n"
        print_map_string += Strip
    print(print_map_string)

def render_player():
    new_map[player_Y][player_X] = [player_skin]

def random_battle():
    #right now the original class methods get updated when opponent gets updated, enabling no replay ablity for any enemy types
    random_draw = random.randint(1,10)
    if random_draw >=1 and random_draw < 8:
        opponent = copy.deepcopy(globlin_object)
    if random_draw >=8 and random_draw < 10:
        opponent = copy.deepcopy(speedy_object)
    if random_draw == 10:
        opponent = copy.deepcopy(brute_object)
    print("you have entered battle agaist a {}".format(opponent.name))
    run = False
    global opponent_health
    opponent_health = opponent.hp
    while player_1.hp > 0 and opponent.hp >0 and run == False:
        input1 = input("what will you do?\n-=attack=-\n-=run=-\n")
        if input1 == "attack":
            P_D = round((player_1.Damage*0.1*random.randint(1,20)),1)
            opponent.hp -= P_D
            print("you did {} damage, the {} is at {}Hp".format(P_D,opponent.name,opponent.hp))
        if input1 == "run":
            print("you decide to run!")
        if opponent.hp < 0:
            print("you won!{} is beaten.".format(opponent.name))
        if player_1.hp < 0:
            print("you lost to a {}.\nGAME OVER".format(opponent.name))

player_1 = player_object

original_map = Map_gen(21,21)
new_map = copy.deepcopy(original_map)
render_player()
#print(original_map[player_Y])

print_map(new_map)

input1 = ""
while input1 != "end":
    time.sleep(0.5)
    os.system("clear")
    opponent_health = globlin_object.hp
    print(opponent_health)
    print(str(player_Y))
    print(str(player_X)+"\n")


    print_map(new_map)  
    moved = False
    if keyboard.is_pressed("w"):
        player_Y -=1
        moved = True
    if keyboard.is_pressed("a"):
        player_X -=1
        moved = True
    if keyboard.is_pressed("s"):
        player_Y +=1
        moved = True
    if keyboard.is_pressed("d"):
        player_X +=1
        moved = True

#bug where if you try to go out of border
    if player_Y < 0:
        player_Y = 0
        print("out of world border_-Y")
        moved = False
    if player_Y >= Map_Y:
        player_Y = Map_Y -1
        print("out of world border_Y+")
        print("Map Y"+str(Map_Y))
        moved = False
    if player_X < 0:
        player_X = 0
        print("out of world border_X-")
        moved = False
    if player_X >= Map_X:
        player_X = Map_X -1
        print("out of world border_X+")
        print("Map X"+str(Map_X))
        print(player_X)
        moved = False

    if original_map[player_Y][player_X] == ["🟥"]:
        print("function red")
    if original_map[player_Y][player_X] == ["🔥"]:
        print("function fire")
    if original_map[player_Y][player_X] == ["💢"]:
        random_battle()
        original_map[player_Y][player_X] = [map_item[0]]
    if original_map[player_Y][player_X] == ["💕"]:
        print("function medkit")
#maybe have all characters be lists with one chacter then break them down on a paste of map, enables better data grabbing

    new_map = copy.deepcopy(original_map)
    render_player()

