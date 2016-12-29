from collision_handler import CollisionHandler
from object_controllers.in_screen_horizontal_object_controller import InScreenHorizontalObjectController
from object_controllers.physics_object_controller import PhysicsObjectController
from objects.balls.ball_object import BallObject
from objects.boundary_object import BoundaryGameObject
from objects.tubes.tube_object import TubeObject
from scenes.app_scene import AppScene


class LevelScene(AppScene):

    def __init__(self):
        super(LevelScene, self).__init__()

    def get_objects(self):
        return list(self._game_objects)

    def _init_boundaries(self):
        vertical_boundary_size = [30, self.dimensions[1]]
        # LEFT------------------------------
        left_bound_start_position = [
            0,
            int(float(self.dimensions[1]))/2,
        ]
        left_bound = BoundaryGameObject(left_bound_start_position, self.resize_factor, vertical_boundary_size)
        self._game_objects.append(left_bound)

        # RIGHT------------------------------
        right_bound_start_position = [
            self.dimensions[0],
            int(float(self.dimensions[1]))/2,
        ]
        right_bound = BoundaryGameObject(right_bound_start_position, self.resize_factor, vertical_boundary_size)
        self._game_objects.append(right_bound)

        horizontal_boundary_size = [self.dimensions[0], 30]
        # TOP------------------------------
        top_bound_start_position = [
            int(float(self.dimensions[0]))/2,
            0
        ]
        top_bound = BoundaryGameObject(top_bound_start_position, self.resize_factor, horizontal_boundary_size)
        self._game_objects.append(top_bound)

        # BOTTOM------------------------------
        bottom_bound_start_position = [
            int(float(self.dimensions[0]))/2,
            self.dimensions[1]
        ]
        bottom_bound = BoundaryGameObject(bottom_bound_start_position, self.resize_factor, horizontal_boundary_size)
        self._game_objects.append(bottom_bound)


    def _init_objects(self):
        self._game_objects = []
        self._init_boundaries()
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
        ch = CollisionHandler(self._game_objects)
