import time
from picamera2 import Picamera2, Preview

class Camera:
    picam : Picamera2

    def __init__(self):
        self.picam = Picamera2()

        self.picam.start_preview(Preview.NULL)
        capture_config = self.picam.create_still_configuration()
        self.picam.configure(capture_config)

        self.picam.start()

    def take_picture(self, image_name : str):
        self.picam.capture_file(image_name)

    
    def __del__(self):
        self.picam.close()

if __name__ == '__main__':
    print("Hello at camera")
    c = Camera()
    c.take_picture(str(time.time())+".jpg")
