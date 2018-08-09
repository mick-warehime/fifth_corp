from event import EventManager, EventListener, Event
from controller import Controller, LaunchController, SettingsController
from input import Keyboard
import sys
from pygame.time import Clock
from constants import constants
import pygame
from enum import Enum


class GameState(Enum):
    SETTINGS = 1
    LOAD_SCREEN = 2


class Game(EventListener):
    keyboard: Keyboard = None
    event_manager: EventManager = None
    controller: Controller = None
    state: GameState = None

    def __init__(self) -> None:
        self.event_manager = EventManager()
        super(Game, self).__init__(self.event_manager)
        self.inialize_pygame()

        self.clock: pygame.Clock = Clock()
        self.screen: pygame.Surface = pygame.display.set_mode(
            constants.SCREEN_SIZE)

        self.keyboard = Keyboard(self.event_manager)

        self.state = GameState.LOAD_SCREEN
        self.controller = LaunchController(self.event_manager, self.screen)

    def notify(self, event: Event) -> None:
        if event == Event.QUIT:
            pygame.quit()
            sys.exit()
        elif event == Event.TICK:
            # limit the redraw speed to 30 frames per second
            self.clock.tick(30)
        elif event == Event.OPEN_SETTINGS:
            self.open_settings()
        elif event == Event.CLOSE_SETTINGS:
            self.close_settings()

    def run(self) -> None:
        while True:
            self.event_manager.post(Event.TICK)

    def inialize_pygame(self) -> None:
        pygame.mixer.pre_init(44100, -16, 4, 2048)
        pygame.init()
        pygame.font.init()

    def open_settings(self) -> None:
        if self.state == GameState.SETTINGS:
            return
        self.state = GameState.SETTINGS
        self.controller = SettingsController(self.event_manager, self.screen)

    def close_settings(self) -> None:
        if self.state == GameState.LOAD_SCREEN:
            return
        self.state = GameState.LOAD_SCREEN
        self.controller = LaunchController(self.event_manager, self.screen)
