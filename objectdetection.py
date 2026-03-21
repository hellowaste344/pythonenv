import random
import time
from pathlib import Path

import cv2  # type: ignore
from ultralytics import YOLO  # type: ignore

"""
yolov8n.pt = Nano(fastest, less acurate)
yolov8s.pt = Small
yolov8l.pt = Large(slow, most accurate)
"""
model = YOLO("yolov8n.pt")

path = Path("sample.mp4")

cap = cv2.VideoCapture(str(path))


def getColours(cls_id):

    random.seed(cls_id)
    return tuple(random.randint(0, 255) for _ in range(3))  # (R,G,B)


frame_rate = 0

t0 = time.perf_counter()
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    for result in results:
        class_names = model.names
        for box in result.boxes:
            if box.conf[0] > 0.4:
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                cls = int(box.cls[0])
                class_name = class_names[cls]

                conf = float(box.conf[0])

                colour = getColours(cls)

                cv2.rectangle(frame, (x1, y1), (x2, y2), colour, 2)

                cv2.putText(
                    frame,
                    f"{class_name} {conf:.2f}",
                    (x1, max(y1 - 10, 20)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    colour,
                    2,
                )

    cv2.imshow("Yolo Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q") or cv2.waitKey(1) == 27:
        break

    frame_rate += 1
elapsed = time.perf_counter()

cap.release()
cv2.destroyAllWindows()

print(f"Fps: {frame_rate / (elapsed - t0):.4f}")
