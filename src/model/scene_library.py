"""Implementation of a library storing all scenes and resolutions."""
from typing import Dict, Tuple

from model.combat_model import CombatData
from model.decision_scene import DecisionSceneData
from model.effects import EffectData
from model.interface import SceneData
from model.resolutions import ChoiceData


class ScenesAccess(object):
    """Represents an object with access to scene and resolution data."""
    _library = None

    @classmethod
    def load_library(cls, scenes: Dict[str, DecisionSceneData],
                     resolutions: Dict[str, ChoiceData],
                     effects: Dict[str, EffectData]) -> None:
        cls._library = _SceneLibrary(scenes, resolutions, effects)

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
                 resolutions: Dict[str, ChoiceData],
                 effects: Dict[str, EffectData]) -> None:
        self._scenes = scenes
        self._resolutions = resolutions
        self._effects = effects

    def get_scene_data(self, name: str) -> SceneData:
        if name not in self._scenes:
            raise KeyError('Scene "{}" not defined.'.format(name))
        return self._scenes[name]

    def get_resolution_data(self, name: str) -> ChoiceData:
        if name not in self._resolutions:
            raise KeyError('Resolution "{}" not defined.'.format(name))
        return self._resolutions[name]

    def get_effect_data(self, name: str) -> EffectData:
        if name not in self._effects:
            raise KeyError('Effect "{}" not defined.'.format(name))
        return self._effects[name]


def example_datas() -> Tuple[Dict[str, DecisionSceneData],
                             Dict[str, ChoiceData], Dict[str, EffectData]]:
    # Scenes

    prompt_0 = (
        'You come upon a derelict charging station. Some lights flicker inside'
        ' and your sensors detect motion within. Your audioscopes fainly'
        ' sense an alarm signal.')
    image_0 = 'derelict_store.png'
    choices_0 = {'Investigate': 'enter'}

    scene_1 = DecisionSceneData(
            'The place is empty but seems to have been recently occupied. You '
            'find some small loot on the ground and see a working power '
            'outlet.', 'outlet.jpg',
            {'Collect loot and leave.': 'inventory', 'Charge batteries':
                'charge'})

    prompt_01 = (
        'The place is crawling with small robo-mites! A tech-robot is '
        'trapped under some fallen debris and is currently in the process'
        ' of being disassembled. It emits a weak distress beacon, asking'
        ' for help.')
    image_01 = 'micro-bots.jpg'
    choices_10 = {'Run away!': 'flee', 'Fight!': 'fight_micro'}

    kill_microbots = DecisionSceneData('Hurray! You killed the micro-bots.',
                                       'victory.png', {'Exit': 'map'}, [])
    charge_battery = DecisionSceneData(
            'You charge your batteries at the outlet. The hour is spent '
            'gazing at the wall.', '',
            {'Collect loot and leave.': 'inventory',
             'Charge batteries another hour.': 'charge',
             'Leave.': 'map'},
            ['charge_30'])

    charge_battery_return = DecisionSceneData(
            'You charge your batteries at the outlet. After about 20 minutes '
            'of waiting, the denizens of this station return from their '
            'scavenging trip. They don’t take kindly to you sucking on their '
            'power supply.', 'denizens.png',
            {'Flee!': 'flee',
             'Offer to pay 20 credits for a full charge.': 'offer',
             'They can suck on this! Attack!': 'combat_denizens'},
            ['charge_10'])

    accept_offer = DecisionSceneData(
            'They accept your generous offer.', '', {'Leave': 'map'},
            ['full_charge', 'minus_20']
    )
    reject_offer = DecisionSceneData(
            'They take some time to deliberate, then reject your stingy offer.'
            'Given the extra time, they are able to form a more focused '
            'attack.', '',
            {'Fight!': 'combat_denizens'}, ['reduce_initiative'])

    flee_choice = ChoiceData({'flee': 1})
    flee = DecisionSceneData('You run away!', '', {'Continue': 'map'})

    kill_denizens = DecisionSceneData(
            'After having defeated the denizens, you are able to take your '
            'time to charge your batteries completely.', '',
            {'Collect loot.': 'inventory', 'Leave.': 'map'},
            ['full_charge'])

    map_scene = DecisionSceneData('Filler for map scene', '',
                                  {'Restart': 'restart'})

    shop_intro = DecisionSceneData((
        'It turns out the station is a thriving black market tech outlet. The '
        'shopkeepbot steps out to hail you. “You’re here just in time! Our '
        'fire sale ends in 34.6 minutes!'), 'sales-robot.jpg',

            {'Buy buy buy!': 'store', 'Leave store': 'map'})

    scene_dict = {
        'scene_1': scene_1,
        'scene_2': DecisionSceneData(prompt_01, image_01, choices_10),
        'scene_3': shop_intro,
        'start': DecisionSceneData(prompt_0, image_0, choices_0),
        'combat_microbots': CombatData('kill_microbots'),
        'denizens': charge_battery_return,
        'kill_microbots': kill_microbots, 'leave': charge_battery,
        'combat_denizens': CombatData('kill_denizens'),
        'flee': flee,
        'map': map_scene,
        'inventory': DecisionSceneData('Filler for inventory scene.', '',
                                       {'Restart': 'restart'}),
        'store': DecisionSceneData('Filler for store scene.', '',
                                   {'Restart': 'restart'}),
        'accept_offer': accept_offer,
        'reject_offer': reject_offer,
        'kill_denizens': kill_denizens}

    # Resolutions

    res_dict = {
        'enter': ChoiceData({'scene_1': 1, 'scene_2': 1, 'scene_3': 1}),
        'restart': ChoiceData({'start': 1}, ),
        'fight_micro': ChoiceData({'combat_microbots': 1}),
        'combat_denizens': ChoiceData({'combat_denizens': 1}),
        'charge': ChoiceData({'leave': 1, 'denizens': 1}),
        'flee': flee_choice,
        'map': ChoiceData({'map': 1}),
        'inventory': ChoiceData({'inventory': 1}),
        'offer': ChoiceData({'accept_offer': 1, 'reject_offer': 1}),
        'store': ChoiceData({'store': 1})}

    # Effects

    effect_dict = {'charge_30': EffectData('Battery charge +30', 'green'),
                   'charge_10': EffectData('Battery charge +10', 'green'),
                   'full_charge': EffectData('Battery charged to full.',
                                             'green'),
                   'minus_20': EffectData('Credits: -20', 'red'),
                   'reduce_initiative': EffectData('Initiative: -20', 'red')}

    return scene_dict, res_dict, effect_dict
