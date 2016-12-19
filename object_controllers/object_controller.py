

class ObjectController(object):
    def __init__(self, target_object):
        self.object = target_object

    def start(self):
        raise NotImplementedError

    def notify_position(self, new_position):
        raise NotImplementedError