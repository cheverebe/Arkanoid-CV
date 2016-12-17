class PositionService(object):
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def notify_position_to_subscribers(self, position):
        for subscriber in self.subscribers:
            subscriber.notify_position(position)

    def run(self):
        raise NotImplementedError