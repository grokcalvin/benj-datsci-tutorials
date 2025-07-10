from ollama import *
import index_testing
#imput story to context

def index_character(name,character_list):
    name_list = []
    for i in character_list:
        name_list.append(i.name)
    index = name_list.index(name)
    return index

def If_Text(examples_file,text,SYT_PROMPT="",non_linear=False,just_first_str=False,is_int=False):
    #print("----"+SYT_PROMPT)
    filename = examples_file
    On = True
    Context = ""
    while On == True:
        messages_list = []
        Prompt = text
        redo = False
        if filename:
            with open("star_wars_DnD_LLM/data/"+filename,"r") as f:
                Context = f.read()



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
        syt_prompt = SYT_PROMPT
        #syt_prompt = "you are to take a part of a narrative and add something interesting to that plot point."
        syt_prompt = [{"role": "system", "content": f"{syt_prompt}"}]
        messages_list = syt_prompt+messages_list
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
        for chunk in stream:
            content = chunk["message"]["content"]
            iter -= 1
            check_file = ""
            #create seperate function that returns true/false if int
            if is_int == True:
                try:
                    output = int(content)
                    print(f"int: {content}")
                except Exception as e:
                    print(f"response:{response} content:{content} \n {e}")
                    break 
            #if just_first_str or non_linear == False:
            #    if len(response) > 0:
            #        response = response[0]
            #        break
            with open("star_wars_DnD_LLM/data/On","r") as f:
                check_file = f.read()
            if check_file != "0":
                break
            if iter <= 1:
                iter = 10
                with open("star_wars_DnD_LLM/data/backup_story","w") as f:
                    f.write(Context+Prompt+"\n\nResponse: "+response)
                print(content)
            print(content, end="", flush=True)
            response += content



        #print(response)
        if is_int == True:
            try:
                print("int output: "+output)
                output = response
                return output
            except:
                print("fail int test")
                redo == True
        elif non_linear == False:
            if response[0] == "Y" and len(response) == 1:
                On = False
                output = True
            elif response[0] == "N" and len(response) == 1:
                On = False
                output = False
            else:
                pass
        elif non_linear:
            On = False
            output = response
        if redo == True:
            On = True

    return output
            

def If_Text_Different(examples_file,text):
    filename = examples_file
    On = True
    while On == True:
        with open("star_wars_DnD_LLM/data"+filename,"r") as f:
            Context = f.read()
        Prompt = text



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
        messages_list.append({"role": "user", "content": f"{Prompt}"})


        #system prompt#short reply
        syt_prompt = "Decide if the effects of a log entry effects the game in a different capacity than the log it came from. Simply response with Y or N"
        #syt_prompt = "you are to take a part of a narrative and add something interesting to that plot point."
        syt_prompt = [{"role": "user", "content": f"{syt_prompt}"}]
        messages_list = syt_prompt+messages_list


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
        for chunk in stream:
            content = chunk["message"]["content"]
            iter -= 1
            check_file = ""
            with open("On","r") as f:
                check_file = f.read()
            if check_file != "0":
                break
            if iter <= 1:
                iter = 10
                with open("backup_story","w") as f:
                    f.write(Context+Prompt+"\n\nResponse: "+response)
            response += content

        if response[0] == "Y" and len(response) == 1:
            On = False
            output = True
        elif response[0] == "N" and len(response) == 1:
            On = False
            output = False
        else:
            pass
    return output

def test_if_log_adds_subplot(log):
    test_if_subplot_point = "Decide if this game's update log entry should continue to significantly effect the game, after it happens. Simply response with Y or N"
    output = If_Text("subplot_test",log,SYT_PROMPT=test_if_subplot_point)

    return output







if __name__ == "__main__":

    Is_plot_point_text = "Decide if this game's update log entry should continue to significantly effect the game, after it happens. Simply response with Y or N"
    
    HP_Test = "Decide if this game's update log entry should directly effect someone's health. second requirement is does it have an IMMEDIATE effect one someone's physical health?. Simply response with Y or N"
    Eval_HP = "you are deciding how a game's update log entry should effect the game in a certain way. This game's update log entry has been found to effect a character's physcial health, your role is to decide how much health these statements would take from someone. Simply response with a number ranging from 1-100."


    
    Item_Damage = "You are deciding how a game's log entry should effect a game in a certain way. This game's update log entry has been found to either destory an item or damage it. you role is to decide how much it damages the item, or if it gets destroyed. simply reply with 'D' for destory or a number ranging from 1-100. with 10 being minor damage and 100 being to completely destroy it."
    if_damage_item = "Decide if this game's update log entry should directly effect an in game item. If no item is mentionsed then say 'N'. Simply response with Y or N"

    #print(If_Text("effect_hp","The air recycling units have stopped working",SYT_PROMPT=HP_Test,non_linear=True))
    sty_prompt = ["Decide if this game's event log entry completely uses up, a specific consumable item. not damages an item, consumes it. Simply reply with Y or N, then name the item in the entry that consumed .",
                  "Decide if this game's event log entry names an item that is used. Simply reply with Y or N then name then item/items",
                  "this game's log entry interacts with an item, your role is to decide if that item is one time use or not or uses some of the items. simply reply with Y or N then explain why",
                  "this game's log entry is said to consume an item. your role is to name the item that is consumed. If you think it shouldnt be rendered useless after use, then say 'None' or if None of the items are rendered useless say 'None'",
                  "this game's game's system has said that this log entry does a unknonw amount of damage to someone, your role is to say what catagory of damage the log entry falls into. Simply say Y for 'medium or below' or N for 'high or above'"]
    
    log = ["Banjo uses a medpack",
           "Banjo uses a wrench to fix the sprinkers",
           "Banjo shoots off fireworks",
           "Banjo goes for a walk using a cane.",
           "Gerry is out in the wasteland and gets shot.",
           "Gerry is walking and stubs his toe."]

    #is an item directly item used?

    #are any items not just used but fully consumed?
        #name the item/items that are consumed.

    #double possitive or double negative depending on what side you want to ai
