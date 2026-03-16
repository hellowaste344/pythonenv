import os
import random
import sys
from pathlib import Path

import mss
import sounddevice as sd
from ultralytics import YOLO

print(os.path.dirname(__file__))
print(os.path.abspath(__file__))
print(os.path.realpath(__file__))
print(sys.platform)
print("#" * 50)

seed = random.randint(0, 3)

opts = ("a", "b", "c", "d")
print(type(opts))
print(opts[seed])

print(sd.query_devices())

path = Path("~/Documents/cutecat.jpg").expanduser()
print(path)


model = YOLO("yolov8n.pt")
print(model.names)

with mss.mss() as sct:
    for i in range(len(sct.monitors)):
        print(sct.monitors[i])
