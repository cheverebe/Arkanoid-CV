import threading

from object_controllers.object_controller import ObjectController
from services.position.camera_position_service import CameraPositionService
from services.position.mouse_position_service import MousePositionService


class CameraHorizontalObjectController(ObjectController):
    def __init__(self, objects):
        super(CameraHorizontalObjectController, self).__init__(objects)
        # self.camera_tracking_service = CameraPositionService()
        self.camera_tracking_service = MousePositionService()
        self.camera_tracking_service.add_subscriber(self)

    def start(self):
        try:
            t=threading.Thread(target=self.camera_tracking_service.run)
            t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
            t.start()
        except:
            print "Error: unable to start thread"

    def update_objects_position(self, new_position):
        for obj in self.objects:
            obj_position = obj.get_position()
            obj_position[1] = new_position[1]
            obj.set_position(obj_position)

    def notify_position(self, new_position):
        self.update_objects_position(new_position)