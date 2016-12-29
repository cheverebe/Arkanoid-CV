import cv2
import numpy as np

from utils.image_utils import ImageUtils


class GameObject(object):
    SPRITE_PATH = 'img/sprites/ball.png'
    mass = 0

    def __init__(self, start_position, resize_factor, speed=[0, 0]):
        self.sprite = cv2.imread(self.SPRITE_PATH)
        self.dimensions = self.sprite.shape[:2]
        self.adapt_size(resize_factor)
        self.position = start_position
        self.speed = speed

    def colliding_corners(self, other_object):
        colliding_corners = []
        corners = other_object.get_corners()
        for i in range(len(corners)):
            if self.in_area(corners[i]):
                colliding_corners.append(i)
        return colliding_corners

    def get_image(self):
        return self.sprite

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
        return self

    def get_dimensions(self):
        return self.dimensions

    def adapt_size(self, resize_factor):
        self.sprite = ImageUtils.resize_image(self.sprite, resize_factor)
        self.dimensions = self.sprite.shape[:2]

    def adapt_position(self, resize_factor):
        self.position = [int(v*resize_factor) for v in self.position]

    def get_mass(self):
        return self.mass

    def moves_independently(self):
        raise NotImplementedError

    def get_corners(self):
        x_radius = int(self.dimensions[0]/2.0)
        y_radius = int(self.dimensions[1]/2.0)
        return [
            np.array(self.position) - [x_radius, y_radius],   # TOP LEFT
            np.array(self.position) - [-x_radius, y_radius],   # TOP RIGHT
            np.array(self.position) - [-x_radius, -y_radius],   # BOTTOM RIGHT
            np.array(self.position) - [x_radius, -y_radius],   # BOTTOM LEFT
        ]

    def in_area(self, position):
        x_radius = int(self.dimensions[0]/2.0)
        y_radius = int(self.dimensions[1]/2.0)
        x = self.position[0]
        y = self.position[1]
        return x + x_radius > position[0] > x - x_radius and y + y_radius > position[1] > y - y_radius

    def set_speed(self, new_speed):
        self.speed = new_speed

    def get_speed(self, new_speed):
        return self.speed
