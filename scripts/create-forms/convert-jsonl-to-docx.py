import os
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
        # build a single markdown string for this conversation
        md = [f"# {file_name} Conversation {idx}\n"]
        for msg in convo["messages"]:
            role = msg["role"].capitalize()
            content = msg["content"]
            md.append(f"## {role} message\n")
            md.append(content + "\n\n")

        full_md = "".join(md)

        # convert markdown into a .docx
        out_file = f"{output_path}-{idx}.docx"
        os.makedirs(os.path.dirname(out_file), exist_ok=True)
        pypandoc.convert_text(
            full_md,
            to="docx",
            format="md",
            outputfile=out_file
        )
        print(f"Saved {out_file}")

    print(f"✅ Converted {len(conversations)} conversations to {output_path}*.docx")

#changed to create folder and move docs into it
if __name__ == '__main__':
    #change
    input_path = 'data/preprocessed/reddit/askSingapore-train.jsonl'
    conversations = read_conversation_from_jsonl(input_path)

    #change
    base_dir    = r'data/processed-word-docs/english/reddit'
    folder_name = 'ask-singapore'

    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    #change name
    output_path = os.path.join(folder_path, 'ask-singapore')

    convert_jsonl_to_docx(
        'Advice Dataset',
        conversations,
        output_path
    )

