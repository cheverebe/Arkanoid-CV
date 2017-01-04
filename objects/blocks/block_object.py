from objects.moving_object import MovingObject


class BlockObject(MovingObject):

    SPRITE_PATH = 'img/sprites/block-triangle.png'

    def colliding_corners(self, other_object):
        if isinstance(other_object, BlockObject):
            return []
        return super(BlockObject, self).colliding_corners(other_object)
