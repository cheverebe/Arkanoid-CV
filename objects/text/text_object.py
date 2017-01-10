

class TextObject(object):

    def __init__(self, start_position, text, scale, color=(255, 255, 255)):
        self.position = start_position
        self.scale = scale
        self.text = text
        self.color = color

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position
        return self

    def get_scale(self):
        return self.scale

    def set_scale(self, scale):
        self.scale = scale
        return self

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color
        return self

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.color = text
        return self
