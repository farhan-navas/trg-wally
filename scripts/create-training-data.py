# DATASET STRUCTURE: https://www.kaggle.com/datasets/thedevastator/empathetic-conversational-model-benchmark/data
# This script converts the dataset to jsonl format
# Usage: python3 convert_to_jsonl.py

# Each CSV file contains rows corresponding to indiv turns within conversations, multiple data points per conversation
# Additional colums capture metadata about the conversation. Columns are:
# conv_id: unique identifier for the conversation, eg: hit:0_conv:0
# utterance_idx: order of utterance within conversation
# context: overall context of the conversation
# prompt: conversation 'system' prompt
# speaker_idx: alternates between user and assistant, starting with user 
# utterance: text of the utterance
# selfeval: self-reported quality of the utterance
# tags: associated tags that can be used to categorize or label dialogues

import csv
import json
import sys
from collections import defaultdict

TRAINING_INPUT_PATH = 'data/raw/empathetic-conversational-model/train.csv'
TRAINING_OUTPUT_PATH = 'data/processed/empathetic-conversational-model/train.jsonl'

VALIDATION_INPUT_PATH = 'data/raw/empathetic-conversational-model/validation.csv'
VALIDATION_OUTPUT_PATH = 'data/processed/empathetic-conversational-model/validation.jsonl'

TEST_INPUT_PATH = 'data/raw/empathetic-conversational-model/test.csv'
TEST_OUTPUT_PATH = 'data/processed/empathetic-conversational-model/test.jsonl'

def replace_comma(input: str) -> str:
    return input.replace("_comma_", ",")

def safe_float(x):
    try:
        return float(x)
    except ValueError:
        return 0

def convert_to_jsonl(input_path, output_path):
    conv_groups = defaultdict(list)
    with open(input_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Split into numerical conversation ids
            conv_id = row['conv_id'].strip().split("_")[0].split(":")[1]

            # Limit the number of conversations to 100 (for training), 
            if int(conv_id) > 75:
                break

            conv_groups[conv_id].append(row)

    with open(output_path, 'w') as f:
        # Go through each conversation
        for conv_id, rows in conv_groups.items():
            prompt = rows[0]['prompt'].strip()
            context = rows[0]['context'].strip()
            system_prompt = "System: You are Wally, a caring and savvy relationship wellness assistant with a unique Asian flair. " \
            "Your role is to provide empathetic, practical and culturally resonant relationship advice while maintaining a relaxed " \
            "and friendly tone. Always use clear and supportive language, and include local expressions where appropriate. If a " \
            "user asks about topics outside your area of expertise, such as medical advice, legal matters, etc., politely " \
            "inform them that you are not qualified to provide guidance on those subjects and suggest they consult with the " \
            "appropriate professionals. The user is currently feeling " + context + ". The topic of this conversation is: " + prompt 

            messages = []
            messages.append({"role": "system", "content": replace_comma(system_prompt)})
            speaker_idx = 0
            curr_highest_avg = 0
            curr_highest_idx = 0

            # Go through each row in the conversation
            for row in rows:
                speaker_label = "assistant" if speaker_idx % 2 else "user"
                message = {"role": speaker_label, "content": replace_comma(row['utterance'].strip())}

                self_eval = row['selfeval'].strip()
                eval_str = self_eval.replace("_", "|")
                all_scores = [safe_float(x) for x in eval_str.split("|") if x]
                avg = sum(all_scores) / len(all_scores)

                if avg > curr_highest_avg and speaker_label == "assistant":
                    curr_highest_avg = avg
                    curr_highest_idx = speaker_idx

                # Assign weight to assistant message only if it has a high self-eval score
                if speaker_label == "assistant" and (eval_str == "5|5|5|5|5|5" or eval_str == "4|5|5|5|5|5"):
                    message["weight"] = 1
                elif speaker_label == "assistant":
                    message["weight"] = 0

                messages.append(message)
                speaker_idx += 1

            messages[curr_highest_idx + 1]["weight"] = 1

            while messages[len(messages) - 1]["role"] == "user":
                messages.pop()

            f.write(json.dumps({"messages": messages}) + "\n")

if __name__ == '__main__':
    convert_to_jsonl(TRAINING_INPUT_PATH, TRAINING_OUTPUT_PATH)
    convert_to_jsonl(VALIDATION_INPUT_PATH, VALIDATION_OUTPUT_PATH)
    convert_to_jsonl(TEST_INPUT_PATH, TEST_OUTPUT_PATH)