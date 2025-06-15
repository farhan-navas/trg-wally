# Read all files matching the folder pattern and write them in order to out_path

import glob
import os

def merge_files(pattern: str, output_path: str):
    paths = sorted(glob.glob(pattern))
    if not paths:
        print(f"[merge_files] ❌ no files found for pattern: {pattern!r}")

    print(f"[merge_files] found {len(paths)} files matching pattern: '{pattern}'")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as fout:
        for idx, p in enumerate(paths):
            with open(p, 'r', encoding='utf-8') as fin:
                content = fin.read().rstrip('\n')
            fout.write(content)
            if idx < len(paths) - 1:
                fout.write('\n')

        print(f"[merge_files] ✅ merge complete, output file: '{output_path}'")

# Example usage:
# merge_files("data/processed/*/*.jsonl", "data/processed/final.jsonl")
