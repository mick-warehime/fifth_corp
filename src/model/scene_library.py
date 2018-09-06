"""Implementation of a library storing all scenes and resolutions."""
from typing import Dict, Tuple

from model.combat_model import CombatData
from model.decision_scene import DecisionSceneData
from model.interface import SceneData
from model.resolutions import ChoiceData


class ScenesAccess(object):
    """Represents an object with access to scene and resolution data."""
    _library = None

    @classmethod
    def load_library(cls, scenes: Dict[str, DecisionSceneData],
                     resolutions: Dict[str, ChoiceData]) -> None:
        cls._library = _SceneLibrary(scenes, resolutions)

    @property
    def library(self) -> '_SceneLibrary':
        if self._library is None:
            raise RuntimeError(
                    'ScenesAccess.load_library has not been called.')
        return self._library


class _SceneLibrary(object):
    """Stores and transmits all scene and resolution information.

    Later this object will be constructed from a proto.
    """

    def __init__(self, scenes: Dict[str, SceneData],
                 resolutions: Dict[str, ChoiceData]) -> None:
        self._scenes = scenes
        self._resolutions = resolutions

    def get_scene_data(self, name: str) -> SceneData:
        if name not in self._scenes:
            raise KeyError('Scene "{}" not defined.'.format(name))
        return self._scenes[name]

    def get_resolution_data(self, name: str) -> ChoiceData:
        if name not in self._resolutions:
            raise KeyError('Resolution "{}" not defined.'.format(name))
        return self._resolutions[name]


def example_scenes_and_resolutions() -> Tuple[Dict[str, DecisionSceneData],
                                              Dict[str, ChoiceData]]:
    prompt_0 = (
        'You come upon a derelict charging station. Some lights flicker inside'
        ' and your sensors detect motion within. Your audioscopes fainly'
        ' sense an alarm signal.')
    image_0 = 'derelict_store.png'
    choices_0 = {'Investigate': 'res_0'}

    prompt_00 = (
        'The place is empty but seems to have been recently occupied. '
        'You find some small loot on the ground and see a working power '
        'outlet.')
    go_back = {'Go back.': 'res_00'}

    image_00 = 'outlet.jpg'
    prompt_01 = (
        'The place is crawling with small robo-mites! A tech-robot is '
        'trapped under some fallen debris and is currently in the process'
        ' of being disassembled. It emits a weak distress beacon, asking'
        ' for help.')
    image_01 = 'micro-bots.jpg'
    choices_10 = {'Run away!': 'res_00', 'Fight!': 'fight_res'}

    kill_microbots = DecisionSceneData('Hurray! You killed the micro-bots.',
                                       'victory.png', go_back)

    scene_dict = {
        'scene_1': DecisionSceneData(prompt_00, image_00, go_back),
        'scene_2': DecisionSceneData(prompt_01, image_01, choices_10),
        'start': DecisionSceneData(prompt_0, image_0, choices_0),
        'combat': CombatData('kill_microbots'),
        'kill_microbots': kill_microbots}

    res_dict = {'res_0': ChoiceData({'scene_1': 1, 'scene_2': 1}),
                'res_00': ChoiceData({'start': 1}, ),
                'fight_res': ChoiceData({'combat': 1})}

    return scene_dict, res_dict
