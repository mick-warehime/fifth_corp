from unittest import TestCase
from input import Keybindings
import tempfile
from typing import Dict
from event import Event
import csv

OPEN_SETTINGS = str(Event.CLOSE_SETTINGS)


# TODO - create a default settings object - read from file?
class KeybindingsTest(TestCase):

    def load_bindings(self, bindings: Dict[str, Event]) -> None:
        self.preference_file = tempfile.NamedTemporaryFile(mode='w')
        self.keybindings = Keybindings()
        self.keybindings.preference_file = self.preference_file.name

        BINDING = 'binding'
        KEY = 'key'
        with open(self.preference_file.name, 'w') as fake_csv:
            writer = csv.DictWriter(fake_csv, fieldnames=[BINDING, KEY])
            writer.writeheader()
            for k, v in bindings.items():
                writer.writerow({BINDING: k, KEY: v})

        self.keybindings.load()

    def test_load_settings(self) -> None:
        bindings = {OPEN_SETTINGS: 'y'}

        self.load_bindings(bindings)

        self.assertEqual(self.keybindings.get_binding('y'), Event(OPEN_SETTINGS))

    def test_save_settings(self) -> None:
        bindings = {OPEN_SETTINGS: 'y'}
        self.load_bindings(bindings)
        new_prefs_file = tempfile.NamedTemporaryFile(mode='w')
        self.keybindings.preference_file = new_prefs_file.name

        self.keybindings.save()

        # load from new file
        self.keybindings = Keybindings()
        self.keybindings.preference_file = new_prefs_file.name
        self.keybindings.load()
        self.assertEqual(self.keybindings.get_binding('y'), Event(OPEN_SETTINGS))
