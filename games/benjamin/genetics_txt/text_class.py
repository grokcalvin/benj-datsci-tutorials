class title_class:
    def __init__(self,name:str,parent) -> None:
        self.name = name
        self.parent = parent
        self.child_display = []
    def action(self,function:str,new_parent):
        if function == "test1" and function in [i.name for i in self.parent.child_display]:
            self.child_display=[
                title_class(name="teir2_1",parent=new_parent),
                title_class(name="teir2_2",parent=new_parent),
                title_class(name="back",parent=new_parent),
            ]
            text_display(self)
        elif function == "teir2_1" and function in [i.name for i in self.parent.child_display]:
            self.child_display=[
                title_class(name="teir3_1",parent=new_parent),
                title_class(name="teir3_2",parent=new_parent),
                title_class(name="back",parent=new_parent),
            ]
            text_display(self)
        elif function == "teir3_1" and function in [i.name for i in self.parent.child_display]:
            self.child_display=[
                title_class(name="teir4_1",parent=new_parent),
                title_class(name="teir4_2",parent=new_parent),
                title_class(name="back",parent=new_parent),
            ]
            text_display(self)
        elif function == "teir3_2" and function in [i.name for i in self.parent.child_display]:
            self.child_display=[
                title_class(name="teir4_3",parent=new_parent),
                title_class(name="teir4_4",parent=new_parent),
                title_class(name="back",parent=new_parent),
            ]
            text_display(self)
        elif function == "teir2_2" and function in [i.name for i in self.parent.child_display]:
            self.child_display=[
                title_class(name="teir3_3",parent=new_parent),
                title_class(name="teir3_4",parent=new_parent),
                title_class(name="back",parent=new_parent),
            ]
            text_display(self)
        elif function == "back" and function in [i.name for i in self.parent.child_display]:
            back_display(self.parent)
        elif function == "test2":
            print("test2")
        elif function == "close":
            print("test3")

    #def select(self):
    #    if self.name:
    #        print("you are in combact what will you do?")
    #        for st in self.child_display:
    #            pass
#if is_player, entity.title = combact then entity.title.select
#menu, start and create character= select stats and levels you add to yourself
#run function and then reprint and run again. the input as a selector and break
    #def create_combact_text():
    #    self.child_display
    #def function1
    #def function2

    #def action()

title = title_class(name="title",parent=None)
title.child_display = [title_class(name="test1",parent=title),title_class(name="test2",parent=title),title_class(name="back",parent=title)]
def text_display(title_input:title_class):
    for i in title_input.child_display:
        print(f"{i.name}")

    select = input("Type Here:")
    #exceptation handling
    i.action(function=select,new_parent=i)
    #enum class then pass in enum values

def back_display(title_input:title_class):
    #because your going off child display you need to parent twice to find the parent of this branch
    text_display(title_input.parent)

text_display(title)


#activate certain text with other functions go into text then end on a battle function and by the ned of the battle function go back into the text
def title_list(title_object):
    for n,i in enumerate(title_object.child_display):
        print(f"({n}){i}")

#you can pass a function in as a input

#round counter method, changes every object to run a round pass method to boost objects














































        #print list
        #   then if input == name then function again.
        #
        #if name = __ and name in parent.child_list_names then execute that function:
        #
        #    function that changes the selected title's children titles and then displays them



        #combat menu, options during combat.
        #inventory
        #attack
        #run (sometimes)

        #two modes of combat

        
        #either one takes the move up.