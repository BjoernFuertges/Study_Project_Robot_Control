import robot_control_system.camera as camera
import argparse
import time

class SelfCamera:

    cam : camera.Camera
    path : str

    def __init__(self, path : str):
        self.cam = camera.Camera
        self.path = path

    def take_images(self):
        print("Press 'exit' to stop. Press any key to take a picture.")
        while True:
            user_input = input('Your input: ')
            if user_input == 'exit':
                break
            self.cam.take_picture(image_name=self.path + str(time.time_ns()))
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='With this tool you can take images with the robot camera')
    parser.add_argument('path', type=str,
                    help='Sets the path for the images')

    args = parser.parse_args()
    sc = SelfCamera(path=args.path)
    sc.take_images()