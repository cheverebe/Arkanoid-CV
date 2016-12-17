import thread

from object_controllers.object_controller import ObjectController
from utils.camera_tracking_service import CameraTrackingService


class CameraHorizontalObjectController(ObjectController):
    def __init__(self, objects):
        super(CameraHorizontalObjectController, self).__init__(objects)
        self.camera_tracking_service = CameraTrackingService()
        self.camera_tracking_service.add_subscriber(self)

    def start(self):
        try:
            thread.start_new_thread(self.camera_tracking_service.run())
        except:
            print "Error: unable to start thread"

    def update_objects_position(self, new_position):
        for obj in self.objects:
            obj_position = obj.get_position()
            obj_position[1] = new_position[1]
            obj.set_position(self, obj_position)

    def notify_position(self, new_position):
        self.update_objects_position(new_position)