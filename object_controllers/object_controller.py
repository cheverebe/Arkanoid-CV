

class ObjectController(object):
    def __init__(self, objects):
        self.objects = objects

    def start(self):
        raise NotImplementedError