import numpy as np
from objects.game_object import GameObject


class BoundaryGameObject(GameObject):
    def moves_independently(self):
        False

    def __init__(self, start_position, resize_factor, size, speed=[0, 0]):
        super(BoundaryGameObject, self).__init__(start_position, resize_factor, speed)
        self.sprite = np.zeros((size[0], size[1], 4), np.uint8)