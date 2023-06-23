from picamera2 import Picamera2, Preview

class Camera:
    picam : Picamera2

    def __init__(self):
        picam = Picamera2()

        picam.start_preview(Preview.NULL)
        capture_config = picam.create_still_configuration()
        picam.configure(capture_config)

    def take_picture(self, image_name : str):
        picam.start()
        picam.capture_file(image_name)

        picam.close()