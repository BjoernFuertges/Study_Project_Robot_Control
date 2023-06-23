#!/usr/bin/env python3
# File name   : move.py
# Description : Control Motor
# Product     : GWR
# Website     : www.gewbot.com
# Author      : William
# Date        : 2019/07/24
import os
import time
import shutil
import RPi.GPIO as GPIO
import robot_control_system.RGB as RGB
from robot_control_system.move_command import Move_Command
from robot_control_system.camera import Camera

class Move:

	# motor_EN_A: Pin7  |  motor_EN_B: Pin11
	# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

	Motor_A_EN    = 4
	Motor_B_EN    = 17

	Motor_A_Pin1  = 14
	Motor_A_Pin2  = 15
	Motor_B_Pin1  = 27
	Motor_B_Pin2  = 18

	Dir_forward   = 0
	Dir_backward  = 1

	left_forward  = 0
	left_backward = 1

	right_forward = 0
	right_backward= 1

	pwm_A = 0
	pwm_B = 0

	rgb : RGB.RGB
	camera : Camera
	tmp_img_folder : str

	def __init__(self, tmp_img_folder : str):#Motor initialization
		self.tmp_img_folder = tmp_img_folder
		if os.path.isdir(self.tmp_img_folder):
			shutil.rmtree(self.tmp_img_folder)

		os.mkdir(self.tmp_img_folder)


		self.camera = Camera()
		
		self.rgb = RGB.RGB()
		
		self.rgb.red()

		GPIO.setwarnings(False)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.Motor_A_EN, GPIO.OUT)
		GPIO.setup(self.Motor_B_EN, GPIO.OUT)
		GPIO.setup(self.Motor_A_Pin1, GPIO.OUT)
		GPIO.setup(self.Motor_A_Pin2, GPIO.OUT)
		GPIO.setup(self.Motor_B_Pin1, GPIO.OUT)
		GPIO.setup(self.Motor_B_Pin2, GPIO.OUT)

		self.motorStop()
		try:
			self.pwm_A = GPIO.PWM(self.Motor_A_EN, 1000)
			self.pwm_B = GPIO.PWM(self.Motor_B_EN, 1000)
		except:
			pass

		self.rgb.blue()

	def __del__(self):
		self.motorStop()
		del rgb
		GPIO.cleanup()             # Release resource

	def motorStop(self) -> None:#Motor stops
		GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
		GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
		GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
		GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
		GPIO.output(self.Motor_A_EN, GPIO.LOW)
		GPIO.output(self.Motor_B_EN, GPIO.LOW)




	def motor_left(self, status : int, direction : int, speed : int) -> None:#Motor 2 positive and negative rotation
		if status == 0: # stop
			GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
			GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
			GPIO.output(self.Motor_B_EN, GPIO.LOW)
		else:
			if direction == self.Dir_backward:
				GPIO.output(self.Motor_B_Pin1, GPIO.HIGH)
				GPIO.output(self.Motor_B_Pin2, GPIO.LOW)
				self.pwm_B.start(100)
				self.pwm_B.ChangeDutyCycle(speed)
			elif direction == self.Dir_forward:
				GPIO.output(self.Motor_B_Pin1, GPIO.LOW)
				GPIO.output(self.Motor_B_Pin2, GPIO.HIGH)
				self.pwm_B.start(0)
				self.pwm_B.ChangeDutyCycle(speed)


	def motor_right(self, status : int, direction : int, speed : int) -> None:#Motor 1 positive and negative rotation
		if status == 0: # stop
			GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
			GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
			GPIO.output(self.Motor_A_EN, GPIO.LOW)
		else:
			if direction == self.Dir_forward:#
				GPIO.output(self.Motor_A_Pin1, GPIO.HIGH)
				GPIO.output(self.Motor_A_Pin2, GPIO.LOW)
				self.pwm_A.start(100)
				self.pwm_A.ChangeDutyCycle(speed)
			elif direction == self.Dir_backward:
				GPIO.output(self.Motor_A_Pin1, GPIO.LOW)
				GPIO.output(self.Motor_A_Pin2, GPIO.HIGH)
				self.pwm_A.start(0)
				self.pwm_A.ChangeDutyCycle(speed)


	def move(self, speed : int, direction : str, turn : str, radius : float = 0.6):   # 0 < radius <= 1  
		#speed = 100
		if direction == 'forward':
			if turn == 'right':
				self.motor_left(0, self.left_backward, int(speed*radius))
				self.motor_right(1, self.right_forward, speed)
			elif turn == 'left':
				self.motor_left(1, self.left_forward, speed)
				self.motor_right(0, self.right_backward, int(speed*radius))
			else:
				self.motor_left(1, self.left_forward, speed)
				self.motor_right(1, self.right_forward, speed)
		elif direction == 'backward':
			if turn == 'right':
				self.motor_left(0, self.left_forward, int(speed*radius))
				self.motor_right(1, self.right_backward, speed)
			elif turn == 'left':
				self.motor_left(1, self.left_backward, speed)
				self.motor_right(0, self.right_forward, int(speed*radius))
			else:
				self.motor_left(1, self.left_backward, speed)
				self.motor_right(1, self.right_backward, speed)
		elif direction == 'no':
			if turn == 'right':
				self.motor_left(1, self.left_backward, speed)
				self.motor_right(1, self.right_forward, speed)
			elif turn == 'left':
				self.motor_left(1, self.left_forward, speed)
				self.motor_right(1, self.right_backward, speed)
			else:
				self.motorStop()
		else:
			pass

	# picture_intervall in ms
	def move_handler(self, in_q, stop, picture_intervall : int) -> None:
		ts_last_picture = 0
		while stop() != True:
			ts_now = int(time.time())
			print(ts_last_picture)
			print(ts_now)
			if ts_last_picture + picture_intervall >= ts_now:
				print("Take picture!")
				ts_last_picture = ts_now
				camera.take_picture(self.tmp_img_folder + "/" + str(ts_now) + ".jpg")

			# Get some data
			mc = in_q.get()

			if mc != None:
				if mc.get_stop_working():
					self.motorStop()
					self.rgb.pink()
					in_q.task_done()
					continue
				
				self.rgb.green()
				self.move(mc.get_speed(), mc.get_direction(), mc.get_turn(), mc.get_radius())
				in_q.task_done()

			# Process the data..
			# Indicate completion
			#in_q.task_done()
		

if __name__ == '__main__':
	m : Move
	try:
		speed_set = 100
		m = Move()
		m.rgb.yellow()
		m.move(speed_set, 'forward', 'no', 0.8)
		time.sleep(1.3)
		m.motorStop()
		m.rgb.green()
		del m
		print("that is the end")
	except KeyboardInterrupt:
		del m
