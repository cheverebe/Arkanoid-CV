import autopy
import time

from services.position.position_service import PositionService


class MousePositionService(PositionService):
    def run(self):
        while True:
            pos_y, pos_x = autopy.mouse.get_pos()
            self.notify_position_to_subscribers((pos_x, pos_y))
            time.sleep(0.05)
