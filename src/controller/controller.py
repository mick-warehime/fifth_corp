from event import EventListener, EventManager, events
from model import Model
from view import View
from pygame import Surface


class Controller(EventListener):
    view: View = None
    model: Model = None

    def __init__(self, event_manager: EventManager, screen: Surface) -> None:
        super(Controller, self).__init__(event_manager)
        self.screen = screen

    def notify(self, event: events.Event) -> None:
        # handle user inputs/ changes view/model
        if isinstance(event, events.InputEvent):
            self.handle_input(event)

    def handle_input(self, event: events.Event) -> None:
        raise NotImplementedError('subclasses must implement handle_input()')
