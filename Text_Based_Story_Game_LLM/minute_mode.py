import area
import Action_LM
import story_LM

#[  ] add if player option

def minute_mode(area,state_of_the_world):
    characters_in_local_areas = []
    for i in area.get_sister_areas():
        for ii in i.characters_in_area:
            characters_in_local_areas.append(ii)
    for i in characters_in_local_areas:
        i.minute_logs = False
    for i in characters_in_local_areas:
        if not i.is_currently_controlled_by_player:
            if not i.minute_logs:
                #syt_prompt = f"Your job is to make a log of what a specific character does this minute, given the circumstance, hidden objective, their modivation core, and setting. make a one sentence log of what they decide to do this during this minute."
                syt_prompt = f"This specific log is for when players want to see a what a specifically named character is doing every minute. simply reply with one sentence:"

                
                prompt=f"State of the world: {state_of_the_world}\n{i.name}'s core modivation/guilding behavior: {i.story}\nHidden objective: {i.built_in_objective}\nSetting: {i.current_area.decription}"
        
                i.minute_logs = story_LM.create_log(prompt,SYT_PROMPT=syt_prompt)
            i.minute_logs.log
        else:
            #interacts with objects in rooms. take, or use
            player = i
    valid_input = False        
    while valid_input == False:
        print(player.current_area.name)
        syt_prompt = f"This specific log is saying what the player does. Simply reply with one sentence:"

        prompt = input(f"what does {player.name} do?: ")
        i.minute_logs = story_LM.create_log(prompt,SYT_PROMPT=syt_prompt)

        #tests
        #if vaild then pass

    #need new q
    #what controls if they leave an area
    #every minute decide what this character wants to do.
    # log minute log for NPC?
       #no real action just logs that can effect things?
       #no stats?
       #can make new logs that stick, like starts playing checker. does this action last more than a minute?

    #when starting something realistic stay there time
        #how long does this character want to do this?