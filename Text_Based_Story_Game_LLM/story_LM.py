from ollama import *
import index_testing
import Action_LM
import Simplify_Plot_Point
import character
#imput story to context
character_list = []


def index_character(name,character_list):
    name_list = []
    for i in character_list:
        name_list.append(i.name)
    index = name_list.index(name)
    return index

#print(char_context)
class plot_point():
    def __init__(self,needed_context,point_to_log):
        self.plot_point = point_to_log
        self.needed_context = needed_context
        self.subplot_points = []

    def log(self):
        log_output = create_log(self.needed_context,self.plot_point)

        #test_if text sty_prompts
        Is_ploint_point_text = "Decide if this thing that happened would continue to make plot developements on its own. Simply response with Y or N"
        ##HP_Test = "Decide if this game's update log entry directly negatively effects someone's physical health. Second requirement is that it needs to have an IMMEDIATE effect on SPECIFIC Character's physical health, while naming who go hurt. Simply response with Y or N"
        ##Eval_HP = "you are deciding how a game's update log entry should effect the game in a certain way. This game's update log entry has been found to effect a specifics character's physcial health, your role is to decide how much health these statements would take from someone. Simply response with a number ranging from 1-100. 100 is certain death."
        #Item_Damage = "You are deciding how a game's log entry should effect a game in a certain way. This game's update log entry has been found to either destory an item or damage it. you role is to decide how much it damages the item, or if it gets destroyed. simply reply with 'D' for destory or a number ranging from 1-100. with 10 being minor damage and 100 being to completely destroy it."
        #if_damage_item = "Decide if this game's update log entry should directly effect an in game item. Simply response with Y or N"
        ##Who_Got_Hurt = "you are helping direct where damage is dealt in a game based, and if it is specific enough to do damage, on a update log entry. If you canot name the individual person effected reply with 'N' if you can then simply name the person's name."
        #


        #test_2_input = "("+self.needed_context+")"+self.plot_point


        #Effects_Hp = Action_LM.If_Text("if_hp_effect",log_output,HP_Test)
        #if Effects_Hp:
        #    print("effecs Hp")
        #    how_effect_Hp = Action_LM.If_Text("effect_hp",log_output,Eval_HP,non_linear=True)
        #    print(how_effect_Hp)
        #    name = Action_LM.If_Text("specific_name",log_output,Who_Got_Hurt,non_linear=True)
        #    if name != "N":
        #        #index characters based on name
        #        Char_index = index_character(name,character_list)
        #        character_list[Char_index].damage(how_effect_Hp)
        #        print("Hp Left: "+ str(character_list[Char_index].hp))
        #        print("---"+name)

        test = Action_LM.If_Text("subplot_test",log_output,Is_ploint_point_text)
        #test2 = Action_LM.If_Text_Different("different_output",test_2_input,SYT_PROMPT=)
        if test:
            self.child_plot_point(Simplify_Plot_Point.Simplify_Plot_Point(log_output))
            log_output = "\n"+ self.subplot_points[-1].log()
        Is_Person_Introduced = "Your job is to decide if this log involves a new character that we havent met yet. Simply reply Y or N"
        test = Action_LM.If_Text("",log_output,Is_Person_Introduced)
        if test:
            pass
        ##if destory  item:
        ##if Action_LM.If_Text("",log_output,SYT_PROMPT=if_damage_item):
        ##    D_Test = Action_LM.If_Text("",log_output,SYT_PROMPT=Item_Damage)
        ##    print("effects item :"+D_Test)
        #print(log_output)

        print(log_output)
        return log_output
    
        #*log makes logs
        #*logs do things
        #*can make charcaters
        #can make areas in areas
                #can find areas

        #character's stats based on modivation and backstory?

        #*add items, testfor items

        #information that the story grabs from
        #characters stories
           #i want the character to have modication
           #to build their own stories.
           #simple









    def logs(self):
        full_log = ""
        #full_log = create_log(self.context,self.plot_point)
        full_log = full_log + self.log()
        if len(self.subplot_points):
            for i in self.subplot_points:
                full_log = full_log + "\n\n" + i.logs()
        return full_log
    
    
    def child_plot_point(self,child_plot_point):
        self.subplot_points.append(plot_point(self.needed_context+"| "+self.plot_point,child_plot_point))

def create_log(log_context,log_point,filename="sce"):
    On = True
    filename = filename
    redo_prompt = ""
    while On == True:
        with open("examples_for_LLM/"+filename,"r") as f:
            Prompt = log_point
            Context = f.read()
        if redo_prompt == "":
            Prompt = log_point
            if Prompt == "end":
                On = False
                break
            elif Prompt == "use file":
                with open("prompt_input.txt","r") as f:
                    Prompt = f.read()
                    print(Prompt)
        elif redo_prompt != "":
            Prompt = redo_prompt
            print(Prompt)


        messages_list = []
        prompt_list= index_testing.get_phrases("Prompt:","Response:",Context)
        response_list = index_testing.get_phrases("Response:","Prompt:",Context)
        for i in range(len(prompt_list)):
            prompt_list[i] = prompt_list[i].replace("Prompt: ","")
        for i in range(len(response_list)):
            response_list[i] = response_list[i].replace("Response: ","")

        for I in range(len(prompt_list)):
            try:
                messages_list.append({"role": "user", "content": f"{prompt_list[I]}"})
            except:
                pass
            try:
                messages_list.append({"role": "assistant", "content": f"{response_list[I]}"})
            except:
                pass


        #system prompt#short reply
        #syt_prompt = "you are a long term role playing bot. dont make big plot developements without the player. Your goal it is to give a log of information about what happened with a specific point of the plot. make it short. Here is the plot point to log:"
        #syt_prompt = syt_prompt + scenario
        #syt_prompt = "you are to take a part of a narrative and add something interesting to that plot point."
        
        syt_prompt = "You are a bot in a role playing game. Your job is to add a log entry about a specified topic that the player will read."
        syt_prompt = [{"role": "system", "content": f"{syt_prompt}"}]
        messages_list = syt_prompt+messages_list
        messages_list.append({"role": "system", "content": f"Those responses were ideal log entries. Each entry has its own hidden context to there plot point you can not see. Here is your context for the next log, remember it your ouput should look similar to previous outputs: {log_context}"})
        messages_list.append({"role": "user", "content": f"{Prompt}"})

    # Stream the response
        stream = chat(
            model="lexi-story-8k",
            #[{"role": "system", "content": f"{Context+Prompt}"}]
            messages=messages_list,
            stream=True
        )

    # Process and save the streamed data
        iter = 10
        response = ""
        print("Response: ", end="", flush=True)
        for chunk in stream:
            content = chunk["message"]["content"]
            iter -= 1
            if len(response) > 200:
                response = ""
                break
            if iter <= 1:
                iter = 10
                with open("backup_story","w") as f:
                    f.write(Context+Prompt+"\n\nResponse: "+response)
            print(content, end="", flush=True)
            response += content
            #print(content, end="", flush=True)
        if response == "":
            Keep = "redo"
        Keep = "end"
        if Keep == "keep":
            Prepend_prompt = "\n\nPrompt: "
            Prompt = Prepend_prompt+Prompt
            with open("examples_for_LLM/"+filename,"w") as f:
                f.write(Context+Prompt+"\n\nResponse: "+response)
            redo_prompt = ""
        elif Keep == "redo":
            redo_prompt = Prompt
        elif Keep == "reprompt":
            redo_prompt = ""
        elif Keep =="end":
            return response
    return response

if __name__ == "__main__":


    sYT_PROMPT_CHARACTER = "please write an interesting character's behavior/modivation core, the essence of the character. This paragraph will only be referenced to decide what the character. Simply reply with one paragraph speaking of modivations."
    Request = "name: Bobby : charismatic"

    world_context = "It's the zombie apocalypse daya. Most people have moved out of the big cities."
    banjo = character.Character("banjo")
    banjo.generate_story(world_context)
    print(banjo.story)
    banjo.create_sinario(None)
    banjo.built_in_objective = "I want this Character to build a relationship with the player either whether that turns out to be possitive or negative."
    print(banjo.built_in_objective)
    #log_point_1 = "a physically sound 4 capacity bunker."
    #log_1 = plot_point(f"It's the zombie apocalypse daya. Most people have moved out of the big cities.",log_point_1)
    
    
    #log_point_2 = "a small town with 250 people in it names Arab, lead by a man named James."
    #log_2 = plot_point("It's medieval times, oppression, knights and Lords.",log_point_2




    #print(create_log(f"It's the zombie apocalypse day {Day}. Most people have moved out of the big cities.",log_point_1))
    #log_1.child_plot_point("raiders are in town")
    #log_1.child_plot_point("banjo is sick")
    #log_1.subplot_points[0].child_plot_point("raiders issue a threat to all sheltered to give tribute or we they will attack.")
    #print(log_1.subplot_points[0].log())
                                           #"this is for a sub-log that logs on another part of a log."))

    #print(log_1.log())
    #print(log_2.log()) 
    
    
    #it needs to be able to have a scenario and make a log make a log of thing make a log on a certain topic you job is to log about a topic
    #plot variable.

    # #simplistic catagories keywords



# and Lords. the plot follows the story of a small now name arab. Lead by a person name Carl.
#tell me a story about ___palce holder plot___: then it makes a story take the words you want to generalize. i dont like that it can only do zombies, replace zombie with ___. bake me -----, then say this or that over and over.

#dont make up past lore, like

#recurrsion

#effcting plot

#i dont want to effect the creation or output of logs