import listener
from event_manager import EventManager
import events


class EventListener(listener.Listener):

    def __init__(self, event_manager: EventManager) -> None:
        event_manager.register(self)
        self.event_manager = event_manager

    def notify(self, event: events.Event) -> None:
        pass
