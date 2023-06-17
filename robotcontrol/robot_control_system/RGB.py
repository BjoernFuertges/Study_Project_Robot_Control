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
        GPIO.setup(left_R, GPIO.OUT)
        GPIO.setup(left_G, GPIO.OUT)
        GPIO.setup(left_B, GPIO.OUT)
        GPIO.setup(right_R, GPIO.OUT)
        GPIO.setup(right_G, GPIO.OUT)
        GPIO.setup(right_B, GPIO.OUT)
        both_off()

    def both_on(self):
        GPIO.output(left_R, on)
        GPIO.output(left_G, on)
        GPIO.output(left_B, on)

        GPIO.output(right_R, on)
        GPIO.output(right_G, on)
        GPIO.output(right_B, on)


    def both_off(self):
        GPIO.output(left_R, off)
        GPIO.output(left_G, off)
        GPIO.output(left_B, off)

        GPIO.output(right_R, off)
        GPIO.output(right_G, off)
        GPIO.output(right_B, off)

    def side_on(self, side_X):
        GPIO.output(side_X, on)

    def side_off(self, side_X):
        GPIO.output(side_X, off)

    def police(self, police_time):
        for i in range (1,police_time):
            for i in range (1,3):
                side_on(left_R)
                side_on(right_B)
                time.sleep(0.1)
                both_off()
                side_on(left_B)
                side_on(right_R)
                time.sleep(0.1)
                both_off()
            for i in range (1,5):
                side_on(left_R)
                side_on(right_B)
                time.sleep(0.3)
                both_off()
                side_on(left_B)
                side_on(right_R)
                time.sleep(0.3)
                both_off()

    def red(self):
        side_on(right_R)
        side_on(left_R)

    def green(self):
        side_on(right_G)
        side_on(left_G)

    def blue(self):
        side_on(right_B)
        side_on(left_B)

    def yellow(self):
        red()
        green()    

    def pink(self):
        red()
        blue()

    def cyan(self):
        blue()
        green()

    def side_color_on(self, side_X,side_Y):
        GPIO.output(side_X, on)
        GPIO.output(side_Y, on)

    def side_color_off(self, side_X,side_Y):
        GPIO.output(side_X, off)
        GPIO.output(side_Y, off)

    def turn_left(self, times):
        for i in range(0,times):
            both_off()
            side_on(left_G)
            side_on(left_R)
            time.sleep(0.5)
            both_off()
            time.sleep(0.5)

    def turn_right(self, times):
        for i in range(1,times):
            both_off()
            side_on(right_G)
            side_on(right_R)
            time.sleep(0.5)
            both_off()
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
