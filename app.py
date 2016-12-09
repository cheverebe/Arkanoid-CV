import cv2

from scenes.levels.level_scene import LevelScene


class App(object):

    def __init__(self, name):
        self.window_name = name
        self._init_window()
        self._init_scene()
        self.running = True

    def run(self):
        while self.running:
            self._update_window()

    def _init_scene(self):
        self.scene = LevelScene()

    def _init_window(self):
        cv2.namedWindow(self.window_name)

    def _update_window(self):
        cv2.imshow(self.window_name, self.scene.get_image())
        cv2.waitKey(10)
