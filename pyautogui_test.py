import random
import time

import pyautogui


def screencapture():

    while True:
        seed = random.randint(1, 3)

        time.sleep(seed)

        snapshot = pyautogui.screenshot()

        file_name = str(time.time()) + ".png"

        snapshot.save(file_name)


screencapture()
