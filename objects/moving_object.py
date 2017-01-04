import numpy as np

from objects.game_object import GameObject


class MovingObject(GameObject):
    def __init__(self, start_position, resize_factor, speed=[0, 0]):
        super(MovingObject, self).__init__(start_position, resize_factor)
        self._init_speed = speed
        self.speed = speed

    def moves_independently(self):
        return False

    def get_speed(self):
        return self.speed

    def get_mass(self):
        return self.mass

    def colliding_corners(self, other_object):
        colliding_corners = []
        corners = self.get_corners()
        for i in range(len(corners)):
            if other_object.in_area(corners[i]):
                colliding_corners.append(i)
        return colliding_corners

    def adapt_position(self, resize_factor):
        self.position = [int(v * resize_factor) for v in self.position]

    def get_mass(self):
        return self.mass

    def moves_independently(self):
        raise NotImplementedError

    def get_corners(self):
        x_radius = int(self.dimensions[0] / 2.0)
        y_radius = int(self.dimensions[1] / 2.0)
        return [
            np.array(self.position) - [x_radius, y_radius],  # TOP LEFT
            np.array(self.position) - [-x_radius, y_radius],  # TOP RIGHT
            np.array(self.position) - [-x_radius, -y_radius],  # BOTTOM RIGHT
            np.array(self.position) - [x_radius, -y_radius],  # BOTTOM LEFT
        ]

    def in_area(self, position):
        corners = self.get_corners()
        mn = corners[0]
        mx = corners[2]
        return mn[0] <= position[0] and mn[1] <= position[1] and mx[0] >= position[0] and mx[1] >= position[1]

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self):
        return self.speed