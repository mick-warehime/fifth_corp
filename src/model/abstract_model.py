from event import EventManager, EventListener, events


class Model(EventListener):
    def __init__(self, event_manager: EventManager) -> None:
        super(Model, self).__init__(event_manager)

    def notify(self, event: events.Event) -> None:
        pass
