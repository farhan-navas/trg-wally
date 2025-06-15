# Simple function to validate training dataset and find out if there are any lines ending with a user message instead of a asistant message

import os
import json
from typing import List

def find_user_ending_lines(jsonl_path: str) -> List[int]:
    abs_path = os.path.abspath(jsonl_path)
    print(f"[DEBUG] Opening file at: {abs_path}")
    if not os.path.isfile(abs_path):
        raise FileNotFoundError(f"No such file: {abs_path}")

    user_ending_lines = []

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        print("starting at file: ", jsonl_path)
        for idx, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue

            record = json.loads(line)

            msgs = record.get("messages", [])
            if not isinstance(msgs, list) or not msgs:
                continue

            # assume each msg is a dict with one key: either "user" or "assistant"
            last_msg = msgs[-1]
            if isinstance(last_msg, dict) and last_msg.get("role") == "user":
                user_ending_lines.append(idx)

    return user_ending_lines