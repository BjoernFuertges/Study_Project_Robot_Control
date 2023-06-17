class status_manager:
    name : str
    stop : bool
    speed : int
    direction : str
    turn : str
    radius : float
    passed_to_robot : bool

    def __init__(self, name) -> None:
        self.name = name
        self.stop = True
        self.speed = 100
        self.direction = 'forward'
        self.turn = 'no'
        self.radius = 0.8
        self.passed_to_robot = False

    def set_turn(self, turn : str) -> None:
        if turn == 'left' or turn == 'right' or turn == 'no':
            self.turn = turn
            self.passed_to_robot = False

    def set_turn_speed_radius(self, turn : str, speed : int, radius : float) -> None:
        if turn == 'left' or turn == 'right' or turn == 'no':
            self.turn = turn
            self.speed = speed
            self.radius = radius
            self.passed_to_robot = False

    def set_direction(self, direction : str) -> None:
        if direction == 'forward' or direction == 'backward' or direction == 'no':
            self.direction = direction
            self.passed_to_robot = False

    def set_direction_speed_radius(self, direction : str, speed : int, radius : float) -> None:
        if direction == 'forward' or direction == 'backward' or direction == 'no':
            self.direction = direction
            self.speed = speed
            self.radius = radius
            self.passed_to_robot = False

    def set_stop(self, stop : bool) -> None:
        self.stop = stop
        self.passed_to_robot = False
    