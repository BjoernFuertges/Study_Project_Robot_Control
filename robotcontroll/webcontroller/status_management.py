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