import os
import json
import glob
from PIL import Image

def convert_labelme_to_yolo(json_dir, output_img_dir, output_label_dir, class_names):
    os.makedirs(output_img_dir, exist_ok=True)
    os.makedirs(output_label_dir, exist_ok=True)

    for json_file in glob.glob(f"{json_dir}/*.json"):
        with open(json_file) as f:
            data = json.load(f)

        img_path = os.path.join(json_dir, data["imagePath"])
        img = Image.open(img_path)
        w, h = img.size

        # Copy image to dataset folder
        img.save(os.path.join(output_img_dir, data["imagePath"]))

        # Create YOLO label file
        label_path = os.path.join(output_label_dir, data["imagePath"].replace('.jpg', '.txt'))
        with open(label_path, 'w') as out_file:
            for shape in data['shapes']:
                label = shape['label']
                cls_id = class_names.index(label)

                # bounding box
                points = shape['points']
                xmin = min(p[0] for p in points)
                xmax = max(p[0] for p in points)
                ymin = min(p[1] for p in points)
                ymax = max(p[1] for p in points)

                x_center = ((xmin + xmax) / 2) / w
                y_center = ((ymin + ymax) / 2) / h
                bbox_width = (xmax - xmin) / w
                bbox_height = (ymax - ymin) / h

                out_file.write(f"{cls_id} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}\n")

if __name__ == "__main__":
    classes = ['garrafa', 'copo']
    convert_labelme_to_yolo(
        json_dir='data/labelme_json',
        output_img_dir='data/images/train',
        output_label_dir='data/labels/train',
        class_names=classes
    )
