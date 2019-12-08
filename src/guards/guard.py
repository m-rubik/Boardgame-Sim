

class Guard():

    number: int = None # Floor number
    active: bool = True
    base_movement_speed: int = None
    movement_speed: int = None
    x_coord: int = None
    y_coord: int = None

    def __init__(self, number):
        self.number = number
        self.base_movement_speed = number + 2

        