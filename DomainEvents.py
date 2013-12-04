__author__ = 'erik.ashepa'


class DomainEvents:
    def __init__(self):
        pass

    handlers = list()

    @staticmethod
    def publish(event):
        for handler in DomainEvents.handlers:
            if event.__class__.__name__ + "Handler" == handler.__class__.__name__:
                handler.handle(event)

    @staticmethod
    def register(handler):
        DomainEvents.handlers.append(handler)