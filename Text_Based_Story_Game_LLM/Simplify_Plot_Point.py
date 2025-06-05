from ollama import *
import index_testing

#imput story to context
def Simplify_Plot_Point(text: str) -> str:
    filename = "simplify_plot_examples"
    redo_prompt = ""
    On = True
    while On == True:
        with open("examples_for_LLM/"+filename,"r") as f:
            Context = f.read()
        Prompt = text
        if redo_prompt != "":
            Prompt = redo_prompt
            redo_prompt = ""


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
        syt_prompt = "Take out the parts that you could make an information log on over time. Your goal is to find the information that needs to be updated in the future multiple times. Only simply one at a time."
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

        #if input() != "redo":
        #    On = False
        #else:
        #    redo_prompt = Prompt
        On = False
    return response
            
if __name__ == "__main__":
    while True:
        print(Simplify_Plot_Point(input()))


    #Decide if this thing that happened would continue to have an effect realistically speaking.

    #read these various logs and simplify them to just say exactly the long term plot point that in the next.