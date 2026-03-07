import random
import time

import mss


def screenshot():

    while True:
        seed = random.randint(1, 3)

        time.sleep(seed)

        file_name = str(time.time()) + ".png"

        with mss.mss() as sct:
            sct.shot(output=file_name)


screenshot()
