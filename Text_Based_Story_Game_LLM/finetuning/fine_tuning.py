
import itertools
import jsonlines

#from datasets import load_dataset

#from llama import BasicModelRunner

import pandas as pd

from pprint import pprint
from transformers import AutoTokenizer

#{'instruction': 'Give three tips for staying healthy.', 'input': '', 'output': '1.Eat a balanced diet and make sure to include plenty of fruits and vegetables. \n2. Exercise regularly to keep your body active and strong. \n3. Get enough sleep and maintain a consistent sleep schedule.', 'text': 'Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n### Instruction:\nGive three tips for staying healthy.\n\n### Response:\n1.Eat a balanced diet and make sure to include plenty of fruits and vegetables. \n2. Exercise regularly to keep your body active and strong. \n3. Get enough sleep and maintain a consistent sleep schedule.'}
#
#{'input': 'Below is an instruction that describes a task. Write a response '
#          'that appropriately completes the request.\n'
#          '\n'
#          '### Instruction:\n'
#          'Give three tips for staying healthy.\n'
#          '\n'
#          '### Response:',
# 'output': '1.Eat a balanced diet and make sure to include plenty of fruits '
#           'and vegetables. \n'
#           '2. Exercise regularly to keep your body active and strong. \n'
#           '3. Get enough sleep and maintain a consistent sleep schedule.'}

#def inference(text, model, tokenizer, max_input_tokens=1000, max_output_tokens=100):
#  # Tokenize
#  input_ids = tokenizer.encode(
#          text,
#          return_tensors="pt",
#          truncation=True,
#          max_length=max_input_tokens
#  )
#
#  # Generate
#  device = model.device
#  generated_tokens_with_prompt = model.generate(
#    input_ids=input_ids.to(device),
#    max_length=max_output_tokens
#  )
#
#  # Decode
#  generated_text_with_prompt = tokenizer.batch_decode(generated_tokens_with_prompt, skip_special_tokens=True)
#
#  # Strip the prompt
#  generated_text_answer = generated_text_with_prompt[0][len(text):]
#
#  return generated_text_answer

tokenizer = AutoTokenizer.from_pretrained("lexi-story-48k")
text = "Hi, how are you?"
encoded_text = tokenizer(text)["input_ids"]
encoded_text
decoded_text = tokenizer.decode(encoded_text)
print("Decoded tokens back into text: ", decoded_text)




def tokenize_function(examples):
    if "question" in examples and "answer" in examples:
      text = examples["question"][0] + examples["answer"][0]
    elif "input" in examples and "output" in examples:
      text = examples["input"][0] + examples["output"][0]
    else:
      text = examples["text"][0]

    tokenizer.pad_token = tokenizer.eos_token
    tokenized_inputs = tokenizer(
        text,
        return_tensors="np",
        padding=True,
    )

    max_length = min(
        tokenized_inputs["input_ids"].shape[1],
        2048
    )
    tokenizer.truncation_side = "left"
    tokenized_inputs = tokenizer(
        text,
        return_tensors="np",
        truncation=True,
        max_length=max_length
    )

    return tokenized_inputs
#-----------
finetuning_dataset_loaded = datasets.load_dataset("json", data_files=filename, split="train")

tokenized_dataset = finetuning_dataset_loaded.map(
    tokenize_function,
    batched=True,
    batch_size=1,
    drop_last_batch=True
)

print(tokenized_dataset)
#--------
tokenized_dataset = tokenized_dataset.add_column("labels", tokenized_dataset["input_ids"])

#Prepare test/train splits
split_dataset = tokenized_dataset.train_test_split(test_size=0.1, shuffle=True, seed=123)
print(split_dataset)



