#prompts = []
#response = []
#Prompt_index = F.index("Prompt:")
#print(Prompt_index)
#response_index = F.index("Response:")
#print(response_index)
#slice = F[Prompt_index:response_index]
#print(slice)
#Prompt_index = F.find("Prompt:", response_index)
#print(Prompt_index)
#print(F[28:])

def get_phrases (phrase_start="",end_phrase="",F=""):
    loop_count = 1
    phrases = []
    start_phrase_index = 0
    first_orrance = F.index(phrase_start,start_phrase_index)
    for i in range(F.count(phrase_start)):
        start_phrase_index = F.index(phrase_start,start_phrase_index)
        if loop_count == F.count(phrase_start) and F.count(phrase_start,first_orrance) > F.count(end_phrase,first_orrance):
            phrases.append(F[start_phrase_index:len(F)-2])
        else:
            end_phrase_index = F.index(end_phrase,start_phrase_index)
            phrases.append(F[start_phrase_index:end_phrase_index-2])

        start_phrase_index += 1
        loop_count +=1
    return phrases
