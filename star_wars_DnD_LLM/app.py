from ollama import *
import index_testing

#imput story to context
def get_response():
    On = True
    filename = "app.txt"
    redo_prompt = ""
    while On == True:
        with open("star_wars_DnD_LLM/data/"+filename,"r") as f:
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
        syt_prompt = "You are the DM for a Star Wars DnD campiagn"
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
        print("Response: ", end="", flush=True)
        for chunk in stream:
            content = chunk["message"]["content"]
            iter -= 1
            check_file = ""
            with open("star_wars_DnD_LLM/data/On","r") as f:
                check_file = f.read()
            if check_file != "0":
                break
            if iter <= 1:
                iter = 10
                with open("star_wars_DnD_LLM/data/backup_story","w") as f:
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
            with open("star_wars_DnD_LLM/data/"+filename,"w") as f:
                f.write(Context+Prompt+"\n\nResponse: "+response)
            redo_prompt = ""
        elif Keep == "redo":
            redo_prompt = Prompt
        elif Keep == "reprompt":
            redo_prompt = ""
if __name__ == "__main__":
    get_response()
#how to add perences and bits of text to the stack of data.