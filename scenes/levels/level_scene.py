from object_controllers.horizontal_object_controller import HorizontalObjectController
from object_controllers.in_screen_horizontal_object_controller import InScreenHorizontalObjectController
from object_controllers.physics_object_controller import PhysicsObjectController
from objects.balls.ball_object import BallObject
from objects.tubes.tube_object import TubeObject
from scenes.app_scene import AppScene


class LevelScene(AppScene):

    def __init__(self):
        super(LevelScene, self).__init__()

    def get_objects(self):
        return list(self._game_objects)

    def _init_objects(self):
        self._game_objects = []
        ball_start_position = [
            int(float(self.dimensions[0]))/2,
            int(float(self.dimensions[1]))/2,
        ]
        ball = BallObject(ball_start_position, self.resize_factor)
        self._game_objects.append(ball)
        ball_controller = PhysicsObjectController(ball)

        tube_start_position = [
            int(float(self.dimensions[0])*3/4),
            int(float(self.dimensions[1])/2),
        ]
        tube = TubeObject(tube_start_position, self.resize_factor)

        controller = InScreenHorizontalObjectController(tube)
        controller.start()
        ball_controller.start()
        self._game_objects.append(tube)
