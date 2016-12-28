import numpy as np

class PsysicsUtils(object):
    @staticmethod
    def new_position(current_position, speed, time_delta):
        return current_position + speed * np.array(time_delta)

    @staticmethod
    def new_speed(current_speed, mass, time_delta, other_forces=[]):
        total_force = sum(other_forces)
        acceleration = total_force / mass
        speed_delta = acceleration * time_delta
        return current_speed + speed_delta
