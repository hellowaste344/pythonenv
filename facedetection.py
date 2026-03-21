import logging

import cv2  # type: ignore

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0)


def face_detector():

    if face_cascade.empty():
        logger.error("Failed to load Haar cascade")
        exit()

    if not cap.isOpened():
        logger.error("Failed to open camera")
        exit()

    while True:
        ret, frame = cap.read()

        if not ret:
            logger.error("Error: couldn't fetch the frame")
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Face detection: ", frame)

        if cv2.waitKey(1) >= 0:
            break


if __name__ == "__main__":
    face_detector()
    cap.release()
    cv2.destroyAllWindows()
