from event import Event
from typing import Dict
import csv
import logging


class Keybindings(object):
    preference_file = 'data/bindings.pref'
    binding_field = 'binding'
    key_field = 'key'

    def __init__(self) -> None:
        self.bindings = self.load()
        logging.debug(str(self))

    def load(self) -> Dict[str, Event]:
        bindings: Dict[str, Event] = dict()
        with open(self.preference_file) as bindings_file:
            reader = csv.DictReader(bindings_file)
            for row in reader:
                key = row[self.key_field]
                binding = row[self.binding_field]
                bindings[key] = Event[binding]
        return bindings

    def save(self) -> None:
        with open(self.preference_file, 'w') as bindings_file:
            writer = csv.writer(bindings_file)
            for key, value in self.bindings.items():
                writer.writerow([key, value])

    def get_binding(self, key: str) -> Event:
        return self.bindings.get(key, Event.NONE)

    def __str__(self) -> str:
        keys = ["\nKEY BINDINGS", "--------------------"]
        for key, value in self.bindings.items():
            keys.append("{}: {}".format(key, value))
        keys.append("--------------------")
        return '\n'.join(keys)

    def event_for_binding(self, binding: Event) -> Event:
        if binding == Event.CLOSE_SETTINGS:
            return Event.CLOSE_SETTINGS
        elif binding == Event.OPEN_SETTINGS:
            return Event.OPEN_SETTINGS
        return Event.NONE
