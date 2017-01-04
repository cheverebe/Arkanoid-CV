import cv2

from utils.image_utils import ImageUtils


class GameObject(object):
    SPRITE_PATH = 'img/sprites/ball.png'
    mass = 0

    def get_sprite(self):
        return cv2.imread(self.SPRITE_PATH, -1)

    def __init__(self, start_position, resize_factor):
        self.sprite = self.get_sprite()
        self.position = start_position
        self.dimensions = self.sprite.shape[:2]
        self.adapt_size(resize_factor)

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
