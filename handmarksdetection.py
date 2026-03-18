import logging
import time

import cv2  # type: ignore
import mediapipe as mp  # type: ignore

logging.basicConfig()  # default is WARNING
logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

mp_holistic = mp.solutions.holistic
holistic_model = mp_holistic.Holistic(
    static_image_mode=False, min_detection_confidence=0.5, min_tracking_confidence=0.5
)

mp_drawing = mp.solutions.drawing_utils

videoCap = cv2.VideoCapture(0)


def handmarksDetector():
    try:
        t0 = time.perf_counter()
        while videoCap.isOpened():
            ret, frame = videoCap.read()

            if ret is False:
                logger.error("Couldn't fetch the frame.")
                break
            frame = cv2.resize(frame, (800, 600))

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = holistic_model.process(image)
            image.flags.writeable = True

            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS,
                mp_drawing.DrawingSpec(
                    color=(255, 0, 255), thickness=1, circle_radius=1
                ),
                mp_drawing.DrawingSpec(
                    color=(0, 255, 255), thickness=1, circle_radius=1
                ),
            )
            mp_drawing.draw_landmarks(
                image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS
            )

            mp_drawing.draw_landmarks(
                image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS
            )
            t1 = time.perf_counter()
            fps = 1 / (t1 - t0)
            t0 = t1
            cv2.putText(
                image,
                str(int(fps)) + " FPS",
                (10, 70),
                cv2.FONT_HERSHEY_COMPLEX,
                1,
                (0, 255, 0),
                2,
            )

            cv2.imshow("face, and hand landmarks", image)

            key = cv2.waitKey(1) & 0xFF

            if key in (ord("q"), 27):
                break
    except Exception as e:
        logging.exception("Unexpected error occured! %s", e)
    finally:
        videoCap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    handmarksDetector()
