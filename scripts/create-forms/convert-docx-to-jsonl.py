import os
import re
import json
import glob
import pypandoc

def convert_docx_to_markdown(docx_path: str) -> str:
    return pypandoc.convert_file(docx_path, 'gfm', format='docx', extra_args=["--wrap=none"])

def parse_docx_to_convo(docx_path: str) -> dict:
    md = convert_docx_to_markdown(docx_path)
    md = re.sub(r'(?m)^[ \t\-]{4,}$', '---', md)

    # Split on each "## X message" heading
    parts = re.split(r"(?m)^##\s+(Assistant|User|System)\s+message\s*$", md)

    messages = []
    for i in range(1, len(parts), 2):
        role = parts[i].lower()               # will come out to "assistant", "user", or "system"
        content = parts[i+1].strip()          # the markdown content under that heading
        messages.append({"role": role, "content": content})

    return {"messages": messages}

def convert_docx_folder_to_json(docx_folder_pattern: str, output_json: str):
    # read all .docx matching pattern, parse each into a convo, then write the full list to output_json
    files = sorted(glob.glob(docx_folder_pattern))
    all_convos = []

    for path in files:
        convo = parse_docx_to_convo(path)
        all_convos.append(convo)
        print(f"Converted {path} into a convo of {len(convo['messages'])} messages")

    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(all_convos, f, ensure_ascii=False, indent=2)

    print(f"✅ Wrote {len(all_convos)} conversations to {output_json}")

if __name__ == "__main__":
    convert_docx_folder_to_json(
        docx_folder_pattern="data/processed-word-docs/english/reddit/relationship-advice-*.docx",
        output_json="data/processed/reddit/trial.json"
    )

    # with open("data/processed/reddit/trial.json", 'w', encoding='utf-8') as f:
    #     convo = parse_docx_to_convo("data/processed-word-docs/english/reddit/relationship-advice-1.docx")
    #     json.dump(convo, f, ensure_ascii=False, indent=2) 
