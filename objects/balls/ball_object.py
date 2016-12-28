from objects.moving_object import MovingObject


class BallObject(MovingObject):
    mass = 10

    def __init__(self, start_position, resize_factor, speed=[10, 10]):
        super(BallObject, self).__init__(start_position, resize_factor, speed)
