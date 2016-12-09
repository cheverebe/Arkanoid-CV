import cv2

from utils.image_utils import ImageUtils
from utils.screen_utils import ScreenUtils


class AppScene(object):
    BG_IMAGE = 'img/bg/level_bg.jpg'

    def __init__(self):
        self._init_window()
        self._init_objects()

    @staticmethod
    def render_object(game_object, image):
        ImageUtils.insert_sprite(game_object.get_image(), game_object.get_position(), image)

    def _init_objects(self):
        raise NotImplementedError

    def get_objects(self):
        raise NotImplementedError

    def get_image(self):
        image = self.background.copy()
        for game_object in self.get_objects():
            self.render_object(game_object, image)
        return image

    def _init_window(self):
        self.background = cv2.imread(self.BG_IMAGE)
        self.dimensions = self.background.shape[:2]
        self._adapt_to_screen()

    def _adapt_to_screen(self):
        screen_resolution = ScreenUtils.get_screen_resolution()
        screen_aspect_ratio = float(screen_resolution[0]) / screen_resolution[1]
        scene_aspect_ratio = float(self.dimensions[0]) / self.dimensions[1]

        if screen_aspect_ratio < scene_aspect_ratio:
            self.resize_factor = screen_resolution[0] / float(self.dimensions[0])
        else:
            self.resize_factor = screen_resolution[1] / float(self.dimensions[1])

        self.background = ImageUtils.resize_image(self.background, self.resize_factor)
        self.dimensions = self.background.shape[:2]
