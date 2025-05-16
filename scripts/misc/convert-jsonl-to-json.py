# Script to convert JSONL files to JSON format, for easier readability and processing.

import json
import os

def convert_jsonl_to_json(input_jsonl_file, output_json_folder):
    # ensure output folder exists
    os.makedirs(output_json_folder, exist_ok=True)
    
    # determine output JSON filename
    base_name = os.path.splitext(os.path.basename(input_jsonl_file))[0]
    output_json_file = os.path.join(output_json_folder, base_name + '.json')
    
    # read jsonl file and aggregate data
    data = []
    with open(input_jsonl_file, 'r', encoding='utf-8') as jsonl_file:
        for line_number, line in enumerate(jsonl_file, start=1):
            line = line.strip()
            if not line:  # Skip empty lines (just in case)
                continue
            try:
                data.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON on line {line_number}: {e}")
                continue
    
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Converted {input_jsonl_file} to {output_json_file}")

# call conversion function
input_jsonl_file = 'data/preprocessed/reddit/train.jsonl' 
output_json_folder = 'data/preprocessed/reddit/'
convert_jsonl_to_json(input_jsonl_file, output_json_folder)

# removed system messages from the JSONL file with the below code, using jq 
# jq -c '
#   (.messages[] 
#     | select(.role=="system") 
#     | .content
#   ) |= sub("^System: *"; "")
# ' train.jsonl > train.jsonl.tmp && mv train.jsonl.tmp train.jsonl

    


            


