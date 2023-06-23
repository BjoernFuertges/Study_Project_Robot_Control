import time
from picamera2 import Picamera2, Preview


def run():
    picam = Picamera2()

    picam.start_preview(Preview.NULL)
    capture_config = picam.create_still_configuration()
    picam.configure(capture_config)

    picam.start()
    time.sleep(2)
    picam.capture_file("test-python.jpg")

    picam.close()
    print("image saved")