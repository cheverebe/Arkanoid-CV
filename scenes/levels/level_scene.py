import cv2

from collision_handler import CollisionHandler
from object_controllers.in_screen_horizontal_object_controller import InScreenHorizontalObjectController
from object_controllers.physics_object_controller import PhysicsObjectController
from objects.balls.ball_object import BallObject
from objects.blocks.block_object import BlockObject
from objects.boundaries.boundary_object import BoundaryGameObject
from objects.tubes.tube_object import TubeObject
from scenes.app_scene import AppScene


class LevelScene(AppScene):

    def __init__(self):
        super(LevelScene, self).__init__()
        self.lives_left = 4
        self.score = 0

    def get_objects(self):
        return list(self._game_objects)

    def _init_boundaries(self):
        gap = 10
        vertical_boundary_size = [self.dimensions[0], 30]
        # LEFT------------------------------
        left_bound_start_position = [
            int(float(self.dimensions[0]))/2,
            gap,
        ]
        left_bound = BoundaryGameObject(left_bound_start_position, 1, vertical_boundary_size)
        self._game_objects.append(left_bound)

        # RIGHT------------------------------
        right_bound_start_position = [
            int(float(self.dimensions[0]))/2,
            self.dimensions[1] - gap,
        ]
        right_bound = BoundaryGameObject(right_bound_start_position, 1, vertical_boundary_size)
        self._game_objects.append(right_bound)

        horizontal_boundary_size = [30, self.dimensions[1]]
        # # TOP------------------------------
        top_bound_start_position = [
            gap,
            int(float(self.dimensions[1]))/2,
        ]
        top_bound = BoundaryGameObject(top_bound_start_position, 1, horizontal_boundary_size)
        self._game_objects.append(top_bound)

        # BOTTOM------------------------------
        bottom_bound_start_position = [
            self.dimensions[0]-gap,
            int(float(self.dimensions[1]))/2,
        ]
        bottom_bound = BoundaryGameObject(bottom_bound_start_position, 1, horizontal_boundary_size)
        self._game_objects.append(bottom_bound)
        self.bottom_boundary = bottom_bound

    def _init_blocks(self):
        self.blocks_left = 0

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2),
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)+100,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)-100,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)+200,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)-200,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)+300,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4),
            int(float(self.dimensions[1])/2)-300,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2),
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)+100,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)-100,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)+200,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)-200,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)+300,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

        block_start_position = [
            int(float(self.dimensions[0])*1/4)+80,
            int(float(self.dimensions[1])/2)-300,
        ]
        block = BlockObject(block_start_position, self.resize_factor)
        self._game_objects.append(block)
        self.blocks_left += 1

    def _init_objects(self):
        self._game_objects = []
        self._text_objects = []

        self._init_boundaries()
        self._init_blocks()

        ball_start_position = self.ball_init_pos()
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
        ch = CollisionHandler(self._game_objects, self.handle_collision)

    def handle_collision(self, active_object, other_object, colliding_corners):
        if isinstance(active_object, BallObject) and other_object == self.bottom_boundary:
            self.ball_drop(active_object)
        if isinstance(active_object, BallObject) and isinstance(other_object, BlockObject):
            CollisionHandler.collision_handle(active_object, other_object, colliding_corners)
            self.block_destroy(other_object)
            self.blocks_left -= 1
            self.check_end()
        else:
            CollisionHandler.collision_handle(active_object, other_object, colliding_corners)

    def ball_drop(self, ball):
        self.lives_left -= 1
        ball.set_position(self.ball_init_pos())

    def ball_init_pos(self):
        return [
            int(float(self.dimensions[0]))/2,
            int(float(self.dimensions[1]))/2,
        ]

    def block_destroy(self, block):
        self._game_objects.remove(block)
        self.score += 10
        print self.score

    def check_end(self):
        if self.blocks_left == 0:
            cv2.destroyAllWindows()
            raise Exception