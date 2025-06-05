import re
with open("prompt_input.txt","r") as f:
    text = f.read()
    text = re.sub(r'[\n]', ' ', text)

with open("prompt_input.txt","w") as f:
    f.write(text)