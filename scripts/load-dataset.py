import kagglehub
import shutil
import os

def main():
    # Download latest version
    path = kagglehub.dataset_download("thedevastator/empathetic-conversational-model-benchmark")
    print("Downloaded dataset to", path)

    # Check file exists
    target_dir = "data/raw"
    os.makedirs(target_dir, exist_ok=True)

    # Move files to target directory
    shutil.move(path, target_dir)
    print("Moved dataset to", target_dir)

if __name__ == '__main__':
    main()
