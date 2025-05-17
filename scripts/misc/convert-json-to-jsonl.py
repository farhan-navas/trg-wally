# Script to convert JSONL files to JSON format, for easier readability and processing.

import os
import json

def convert_to_jsonl(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    with open(output_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"Converted {input_path} to {output_path}")

# Usage
input_path = 'data/refined/reddit/train.json'
output_path = 'data/refined/reddit/train-trial.jsonl'

convert_to_jsonl(input_path, output_path)