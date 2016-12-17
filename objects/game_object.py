import cv2
import thread

from utils.image_utils import ImageUtils


class GameObject(object):
    SPRITE_PATH = 'img/sprites/ball.png'

    def __init__(self, start_position, resize_factor):
        self.sprite = cv2.imread(self.SPRITE_PATH)
        self.dimensions = self.sprite.shape[:2]
        self.adapt_size(resize_factor)
        self.position = start_position

    def collides(self, other_object):
        return False

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