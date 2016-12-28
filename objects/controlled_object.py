from objects.game_object import GameObject


class ControlledObject(GameObject):

    def moves_independently(self):
        return True
