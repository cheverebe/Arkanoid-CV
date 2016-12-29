import numpy as np
from services.time.time_service import TimeService


class CollisionHandler(object):
    def __init__(self, objects=[]):
        self.objects = objects
        self.time_service = TimeService.get_instance()
        self.time_service.add_subscriber(self)

    def notify_time(self, new_time):
        for game_object in self.objects:
            for other_object in self.objects:
                colliding_corners = game_object.colliding_corners(other_object)
                if game_object != other_object and colliding_corners:
                    new_speed = self.reflect_speed(game_object.get_speed(), colliding_corners)
                    game_object.set_speed(new_speed)

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
        elif set(colliding_corners) == set([3, 1]):
            return s * np.array([-1, 1])
        else:
            raise ValueError
