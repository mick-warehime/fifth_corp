import pygame
from event import EventManager, Event, EventListener, InputEvent
from typing import Tuple
from .keybindings import Keybindings


# TODO - create mapping of keys to human readable 263 -> left arrow and a look up method
class Keyboard(EventListener):
    def __init__(self, event_manager: EventManager) -> None:
        super(Keyboard, self).__init__(event_manager)
        self.bindings = Keybindings()
        self.bindings.load()

    def notify(self, event: Event) -> None:
        if event == Event.TICK:
            self.handle_inputs()

    def handle_inputs(self) -> None:
        # Called for each game tick. We check our keyboard presses here.
        for pg_event in pygame.event.get():
            # handle window manager closing our window
            if pg_event.type == pygame.QUIT:
                self.event_manager.post(Event(Event.QUIT))
            # handle key down events
            elif pg_event.type == pygame.KEYDOWN:
                self.handle_keypress(pg_event)
            elif pg_event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click()

    def handle_keypress(self, pg_event: pygame.event) -> None:

        if pg_event.key == pygame.K_ESCAPE:
            self.event_manager.post(Event.QUIT)
        elif self.get_binding(pg_event.unicode) != Event.NONE:
            self.post_bound_event(key=pg_event.unicode)
        else:
            # post any other keys to the message queue for everyone
            # else to see
            self. post_input_event(Event.KEYDOWN, pg_event.unicode)

    def handle_mouse_click(self) -> None:
        self.post_input_event(
            InputEvent.MOUSE_CLICK,
            key=pygame.mouse.get_pressed())

    def post_input_event(self, event: Event, key: str = '') -> None:
        input = InputEvent(event=event, key=key, mouse=self.mouse_pos())
        self.event_manager.post(input)

    def mouse_pos(self) -> Tuple[int, int]:
        return pygame.mouse.get_pos()

    def get_binding(self, key: str) -> Event:
        return self.bindings.get_binding(key)

    def post_bound_event(self, key: str) -> None:
        binding = self.get_binding(key)
        event = self.bindings.event_for_binding(binding)
        return self.event_manager.post(Event(event))
