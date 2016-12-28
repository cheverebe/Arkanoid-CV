import threading

from object_controllers.object_controller import ObjectController
from services.time.time_service import TimeService
from utils.physics_utils import PsysicsUtils


class PhysicsObjectController(ObjectController):
    def __init__(self, object):
        super(PhysicsObjectController, self).__init__(object)
        self.time_service = TimeService()
        self.time_service.add_subscriber(self)
        self.last_time = None

    def start(self):
        try:
            t=threading.Thread(target=self.time_service.run)
            t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
            t.start()
        except:
            print "Error: unable to start thread"

    def notify_time(self, new_time):
        if self.last_time is not None:
            obj_position = self.object.get_position()
            obj_speed = self.object.get_speed()
            time_delta = new_time - self.last_time
            new_position = PsysicsUtils.new_position(obj_position, obj_speed, time_delta)
            self.object.set_position(new_position)
        self.last_time = new_time