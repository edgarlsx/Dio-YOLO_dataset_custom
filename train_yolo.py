import subprocess

def train_yolo():
    command = "./darknet detector train data/obj.data yolov4-custom.cfg weights/yolov4.conv.137 -map"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    train_yolo()
