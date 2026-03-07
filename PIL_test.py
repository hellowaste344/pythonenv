import random
import time

from PIL import ImageGrab


def screenshot():

    while True:
        seed = random.randint(1, 3)

        time.sleep(seed)

        snapshot = ImageGrab.grab()

        file_name = str(time.time()) + ".png"

        snapshot.save(file_name)


screenshot()
