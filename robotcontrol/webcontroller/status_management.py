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
        self.radius = 0.0
        self.passed_to_robot = False

    def set_turn(self, turn : str) -> None:
        if turn == 'left' or turn == 'right' or turn == 'no':
            self.turn = turn
            self.passed_to_robot = False

    def set_turn_speed_radius(self, turn : str, speed : int, radius : float) -> None:
        if turn == 'left' or turn == 'right' or turn == 'no':
            self.turn = turn
            self.speed = speed
            self.set_radius(radius)
            self.passed_to_robot = False

    def set_direction(self, direction : str) -> None:
        if direction == 'forward' or direction == 'backward' or direction == 'no':
            self.direction = direction
            self.passed_to_robot = False

    def set_direction_speed_radius(self, direction : str, speed : int, radius : float) -> None:
        if direction == 'forward' or direction == 'backward' or direction == 'no':
            self.direction = direction
            self.speed = speed
            self.set_radius(radius)
            self.passed_to_robot = False

    def change_radius(self, radius : float) -> None:
        radiusTmp = self.radius + radius
        if radiusTmp >= 1:
            self.radius = 1
        elif radiusTmp <= 0:
            self.radius = 0
        else:
            self.radius = radiusTmp
        self.passed_to_robot = False

    def set_radius(self, radius : float, setPTR : bool = False) -> None:
        if radius >= 1:
            self.radius = 1
        elif radius <= 0:
            self.radius = 0
        else:
            self.radius = radius

        if setPTR:
            self.passed_to_robot = False

    def set_stop(self, stop : bool) -> None:
        self.stop = stop
        self.passed_to_robot = False
    