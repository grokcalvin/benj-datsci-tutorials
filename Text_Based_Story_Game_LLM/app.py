import index_testing
import area
# 1
# get a line to read from file [ DONE ]
# find something in  a string [ Done ]
# find where a string ends [ Done ]
# get the rest of the string [ Done ]
# find the index of end point [ Done ]
# get exact string you want [ Done ]

# 2
# get State of the world var set [ Done ]
# write a basic area file [ DONE ]
# write basic dirctory of starting area [ DONE ]
# get the basic directory of staring area [ DONE ]
# assign root area [ Done]
# assign entire string as sub_area [ Done ]
# split string and run a for loop [ Done ]
# assign current targeted area [ Done ]
# iterate through assigning area values [ Done ]
# write example for adding more areas [ Done ]
# Get str of adding areas [ Done ]
# write for loop for each bracket [ Done ]
# get rid of bracket data [ Done ]
# split data with : [Done]
# search for area with second name [ Done ]
# add first data point to the found area [ Done ]
#do the same thing but for discriptions of area: [ Done ]

# make players_current location var [ Done ]
# get players current location [  ]

class Game():

    #[ Done ] area imports
    #[ Done ] area decriptions imports
    #[ Done ] area log imports

    #chance of makeing log as part of input
    #gameloop, for areas in dir print logs

    def __init__(self,start_data):
        with open("examples_for_LLM/"+start_data,"r") as f:
            game_txt = f.read()

        start_index = game_txt.index("State_Of_World: ")+len("State_Of_World: ")
        end_index = game_txt.index(">",start_index)
        self.State_Of_The_World = game_txt[start_index:end_index]
        print(self.State_Of_The_World)


        self.root_area = area.Area(name="root")
        #area break down loop
        start_str = "Name the area you start in example Washington State/Aberdeen/Banjo's House>: "
        start_index = game_txt.index(start_str)+len(start_str)
        end_index = game_txt.index(">",start_index)
        new_str = game_txt[start_index:end_index]
        new_str = new_str.split("/")
        print(new_str)
        current_targeted_area  = self.root_area
        for dir in new_str:
            current_targeted_area.add_sub_area(dir)
            current_targeted_area = current_targeted_area.sub_areas[0]
        
        self.players_current_location = current_targeted_area


        #add multiple areas:
        start_str = "To add other places in the world becides where you start, add as many as you want using this format: [place to add the world:place that place is in],[],[]: "
        start_index = game_txt.index(start_str)+len(start_str)
        end_index = game_txt.index(">",start_index)
        new_str = game_txt[start_index:end_index]
        new_str = new_str.split(",")
        for i in new_str:
            
            new_i = i[1:len(i)-1]
            print(new_i)
            new_i = new_i.split(":")
            print(new_i)
            area_to_add_to = area.scan_by_layer(self.root_area,new_i[1])
            area_to_add_to.add_sub_area(new_i[0])
            print(area_to_add_to.sub_areas)
        
        #add decriptions to areas:
        start_str = "To add decriptions to areas write [this is an example discription of an area:area name]: "
        start_index = game_txt.index(start_str)+len(start_str)
        end_index = game_txt.index(">",start_index)
        new_str = game_txt[start_index:end_index]
        new_str = new_str.split(";")
        for i in new_str:
            new_i = i[1:len(i)-1]
            new_i = new_i.split(":")
            area_to_add_to = area.scan_by_layer(self.root_area,new_i[1])
            area_to_add_to.decription = (new_i[0])
            print(area_to_add_to.decription)

        start_str = "To add topic that will be logged write [Log Topic,Area To assign the Log Topic]: "
        start_index = game_txt.index(start_str)+len(start_str)
        end_index = game_txt.index(">",start_index)
        new_str = game_txt[start_index:end_index]
        new_str = new_str.split(";")
        for i in new_str:
            new_i = i[1:len(i)-1]
            new_i = new_i.split(":")
            area_to_add_to = area.scan_by_layer(self.root_area,new_i[1])
            print(new_i[0])
            area_to_add_to.add_log_point(self.State_Of_The_World,new_i[0])



    def get_path_areas(self):
        log_path = self.players_current_location.path
        print(log_path)
        log_path = log_path.split("/")
        area_log_list = []
        for log in log_path:
            area_log_list.append(area.scan_by_layer(self.players_current_location,log))
        return area_log_list

    def log_logs(self,area_list):
        for area in area_list:
            if area.log_points:
                for i in area.log_points:
                    print(f"{area.name} log: {i.logs}\n")

    def log_path(self):
        areas_in_path = self.get_path_areas()
        self.log_logs(areas_in_path)
        #self.root_area = area.Area("root")



game_test = Game(input("Enter file name:"))
game_test.log_path()

        