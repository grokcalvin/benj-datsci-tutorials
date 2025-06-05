from Inventory import *
import copy
import story_LM
#item using and item creation

    #item using is first.
    # [ Done ] effects
    # [ Done ] requirements
    # [ Done ] boost attibute
    #   armor
    #
    # wrench is required to fix ___
    # wrench is requiremed to make ___


    #effects
       #hp_gain
       #increase food
       #sincrease water
    
    #creating items questions and presets
        #is this item food? simply reply Y or N:
            #would you say that this food is closer to level 1 food or level 3 food? simply reply 1 or 3, then explain why?, cut off tag
                #would you say that this is a level 1 or level 2 food? simply say 1 or 2, then explain why?
                #would you say that this is a level 3 or level 4 food? simply say 4 or 3, then explain why?
    #reference all items gained or used, if no with similar name then create
        #[ Done ] create Y N is food.
        #[ Done ] create 2 or 4 split
        #[ Done ] create 1 2 split
        #[ Done ] create 3 4 split
        #[ Done ] create catagory dict
        #[ Done ] catagories area returned test 30 of them
        #[ Done ] iterate through catagory
        #[ Done ] see which catagory has then most
    #[ Done ]
        #[  ] create prompt for setting item range of { } item

    
#add logs to areas [  ]

class item_type():
    def __init__(self,gain_hp=None,gain_food=None,gain_water=None,gain_armor=None,name="item",damage=None):
        self.gain_hp=gain_hp
        self.gain_food=gain_food
        #self.gain_water=gain_water
        self.gain_armor=gain_armor
        self.name = name
        self.damage = damage

class item():
    def __init__(self,name,parent_inventory=None,item_type=None,is_stackable=True,quantity=1):
        self.name = name
        self.parent_inventory = parent_inventory
        self.gain_hp = item_type.gain_hp
        self.gain_food = item_type.gain_food
        #self.gain_water = item_type.gain_water
        self.gain_armor = item_type.gain_armor
        self.damage = item_type.damage

        self.type = item_type.type
        self.quantity = quantity
        self.is_stackable = is_stackable

    def effect_player(self,target):
        if self.gain_hp != None:
            target.hp += self.gain_hp
        if self.gain_food != None:
            target.food = self.gain_food
        #if self.gain_water != None:
            #target.water = self.gain_water       
        



class Area():
    def __init__(self,name,decription="",Inventory=[],parent_area=None,plot_points=[]):
        self.decription = decription
        self.inventory = Inventory
        self.sub_areas = []
        self.parent_area = parent_area
        self.name = name
        self.path = "root"
        self.characters_in_area = []

        self.log_points = plot_points

        if self.parent_area != None:
            self.name_space = self.parent_area.name_space+"/"+name
        else:
            self.name_space = name




    def add_sub_area(self,name,decription="",inventory=[]):
        self.sub_areas.append(Area(name,decription=decription,Inventory=inventory,parent_area=self))
        self.sub_areas[-1].path = self.path+"/"+self.sub_areas[-1].name

    def add_log_point(self,needed_context,point_log):
        plot_point = story_LM.plot_point(needed_context=needed_context,point_to_log=point_log)
        self.log_points.append(plot_point)

    def return_subplot(self,name):
        name_list = []
        for i in self.sub_areas:
            name_list.append(i.name)

        return self.sub_areas[name_list.index(name)]

    def reparent_area(self,parent_area):
        self.parent_area = parent_area
    def remove_sub_areas(self,name):
        name_list = []
        for i in self.sub_areas:
            name_list.append(i.name)
        name_index = self.sub_areas.index(name)
        self.sub_areas.pop(name_index)

    def list_all_items(self):
        item_list = self.inventory

    def get_sister_areas(self):
        if self.parent_area:
            return self.parent_area.sub_areas
    def get_characters_in_area(self):
        return self.characters_in_area

def scan_down(starting_point,layers,name):
    plot_points = starting_point.sub_areas
    found_name = None
    name_list = []
    for i in plot_points:
        name_list.append(i.name)
        try:    
            area_index = name_list.index(name)
            found_name = plot_points[area_index]
            if found_name != None:
                return found_name
        except: pass
    layers -= 1

    if layers <= 0 and found_name == None:
        return None

    if layers > 0:
        for spp in plot_points:
            try:
                found_name = scan_down(spp,layers,name)
                if found_name != None:
                    return found_name
            except: pass
    elif found_name == None:
        return None

def scan_by_layer(target,name):
    found_name = None
    orininal_point = target
    layers_base = 1
    while found_name == None:
        layers = layers_base
        if target.parent_area != None:
            if target.parent_area.name == name:
                return target.parent_area.name

        while layers > 1:
            if target.parent_area != None:
                target = target.parent_area
            found_name = scan_down(target,layers-1,name)
            layers -= 1
            if found_name != None:
                return found_name
        
        found_name = scan_down(orininal_point,layers_base,name)
        if found_name != None:
            return found_name
        layers_base += 1


#if 5 then go to 1 with 4 left to scan down


#mutliple parents
                
        #main list of all total - objects, then next layer
                #dig into layer 

#if not then do next layer up and down
   # for it to go down you need to know how far to go down

    #return the area object by going into area objects
        
    

class game():
    def __init__(self):
        root = ["test/test1"]
        pass

def move_item_area(item,location_directory):
    item.parent_area.remove_item(item.name)
    current_point = game.areas
    for i,s in enumerate(location_directory.split("/")):
        print(i + s)
        current_point = current_point.return_subplot(i[s])

def make_layers(target:Area, layers):
    for i in range(10):
        target.add_sub_area(str(i))
    layers -= 1
    if layers > 0:
        for i in target.sub_areas:
            make_layers(i,layers)

#do something takes ___ time, or end day.

    #"World/United_states/Washington_State/Abderdeen/bunker/kitchen/box"

    #"move medpacks from kitchen to the farm"
    
if __name__ == "__main__":
    root = Area("root")

    make_layers(target=root,layers=3)
    print(root.sub_areas[2].sub_areas[1].sub_areas[5].name_space)
    starting_point = root.sub_areas[2].sub_areas[1].sub_areas[5]

    #end point for testing
    root.sub_areas[5].sub_areas[1].sub_areas[5].name = "bunker 4"


    print(scan_by_layer(root,"bunker 4").name)
    print(scan_by_layer(starting_point,"bunker 4").name_space)


    item_types = {"medpack":item_type(gain_hp=10),
                  "sushi":item_type(gain_food=30),
                  "water_bottle":item_type(gain_water=20),
                  "steel_helmet":item_type(gain_armor=10,type="helmet"),
                  "cavlar_helmet":item_type(gain_armor=20,type="helmet")
                  }

    medpack = item("medpack",item_type=item_types["medpack"],)
    print(medpack.name)
    #banjo = character.Character("banjo")
    #medpack.effect_player(banjo)
    print(banjo.hp)
#list of areas

#testfor has list

    needed_for_crafting = Inventory()
    needed_for_crafting.add_items([
        medpack,
        item("shushi",item_type=item_types["sushi"]),
        item("water_bottle",item_type=item_types["water_bottle"])
        ])
    
    needed_for_crafting.print_inventory()

    copy_inv = copy.copy(needed_for_crafting)
    needed_for_crafting.add_items(copy_inv)
    needed_for_crafting.print_inventory()
    
    print(needed_for_crafting.check_if_items(copy_inv))
    needed_for_crafting.print_inventory()

    helmet = item("steel helmet",item_type=item_types["steel_helmet"])
    better_helmt = item("cavlar helmet",item_type=item_types["cavlar_helmet"])
    banjo.equip_item(helmet)
    print(banjo.mod_armor)
    banjo.equip_item(better_helmt)
    print(banjo.mod_armor)
    banjo.inventory.print_inventory()


#needs inventory


#for list if not tool then keep then remove tools


#we moving farming tools to farm input item, then farm but what if farm, shed