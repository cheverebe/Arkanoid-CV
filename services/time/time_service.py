import threading
import time


class TimeService(object):
    sleep_time = 0.02
    instance = None

    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_time_to_subscribers(self, t):
        for subscriber in self.subscribers:
            subscriber.notify_time(t)

    def run(self):
        while True:
            self.notify_time_to_subscribers(time.time())
            time.sleep(self.sleep_time)

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = TimeService()
            try:
                t = threading.Thread(target=cls.instance.run)
                t.daemon = True  # set thread to daemon ('ok' won't be printed in this case)
                t.start()
            except:
                print "Error: unable to start thread"
        return cls.instance
