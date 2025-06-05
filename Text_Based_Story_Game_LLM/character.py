from Inventory import *
import Action_LM
import story_LM

 # [ Done ] assign variables
 # [ Done ] Give character a stats objects
 # [ Done ] access them in battle
 # [ Done ] Give stats to status effect
class stats():
    def __init__(self,name="",hp=0,strength=0,dexterity=0,constitution=0,food=0,water=0,armor=0):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.dexterity = dexterity
        constitution = constitution
        self.food = food
        #self.water = water

        self.armor = armor

    def add_stats(self,target):
        target.hp += self.hp
        target.strength += self.strength
        target.dexterity += self.dexterity
        target.constitution += self.constitution
        target.food += self.food
        #target.water += self.water

        target.armor += self.armor

class status_effect():
    def __init__(self,name,stats,effect_interval="combat round"):
        self.name = name
        self.effect_interval = effect_interval
        self.stats = stats
        
class Character():
    def __init__(self,name,gear=[],inventory=Inventory(),personality=[],story="",curent_area=None,moves=[],is_player_controlled=False):
        self.name = name
        self.inventory = inventory
        self.inventory.parent = self
        self.story = story
        self.log_points = []
        self.minute_logs = []
        self.current_area = curent_area
        self.moves = moves
        self.movement = 0

        self.is_player_controlled = is_player_controlled
        self.is_currently_controlled_by_player = False

        status_effects = []
        stats = stats(hp=100,strength=10,dexterity=10,constitution=10,food=100,water=100,armor=0)
        self.attribute_mod_items = gear

        #modified attribute
        self.mod_armor = None

        #when take it off
    def equip_item(self,item):
        #if not found equip
        type_list = []
        for i in self.attribute_mod_items:
            type_list.append(i.type)
        if item.type in type_list:
            index = type_list.index(item.type)
            self.inventory.add(self.attribute_mod_items[index])
            del self.attribute_mod_items[index]
            self.attribute_mod_items.append(item)
        else:
            self.attribute_mod_items.append(item)
        self.calculate_attribute_mod()

    def calculate_attribute_mod(self):
        self.mod_armor = self.armor
        for i in self.attribute_mod_items:
            if i.gain_armor != None:
                self.mod_armor += i.gain_armor


    def damage(self,amount):
        self.hp = self.hp - int(amount)
        if self.hp <= 0:
            print("dead")

    def generate_story(self,world_context, where_he_ends):
        sYT_PROMPT_CHARACTER = "please write an interesting character's behavior/modivation core, the essence of the character. This paragraph will only be referenced to decide what the character. Simply reply with one paragraph speaking of modivations."
        Request = f"{self.name}"

        self.story = Action_LM.If_Text("characters_core",text=Request,SYT_PROMPT=sYT_PROMPT_CHARACTER,non_linear=True)

    def create_sinario(self,sinario_requirement):
        #syt_prompt = f"Create a realistic explanation for {self.name} to be in the following circumstance in one paragraph."
        syt_prompt = f""

        #no sinario, they just start talking to player and then

        circumstance = f"{self.name} is meeting the player in front of the player's bunker."
        prompt = f"[Charcter's modivation core:] {self.story} [Circumstance needs explaination:] {circumstance}"
        self.sinario = Action_LM.If_Text("",prompt,syt_prompt,non_linear=True)
        print(self.sinario)

    def area_log(self):
        self.current_area_log = story_LM.plot_point("The personal effect of being at this location for around 24 hours, or something they did during that time",f"{self.name} has been in {self.curent_area.name}:{self.current_area.decription} for 24 hours")
        return self.current_area_log
    
    def logs(self):
        self.area_log()
        self.current_area_log.logs
        if self.current_area_log:
            for i in self.log_points:
                i.logs

    def print_moves(self):
        full_str = ""
        index = 1
        for i in self.moves:
            req_item = ""
            req_ammo = ""
            min = 0
            max = 0
            for ii in i.dice:
                max += ii
                min += 1
            if i.req_item:
                req_item = f"req item: {i.req_item}"
            if i.req_ammo:
                req_item = f"req ammo: {i.req_ammo}"
            full_str = full_str + f" {index} - {i.name} {min} damage to {max} damage, movement cost:{i.calculate_total_required_movement()} {req_item} {req_ammo}\n"
            index += 1
        return full_str

    # [ Done ] triggered during battle it have effect
    # [ Done ] Effect the stats of the chracter based on status effects
    # [  ] is it best to have stat object? that can old other stat objects and add them all up?
    # [  ] or if statements to compare the stats and subtract.
    def status_effect_effect(self):
        if self.status_effects:
            for i in self.status_effects:
                if i.effect_interval == "combat round":
                    self.stats.add_stats(i)