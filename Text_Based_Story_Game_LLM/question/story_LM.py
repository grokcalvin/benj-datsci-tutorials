from ollama import *
import index_testing
#imput story to context
character_list = []


def index_character(name,character_list):
    name_list = []
    for i in character_list:
        name_list.append(i.name)
    index = name_list.index(name)
    return index

#print(char_context)

def create_log(filename="sce"):
    On = True
    filename = filename
    redo_prompt = ""
    while On == True:
        Prompt = input("Input Filename:")

        messages_list = [{"role": "user", "content": f"{Prompt}"}]
        operational_data = "The user prefers for you to not name unnessiarly specifics when planning, yet still with depth."
        syt_prompt = [{"role": "system", "content": f"{operational_data}"}]
        messages_list = syt_prompt+messages_list

    # Stream the response
        stream = chat(
            model="lexi-story-8k",
            messages=messages_list,
            stream=True
        )

    # Process and save the streamed data
        iter = 10
        response = ""
        print("Response: ", end="", flush=True)
        Context = ""
        for chunk in stream:
            content = chunk["message"]["content"]
            iter -= 1
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

    test = create_log("Test")
    print(test)