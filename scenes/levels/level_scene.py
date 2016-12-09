from objects.balls.ball_object import BallObject
from scenes.app_scene import AppScene


class LevelScene(AppScene):

    def __init__(self):
        super(LevelScene, self).__init__()

    def get_objects(self):
        return list(self._game_objects)

    def _init_objects(self):
        self._game_objects = []
        start_position = [
            int(float(self.dimensions[0]))/2,
            int(float(self.dimensions[1]))/2,
        ]
        ball = BallObject(start_position, self.resize_factor)
        self._game_objects.append(ball)

