import time
from picamera2 import Picamera2, Preview


def run():
    picam = Picamera2()

    config = picam.create_preview_configuration()
    picam.configure(config)

    picam.start_preview(Preview.QTGL)

    picam.start()
    time.sleep(2)
    picam.capture_file("test-python.jpg")

    picam.close()
    print("image saved")