import time


class TimeService(object):
    sleep_time = 0.05

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
