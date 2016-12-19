import threading

from object_controllers.object_controller import ObjectController
from services.position.mouse_position_service import MousePositionService


class HorizontalObjectController(ObjectController):
    def __init__(self, objects, position_service=MousePositionService):
        super(HorizontalObjectController, self).__init__(objects)
        self.camera_tracking_service = position_service()
        self.camera_tracking_service.add_subscriber(self)

    def start(self):
        try:
            t=threading.Thread(target=self.camera_tracking_service.run)
            t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
            t.start()
        except:
            print "Error: unable to start thread"

    def notify_position(self, new_position):
        obj_position = self.object.get_position()
        obj_position[1] = new_position[1]
        self.object.set_position(obj_position)