from objects.game_object import GameObject


class MovingObject(GameObject):

    def moves_independently(self):
        return False

    def get_speed(self):
        return self.speed

    def get_mass(self):
        return self.mass
