import numpy as np

from objects.game_object import GameObject


class BoundaryGameObject(GameObject):
    def moves_independently(self):
        False

    def get_sprite(self):
        return self.temp_sprite

    def __init__(self, start_position, resize_factor, size, speed=[0, 0]):
        self.temp_sprite = np.zeros((size[0], size[1], 4), np.uint8)
        super(BoundaryGameObject, self).__init__(start_position, resize_factor, speed)

    def colliding_corners(self, other_object):
        if isinstance(other_object, BoundaryGameObject):
            return []
        return super(BoundaryGameObject, self).colliding_corners(other_object)
