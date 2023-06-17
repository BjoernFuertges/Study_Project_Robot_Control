class Move_Command:
	stop_working : bool
	speed : int
	direction : str
	turn : str
	radius : float

	def __init__(self) -> None:
		self.stop_working = False
		self.speed = 0
		self.direction = 'forward'
		self.turn = 'no'
		self.radius = 0.0

	def set_stop_working(self, stop_working : bool) -> None:
		self.stop_working = stop_working

	def set_speed(self, speed : int) -> None:
		if speed >= 0:
			self.speed = speed

	def set_direction(self, direction : str) -> None:
		if direction == 'forward' or direction == 'backward' or direction == 'no':
			self.direction = direction

	def set_turn(self, turn : str) -> None:
		if turn == 'left' or turn == 'right' or turn == 'no':
			self.turn = turn

	def set_radius(self, radius : float) -> None:
		self.radius = radius

	def get_stop_working(self) -> bool:
		return self.stop_working

	def get_speed(self) -> int:
		return self.speed		
	
	def get_direction(self) -> str:
		return self.direction
	
	def get_turn(self) -> str:
		return self.turn
	
	def get_radius(self) -> float:
		return self.radius

	def to_string(self) -> str:
		return \
			"\nMove_Command: \n\t" + \
			"stop_working:" + 	str(self.stop_working) + "\n\t" + \
			"speed:" 		+ 	str(self.speed) + "\n\t" + \
			"direction:" 	+ 	str(self.direction) + "\n\t" + \
			"turn:" 		+ 	str(self.turn) + "\n\t" + \
			"radius:" 		+ 	str(self.radius) + "\n"