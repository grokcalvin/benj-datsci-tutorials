from area import *
from Action_LM import *
from area import item_type, item

class Space_Type():
    def __init__(self,name="Blank",description="default",space_parent=None,space_children=None):
        self.name = name
        self.description = description
        self.parent = space_parent
        self.children = space_children
        

def basic_LM_response(Prompt):


    syt_prompt = "You are a bot assistant, tyring your best to help the user: "
    syt_prompt = [{"role": "user", "content": f"{syt_prompt}"}]

    messages_list = syt_prompt
    messages_list.append({"role": "user", "content": f"{Prompt}"})

    stream = chat(
                model="lexi-story-8k",
                messages=messages_list,
                stream=True
        )

        # Process and save the streamed data
    iter = 10
    response = ""
    for chunk in stream:
        content = chunk["message"]["content"]
        iter -= 1
        check_file = ""
        #create seperate function that returns true/false if int
        with open("On","r") as f:
            check_file = f.read()
        if check_file != "0":
            break
        response += content
    return response

#food, weapons, material, armor
def is_food_category(item):
    prompt = f"is \'{item}\' something that fits into the can/should eat category? simply reply with Y/N"
    return basic_LM_response(prompt)

def create_food_type(item):
    total = 0
    total_inputs = 0
    for i in range(10):
        output = basic_LM_response(f"given a scale of 1-10 how would you rate {food_item} to satify hunger? Simply respond with a number.")
        try:
            total += int(output)
            total_inputs += 1
        except:
            pass
    print(total)
    print(total_inputs)
    mean = total/total_inputs
    new_item = item_type(gain_hp=None,gain_food=int(mean),gain_water=None,gain_armor=None,name=item)
    item_instance = item(name=new_item.type,parent_inventory=None,item_type=new_item,is_stackable=True,quantity=1)
    print(str(item_instance.gain_food)+" "+item_instance.name)
    return new_item

def is_melee_weapon_category(item):
    prompt = f"Is the '{item} item considered an effective melee weapon? Simply reply with Y/N"
    return basic_LM_response(prompt)

def create_melee_weapon_type(item):
    total = 0
    total_inputs = 0
    for i in range(10):
        output = basic_LM_response(f"given a scale of 1-10 how would you rate {item} In terms of damage? Simply respond with a number.")
        try:
            total += int(output)
            total_inputs += 1
        except:
            pass
    print(total)
    print(total_inputs)
    mean = total/total_inputs
    new_item = item_type(damage=(mean),name=item)
    item_instance = item(name=new_item.type,parent_inventory=None,item_type=new_item,is_stackable=False,quantity=1)
    print(str(item_instance.damage)+" "+item_instance.name)
    return new_item
items = ["cake","Soda","knife"]
for unknown_item in items:
    food_test = is_food_category(unknown_item)
    print(food_test+" Y/N?")
    if food_test == "Y":
        new_item = create_food_type(unknown_item)
        print(new_item.type)

area = "bedroom"
get_items_prompt = f"Say generate a list of random yet relevant loot you could find in a {area}. Simply reply with just a list separated using commas."




#raw_list = basic_LM_response(get_items_prompt)
#processed_item_list = raw_list.split(",")
#print(processed_item_list)

def Get_Next_Largest_Division_Of_Space(Space_Name):
    area_name_dict = {}
    for i in range(50):
        raw_anwer = basic_LM_response(f"what is the next largest division of space under a '{Space_Name}' space?. Example - State,County or House, room. Response with just one answer. And just the anwer.")
        if raw_anwer in area_name_dict.keys():
            area_name_dict[raw_anwer] += 1

        else:
            area_name_dict[raw_anwer] = 1

    max_key = max(area_name_dict, key=area_name_dict.get)

        #create dict counter
    print(area_name_dict)
    return max_key

def Get_all_Divisions_Of_Space(Starting_Space,parent=None):
    Child = None
    New_Space_name = Get_Next_Largest_Division_Of_Space(Starting_Space)
    Space_Type_Preset = Space_Type(name=New_Space_name,space_parent=parent,space_children=None)
    if New_Space_name == "Room" or New_Space_name == "room":
        pass
    else:
        Get_all_Divisions_Of_Space(Starting_Space,parent=None)
        Child = Get_all_Divisions_Of_Space(New_Space_name,Space_Type_Preset)
        Space_Type_Preset.children = Child
    return Space_Type_Preset

Space_Object = Get_all_Divisions_Of_Space("State")
iter_space = Space_Object
var = ""
while var != "room" or var != "Room":
    print(iter_space.name)
    iter_space = iter_space.space_children



print(Get_Next_Largest_Division_Of_Space("State"))
#then filter the area types, does this have other areas inside of it? load the different types, then save as an item, with probablities of each item then randomly gen from that list.

### but the idea now is to describe a characteristic like hardness, describe how good it is in words.
### then from that grab stats of how good it is using comparisons, and knowledge for how the game's stats compare to real life if applicable.

#Calvin notes
#prompt engineering
#keep it really low level.
#use a seed, for consisent 
#if fine turn then run it a bunch of times. with both versions.

#categories tied to hunger, dont say common and uncomman
#given a scale of 1-10 how would you say grapes satify hunger.
#no 2 scale problems
#smiple as possible just get it going.
#restart code.

#define outputs.

#To-do
# [] get a LM working