#!/usr/bin/python3
# File name   : motor.py
# Description : Control LEDs 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

# Lamps at the front

import RPi.GPIO as GPIO
import time

class RGB:

    left_R = 22
    left_G = 23
    left_B = 24

    right_R = 10
    right_G = 9
    right_B = 25

    on  = GPIO.LOW
    off = GPIO.HIGH
    
    def __init__(self):#initialization
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_R, GPIO.OUT)
        GPIO.setup(self.left_G, GPIO.OUT)
        GPIO.setup(self.left_B, GPIO.OUT)
        GPIO.setup(self.right_R, GPIO.OUT)
        GPIO.setup(self.right_G, GPIO.OUT)
        GPIO.setup(self.right_B, GPIO.OUT)
        self.both_off()

    def __del__(self):
        self.both_off()
        GPIO.cleanup()

    def both_on(self):
        GPIO.output(self.left_R, self.on)
        GPIO.output(self.left_G, self.on)
        GPIO.output(self.left_B, self.on)

        GPIO.output(self.right_R, self.on)
        GPIO.output(self.right_G, self.on)
        GPIO.output(self.right_B, self.on)


    def both_off(self):
        GPIO.output(self.left_R, self.off)
        GPIO.output(self.left_G, self.off)
        GPIO.output(self.left_B, self.off)

        GPIO.output(self.right_R, self.off)
        GPIO.output(self.right_G, self.off)
        GPIO.output(self.right_B, self.off)

    def side_on(self, side_X):
        GPIO.output(side_X, self.on)

    def side_off(self, side_X):
        GPIO.output(side_X, self.off)

    def police(self, police_time):
        for i in range (1,police_time):
            for i in range (1,3):
                self.side_on(self.left_R)
                self.side_on(self.right_B)
                time.sleep(0.1)
                self.both_off()
                self.side_on(self.left_B)
                self.side_on(self.right_R)
                time.sleep(0.1)
                self.both_off()
            for i in range (1,5):
                self.side_on(self.left_R)
                self.side_on(self.right_B)
                time.sleep(0.3)
                self.both_off()
                self.side_on(self.left_B)
                self.side_on(self.right_R)
                time.sleep(0.3)
                self.both_off()

    def red(self):
        self.side_on(self.right_R)
        self.side_on(self.left_R)

    def green(self):
        self.side_on(self.right_G)
        self.side_on(self.left_G)

    def blue(self):
        self.side_on(self.right_B)
        self.side_on(self.left_B)

    def yellow(self):
        self.red()
        self.green()    

    def pink(self):
        self.red()
        self.blue()

    def cyan(self):
        self.blue()
        self.green()

    def side_color_on(self, side_X,side_Y):
        GPIO.output(side_X, self.on)
        GPIO.output(side_Y, self.on)

    def side_color_off(self, side_X,side_Y):
        GPIO.output(side_X, self.off)
        GPIO.output(side_Y, self.off)

    def turn_left(self, times):
        for i in range(0,times):
            self.both_off()
            self.side_on(self.left_G)
            self.side_on(self.left_R)
            time.sleep(0.5)
            self.both_off()
            time.sleep(0.5)

    def turn_right(self, times):
        for i in range(1,times):
            self.both_off()
            self.side_on(self.right_G)
            self.side_on(self.right_R)
            time.sleep(0.5)
            self.both_off()
            time.sleep(0.5)

if __name__ == '__main__':
    rgb = RGB()
    rgb.police(4)
    rgb.both_on()
    rgb.time.sleep(1)
    rgb.both_off()
    rgb.yellow()
    rgb.time.sleep(5)
    rgb.both_off()
    rgb.pink()
    rgb.time.sleep(5)
    rgb.both_off()
    rgb.cyan()
    time.sleep(5)
    rgb.both_off()
