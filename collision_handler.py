import numpy as np
from services.time.time_service import TimeService


class CollisionHandler(object):
    def  __init__(self, objects=[], collision_handle_method=None):
        self.objects = objects
        self.time_service = TimeService.get_instance()
        self.time_service.add_subscriber(self)
        if not collision_handle_method:
            collision_handle_method = self.collision_handle
        self.collision_handle_method = collision_handle_method

    def notify_time(self, new_time):
        for game_object in self.objects:
            for other_object in self.objects:
                colliding_corners = game_object.colliding_corners(other_object)
                colliding_corners = colliding_corners if colliding_corners else self.invert_corners(
                    other_object.colliding_corners(game_object))
                if game_object != other_object and colliding_corners:
                    self.collision_handle_method(game_object, other_object, colliding_corners)

    @staticmethod
    def collision_handle(active_object, other_object, colliding_corners):
        new_speed = CollisionHandler.reflect_speed(active_object.get_speed(), colliding_corners)
        active_object.set_speed(new_speed)

    @staticmethod
    def reflect_speed(speed, colliding_corners):
        s = np.array(speed)
        if set(colliding_corners) == set([0]):
            return s * np.array([-1, -1])
        elif set(colliding_corners) == set([0, 1]):
            return s * np.array([1, -1])
        elif set(colliding_corners) == set([1]):
            return s * np.array([-1, -1])
        elif set(colliding_corners) == set([1, 2]):
            return s * np.array([-1, 1])
        elif set(colliding_corners) == set([2]):
            return s * np.array([-1, -1])
        elif set(colliding_corners) == set([2, 3]):
            return s * np.array([1, -1])
        elif set(colliding_corners) == set([3]):
            return s * np.array([-1, -1])
        elif set(colliding_corners) == set([3, 0]):
            return s * np.array([-1, 1])
        else:
            print colliding_corners
            raise ValueError

    @staticmethod
    def invert_corners(corners):
        inverted = []
        for corner in corners:
            if corner == 0:
                inverted.append(2)
            elif corner == 1:
                inverted.append(3)
            elif corner == 2:
                inverted.append(0)
            elif corner == 3:
                inverted.append(1)
        return inverted
