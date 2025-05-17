import kagglehub
import shutil
import os
# import pandas as pd
from datasets import load_dataset

def load_ecm_dataset():
    # Download latest version
    path = kagglehub.dataset_download("thedevastator/empathetic-conversational-model-benchmark")
    print("Downloaded dataset to", path)

    # Check file exists
    target_dir = "data/raw"
    os.makedirs(target_dir, exist_ok=True)

    # Move files to target directory
    shutil.move(path, target_dir)
    print("Moved dataset to", target_dir)

def load_singlish_dataset():
    ds = load_dataset("gabrielchua/singlish-to-english-synthetic")

    for split, split_dataset in ds.items():
        output_path = f"data/raw/singlish/{split}.csv"
        df = split_dataset.to_pandas()
        df.to_json(output_path, orient="records", lines=True)
        print(f"Saved {split} split to {output_path}")

if __name__ == '__main__':
    # load_ecm_dataset()
    load_singlish_dataset()
