# this script create a google form/doc using the google API. Markdown is formatted into html and display in word doc/form 

import json
import pypandoc

try:
    pypandoc.get_pandoc_version()
except OSError:
    print("Downloading pandoc…")
    pypandoc.download_pandoc()

def read_conversation_from_jsonl(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    conversations = []
    for line in lines:
        if line.strip():
            conversations.append(json.loads(line))

    # return a list of conversation objects(?)
    return conversations

def convert_jsonl_to_docx(file_name: str, conversations: list, output_path: str) -> None:
    for idx, convo in enumerate(conversations, start=1):
        # 1. Build a single Markdown string for this conversation
        md = [f"# {file_name} Conversation {idx}\n"]
        for msg in convo["messages"]:
            role = msg["role"].capitalize()
            content = msg["content"]
            # If your content is already HTML, skip this step
            # Otherwise convert Markdown → HTML → back to Markdown (optional)
            # Here we'll assume it's Markdown to begin with:
            md.append(f"## {role} message\n")
            md.append(content + "\n\n")

        full_md = "".join(md)

        # 2. Call pypandoc to convert that markdown into a .docx
        out_file = f"{output_path}-{idx}.docx"
        pypandoc.convert_text(
            full_md,
            to="docx",
            format="md",
            outputfile=out_file
        )
        print(f"✅ Saved {out_file}")

if __name__ == '__main__':
    input_path = 'data/processed/reddit/relationship-advice-train.jsonl'
    conversations = read_conversation_from_jsonl(input_path)
    output_path = 'data/processed-word-docs/reddit/relationship-advice'
    convert_jsonl_to_docx(
        'Relationship Advice Dataset',
        conversations,
        output_path
    )
