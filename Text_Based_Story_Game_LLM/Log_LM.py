from ollama import *
import index_testing

#imput story to context
def get_response():
    On = True
    filename = input("filename:")
    redo_prompt = ""
    while On == True:
        with open("examples_for_LLM/"+filename,"r") as f:
            Context = f.read()
        print(Context)
        if redo_prompt == "":
            Prompt = input("Enter Prompt or \'use file\':")
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
        print(prompt_list)

        full_response = ""
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
        print(messages_list)


        #system prompt#short reply
        syt_prompt = "you are a long term role playing bot, whose goal it is to give a log of information about what happened with a specific point of the plot. Here is the plot point to log: "
        syt_prompt = syt_prompt + "It's the end of the world, it's the zombie apocalypse. This story follows a small family that has been living in a bunker. 4 brothers, banjo the eldest bother, 22, bumpsh the second to oldest, 19, Yam, the third to oldest, and boibest, the 4th eldest."
        #syt_prompt = "you are to take a part of a narrative and add something interesting to that plot point."
        syt_prompt = [{"role": "user", "content": f"{syt_prompt}"}]
        messages_list = syt_prompt+messages_list


    # Stream the response
        stream = chat(
            model="lexi-story-48k",
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
            print(content, end="", flush=True)

        print("\n\n")

        #response = generate("lexi-story-56k",Context+Prompt)
        #response = response["response"]
        Keep = input("redo or keep or reprompt?:")
        if Keep == "keep":
            Prepend_prompt = "\n\nPrompt: "
            Prompt = Prepend_prompt+Prompt
            with open(filename,"w") as f:
                f.write(Context+Prompt+"\n\nResponse: "+response)
            redo_prompt = ""
        elif Keep == "redo":
            redo_prompt = Prompt
        elif Keep == "reprompt":
            redo_prompt = ""
if __name__ == "__main__":
    get_response()