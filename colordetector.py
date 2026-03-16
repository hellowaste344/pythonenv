import cv2  # type: ignore
import numpy as np

video = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = video.read()
        if not ret:
            print("Failed to capture frame, try again...")
            break

        cv2.imshow("frame", frame)
        # frame[height][width][color]
        means = np.mean(frame, axis=(0, 1))
        b_mean, g_mean, r_mean = means

        if max(b_mean, g_mean, r_mean) == b_mean:
            print("Blue")

        elif max(b_mean, g_mean, r_mean) == g_mean:
            print("Green")

        else:
            print("Red")

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == 27:
            break
except Exception as exc:
    print(f"Error occured: {exc}")

finally:
    video.release()
    cv2.destroyAllWindows()
