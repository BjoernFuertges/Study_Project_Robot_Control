#!/usr/bin/env python3
# File name   : move.py
# Description : Control Motor
# Product     : GWR
# Website     : www.gewbot.com
# Author      : William
# Date        : 2019/07/24
import time
import RPi.GPIO as GPIO
import RGB as RGB
from move_command import Move_Command

import random # TEST

class Move:

	# motor_EN_A: Pin7  |  motor_EN_B: Pin11
	# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12



	rgb : RGB.RGB

	def __init__(self):#Motor initialization
		# from RPIservo
		self.sc_direction = [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1]
		self.initPos = [init_pwm0,init_pwm1,init_pwm2,init_pwm3,
						init_pwm4,init_pwm5,init_pwm6,init_pwm7,
						init_pwm8,init_pwm9,init_pwm10,init_pwm11,
						init_pwm12,init_pwm13,init_pwm14,init_pwm15]
		self.goalPos = [300,300,300,300, 300,300,300,300 ,300,300,300,300 ,300,300,300,300]
		self.nowPos  = [300,300,300,300, 300,300,300,300 ,300,300,300,300 ,300,300,300,300]
		self.bufferPos  = [300.0,300.0,300.0,300.0, 300.0,300.0,300.0,300.0 ,300.0,300.0,300.0,300.0 ,300.0,300.0,300.0,300.0]
		self.lastPos = [300,300,300,300, 300,300,300,300 ,300,300,300,300 ,300,300,300,300]
		self.ingGoal = [300,300,300,300, 300,300,300,300 ,300,300,300,300 ,300,300,300,300]
		self.maxPos  = [560,560,560,560, 560,560,560,560 ,560,560,560,560 ,560,560,560,560]
		self.minPos  = [100,100,100,100, 100,100,100,100 ,100,100,100,100 ,100,100,100,100]
		self.scSpeed = [0,0,0,0, 0,0,0,0 ,0,0,0,0 ,0,0,0,0]

		self.ctrlRangeMax = 560
		self.ctrlRangeMin = 100
		self.angleRange = 180

		'''
		scMode: 'init' 'auto' 'certain' 'quick' 'wiggle'
		'''
		self.scMode = 'auto'
		self.scTime = 2.0
		self.scSteps = 30
		
		self.scDelay = 0.037
		self.scMoveTime = 0.037

		self.goalUpdate = 0
		self.wiggleID = 0
		self.wiggleDirection = 1

		# END

		self.Motor_A_EN    = 4
		self.Motor_B_EN    = 17

		self.Motor_A_Pin1  = 14
		self.Motor_A_Pin2  = 15
		self.Motor_B_Pin1  = 27
		self.Motor_B_Pin2  = 18

		self.Dir_forward   = 0
		self.Dir_backward  = 1

		self.left_forward  = 0
		self.left_backward = 1

		self.right_forward = 0
		self.right_backward= 1

		self.pwm_A = 0
		self.pwm_B = 0

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

		print(self.pwm_A)
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
		print("ml: " + str(status) + ", " + str(direction) + ", " + str(speed))
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
		print("mr: " + str(status) + ", " + str(direction) + ", " + str(speed))
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

	def pwmGenOut(self, angleInput):
		return int(round(((self.ctrlRangeMax-self.ctrlRangeMin)/self.angleRange*angleInput),0))

	def moveAngle(self, ID, angleInput):
		self.nowPos[ID] = int(self.initPos[ID] + self.sc_direction[ID]*self.pwmGenOut(angleInput))
		if self.nowPos[ID] > self.maxPos[ID]:self.nowPos[ID] = self.maxPos[ID]
		elif self.nowPos[ID] < self.minPos[ID]:self.nowPos[ID] = self.minPos[ID]
		self.lastPos[ID] = self.nowPos[ID]
		self.pwm_B.set_pwm(ID, 0, self.nowPos[ID])

	def move_handler(self, in_q, stop) -> None:
		while stop() != True:
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
		#m.move(speed_set, 'forward', 'left', 0.8)
		while 1:
			m.moveAngle(0,(random.random()*100-50))
			time.sleep(1)
			m.moveAngle(1,(random.random()*100-50))
			time.sleep(1)
		#time.sleep(1.3)
		m.motorStop()
		m.rgb.green()
		del m
		print("that is the end")
	except KeyboardInterrupt:
		del m
