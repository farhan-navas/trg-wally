# DATSET STRUCTURE: https://huggingface.co/datasets/gabrielchua/singlish-to-english-synthetic

import os
import csv
import json

TRAINING_INPUT_PATH = 'data/raw/singlish/train.csv'
TRAINING_OUTPUT_PATH = 'data/processed/singlish/train.jsonl'

def convert_to_jsonl():
    with open(TRAINING_INPUT_PATH, 'r') as f:
        with open(TRAINING_OUTPUT_PATH, 'w') as write_file:
            for idx, line in enumerate(f):
                message = []
                system_prompt = "You are Wally, a caring and savvy relationship wellness assistant with a unique Asian flair. " \
                "Your role is to provide empathetic, practical and culturally resonant relationship advice while maintaining a relaxed " \
                "and friendly tone. Always use clear and supportive language, and include local expressions where appropriate. If a " \
                "user asks about topics outside your area of expertise, such as medical advice, legal matters, etc., politely " \
                "inform them that you are not qualified to provide guidance on those subjects and suggest they consult with the " \
                "appropriate professionals."
            
                message.append({"role": "system", "content": system_prompt})
                if idx >= 25:
                    break
                
                row = json.loads(line)
                assistant = row["singlish"].strip()
                user = row["english"].strip()
                message.extend([{"role": "user", "content": user}, {"role": "assistant", "content": assistant}])

                write_file.write(json.dumps({"messages": message}) + "\n")
    
if __name__ == '__main__':
    convert_to_jsonl()