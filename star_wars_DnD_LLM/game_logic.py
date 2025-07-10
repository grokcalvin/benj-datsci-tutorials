core_data = "core_text"
perferences = 'preferences'
quest_exmaple = 'quest_example'
timeline = "timeline"
version = 'version_of_game'
save_to = 'app'

def Compile_Text():
    compiled_text = ""
    with open("star_wars_DnD_LLM/data/"+core_data,"r") as f:
        Context = f.read()
        compiled_text = compiled_text + Context +'\n\n'
    with open("star_wars_DnD_LLM/data/"+perferences,"r") as f:
        Context = f.read()
        compiled_text = compiled_text + Context +'\n\n'
    with open("star_wars_DnD_LLM/data/"+quest_exmaple,"r") as f:
        Context = f.read()
        compiled_text = compiled_text + Context + '\n\n'
    with open("star_wars_DnD_LLM/data/"+timeline,"r") as f:
        Context = f.read()
        compiled_text = compiled_text + Context + '\n\n'
    with open("star_wars_DnD_LLM/data/"+version,"r") as f:
        Context = f.read()
        compiled_text = compiled_text + Context


    with open("star_wars_DnD_LLM/data/"+save_to,"w") as f:
        Context = f.write(compiled_text)

