import json
import os

TRAINING_INPUT_PATH  = 'data/raw/reddit/advice.json'
TRAINING_OUTPUT_PATH = 'data/preprocessed/reddit/advice-train.jsonl'

SYSTEM_PROMPT = (
    "You are Wally, a caring and savvy relationship wellness assistant with a unique Asian flair. "
    "Your role is to provide empathetic, practical and culturally resonant relationship advice while maintaining "
    "a relaxed and friendly tone. Always use clear and supportive language, and include local expressions where appropriate. "
    "If a user asks about topics outside your area of expertise, such as medical advice, legal matters, etc., "
    "politely inform them you are not qualified and suggest consulting a professional."
)

def clean_comments(comments):
    # remove auto-moderator comments
    return [c for c in comments if c.get("comment author") != "AutoModerator"]

def build_chain_messages(title, post_text, top_comment):
    # system → user:title+text → assistant:top_comment → user:reply → assistant:reply → …
    msgs = [{"role": "system", "content": SYSTEM_PROMPT}]

    # Combine title and text into the first user message
    combined = (title.strip() + "\n\n" + post_text.strip()).strip()
    if combined:
        msgs.append({"role": "user", "content": combined})

    current = top_comment
    role = "assistant"
    while current:
        text = current.get("body", "").strip()
        if text:
            msgs.append({"role": role, "content": text})

        replies = current.get("replies", [])
        if not replies:
            break

        current = replies[0]
        role = "user" if role == "assistant" else "assistant"

    return msgs

def convert_reddit_threads(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as f:
        threads = json.load(f)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as out:
        count = 0
        for thread in threads:
            title = thread.get("title", "")
            post_text = thread.get("text", "")
            comments = clean_comments(thread.get("comments", []))

            for top in comments:
                if not top.get("replies"):
                    continue

                messages = build_chain_messages(title, post_text, top)
                if len(messages) > 2:
                    out.write(json.dumps({"messages": messages}, ensure_ascii=False) + "\n")
                    count += 1

    print(f"Successfully wrote {count} conversations")

if __name__ == "__main__":
    convert_reddit_threads(TRAINING_INPUT_PATH, TRAINING_OUTPUT_PATH)
