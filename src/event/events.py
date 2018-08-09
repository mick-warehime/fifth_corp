from typing import Tuple
from enum import Enum


class Event(Enum):
    NONE = 'none'
    QUIT = 'quit'
    TICK = 'tick'
    OPEN_SETTINGS = 'open settings'
    CLOSE_SETTINGS = 'close settings'
    KEYDOWN = 'keydown'
    KEYUP = 'keyup'
    MOUSE_CLICK = 'mouse click'

    # comparing enums gives wrong result without this
    # has to do with this file being imported twice
    # but i can't for the life of me figure out why/how/where
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Enum):
            return self.value == other.value
        return False


class InputEvent(object):

    def __init__(self, event: Event, key: str,
                 mouse: Tuple[int, int] = (-1, -1)) -> None:
        self.event = event
        self.key = key
        self.mouse = mouse

    def __str__(self) -> str:
        return '%s, key=%s, mouse=%s' % (self.event, self.key, self.mouse)
