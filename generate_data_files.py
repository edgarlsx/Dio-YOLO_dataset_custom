import os
import glob
import random

def generate_train_val_split(img_dir, output_dir, split_ratio=0.8):
    os.makedirs(output_dir, exist_ok=True)

    all_images = glob.glob(os.path.join(img_dir, "*.jpg"))
    random.shuffle(all_images)

    split_index = int(len(all_images) * split_ratio)
    train = all_images[:split_index]
    val = all_images[split_index:]

    with open(os.path.join(output_dir, "train.txt"), "w") as f:
        for path in train:
            f.write(f"{os.path.abspath(path)}\n")

    with open(os.path.join(output_dir, "val.txt"), "w") as f:
        for path in val:
            f.write(f"{os.path.abspath(path)}\n")

if __name__ == "__main__":
    generate_train_val_split("data/images/train", "data")
