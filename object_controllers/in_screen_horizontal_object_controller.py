from object_controllers.horizontal_object_controller import HorizontalObjectController
from utils.screen_utils import ScreenUtils


class InScreenHorizontalObjectController(HorizontalObjectController):
    def notify_position(self, new_position):
        new_position = self.limit_horizontal_position(new_position)
        super(InScreenHorizontalObjectController, self).notify_position(new_position)

    def limit_horizontal_position(self, new_position):
        height, width = self.object.get_dimensions()
        left_radius = width / 2
        right_radius = width - left_radius
        lower_limit = left_radius
        screen_h, screen_w = ScreenUtils.get_screen_resolution()
        upper_limit = screen_w - right_radius
        x, y = new_position
        y = min(max(lower_limit, y), upper_limit)
        return x, y