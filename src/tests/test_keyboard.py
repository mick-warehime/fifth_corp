from unittest.mock import patch
from unittest import TestCase
from input import Keyboard
from typing import Any


class KeyboardTest(TestCase):

    @patch('event.EventManager')
    def get_keyboard(self, EventManager: Any) -> None:
        self.keyboard = Keyboard(EventManager())

    def setUp(self) -> None:
        self.get_keyboard()

    def test_keydown(self) -> None:
        pass

        # need to figureout hot to mock pygame.events
        # self.keyboard.get_pygame_events = MagicMock(return_value=[{'unicode': 'x'}])
        # self.keyboard.notify(Event.TICK)
