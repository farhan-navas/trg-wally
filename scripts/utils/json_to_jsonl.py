# Script to convert JSON files to JSONL format, for API

import json

def convert_to_jsonl(input_path, output_path):
    with open(input_path, 'r') as f:
        data = json.load(f)

    with open(output_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
    
    print(f"[json_to_jsonl] converted {input_path} to {output_path}")

# Usage
input_path = 'data/processed/reddit/relationship-advice-train.json'
output_path = 'data/processed/reddit/relationship-advice-train.jsonl'