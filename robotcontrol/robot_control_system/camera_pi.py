import time
from picamera2 import Picamera2


def run():
    picam = Picamera2()

    picam.configure(config)

    picam.start()
    time.sleep(2)
    picam.capture_file("test-python.jpg")

    picam.close()
    print("image saved")