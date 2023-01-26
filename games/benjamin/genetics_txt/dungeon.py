import random
class Room:
    def __init__(self,up=None,down=None,left=None,right=None) -> None:
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.texture = "[ ]"

        self.coming_from_value = None

        self.room = None

    def __str__(self):
        return self.texture
    
    def room_gen(self):
        pass

#array and snake
class land_chunk:
    def __init__(self,x=10,y=10) -> None:
        y_strips = []
        for y1 in range(y):
            x_strip = []
            for x1 in range(x):
                new_room = Room()
                x_strip.append(new_room)
            y_strips.append(x_strip)
        self.area = y_strips
        self.x_max_index = x -1
        self.y_max_index = y -1


#import land chunk, have 4 tile values that bring you to the next room
#[^],[!],[<],[>]
#spawn area based on "coming from value"
#main map, then moving around, global, each tile has a area 
#each room has random selection from tool based on its left, right, up, down values

# way to make rooms by moving around and typing a texture input to replace tile then enetering "done" to make map



def print_area(area:land_chunk,player_pos_x=None,player_pos_y=None):
    print_y_strips = ""
    for yy in range(len(area.area)):
        print_x_strip = ""
        for xx in range(len(area.area[yy])):
            if xx == player_pos_x and yy == player_pos_y:
                print_x_strip = print_x_strip + "[P]"
            else:
                print_x_strip = print_x_strip + area.area[yy][xx].texture
        print_y_strips = print_y_strips + print_x_strip + "\n"
    print(print_y_strips)

class snake_room_gen:
    def __init__(self) -> None:
        self.index_X = 0
        self.index_Y = 0

    def center(self,area:land_chunk):
        x_index = (area.x_max_index)/2
        self.index_X = int(x_index//1)
        y_index = (area.y_max_index)/2
        self.index_Y = int(y_index//1)

    def snake(self,area:land_chunk,moves,amount_of_snakes) -> land_chunk:

        while amount_of_snakes > 0:
            print("snake spawned")
            temp_x_index = self.index_X
            temp_y_index = self.index_Y
            temp_moves_left = moves
            print(temp_x_index)
            print(temp_y_index)
            while temp_moves_left > 0:
                possible_moves = []
                if not temp_y_index == 0:
                    possible_moves.append("Up")
                if not temp_y_index == area.y_max_index:
                    possible_moves.append("Down")   
                if not temp_x_index == 0:
                    possible_moves.append("Left")
                if not temp_x_index == area.x_max_index:
                    possible_moves.append("Right")
                
                new_move = possible_moves[(random.randint(0,len(possible_moves)-1))]

                if new_move == "Up":
                    temp_y_index -= 1
                    area.area[temp_y_index][temp_x_index].texture = "[#]"
                if new_move == "Down":
                    temp_y_index += 1
                    area.area[temp_y_index][temp_x_index].texture = "[#]"
                if new_move == "Left":
                    temp_x_index -= 1
                    area.area[temp_y_index][temp_x_index].texture = "[#]"
                if new_move == "Right":
                    temp_x_index += 1
                    area.area[temp_y_index][temp_x_index].texture = "[#]"
                temp_moves_left -= 1
            amount_of_snakes -= 1
        return area

def connect_rooms(area):
    new_area = []
    for yy in range(len(area.area)):
        for xx in range(len(area.area[0])):
            nearby_rooms = []
            nearby_blocks = []
            if not yy == 0:
                nearby_blocks.append("Up")
            if not yy == area.y_max_index:
                nearby_blocks.append("Down")   
            if not xx == 0:
                nearby_blocks.append("Left")
            if not xx == area.x_max_index:
                nearby_blocks.append("Right")

            #this needs to be selected from possilities of rooms nearby
            if "Up" in nearby_blocks:
                if area.area[yy-1][xx].texture == "[#]":
                    nearby_rooms.append("Up")
            if "Down" in nearby_blocks:
                if area.area[yy+1][xx].texture == "[#]":
                    nearby_rooms.append("Down")
            if "Left" in nearby_blocks:
                if area.area[yy][xx-1].texture == "[#]":
                    nearby_rooms.append("Up")
            if "Right" in nearby_blocks:
                if area.area[yy][xx+1].texture == "[#]":
                    nearby_rooms.append("Right")

            if len(nearby_rooms) > 0:
                number_of_connects = random.randint(1,len(nearby_rooms))
                while number_of_connects > 0:
                    random_index = random.randint(1,len(nearby_rooms))
                    random_room_to_connect = nearby_rooms[random_index]
                    if random_room_to_connect == "Up":
                        area.area[yy-1][xx].down = True
                    if random_room_to_connect == "Up":
                        area.area[yy+1][xx].up = True
                    if random_room_to_connect == "Up":
                        area.area[yy][xx-1].right = True
                    if random_room_to_connect == "Up":
                        area.area[yy][xx+1].left = True

                    del(nearby_rooms[random_index])
                    number_of_connects -= 1

land = land_chunk(x=30,y=30)
print_area(land)

snake_1 = snake_room_gen()
snake_1.center(land)
land = snake_1.snake(land,45,3)
print_area(land)
