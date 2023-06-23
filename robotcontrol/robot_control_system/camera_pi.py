import time
from picamera2 import Picamera2, Preview


def run():
    picam = Picamera2()

    picam2.start_preview(Preview.NULL)
    capture_config = picam2.create_still_configuration()
    picam2.configure(capture_config)

    picam2.start()
    time.sleep(2)
    picam2.capture_file("test-python.jpg")

    picam2.close()
    print("image saved")