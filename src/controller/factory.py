"""Constructs Scenes/Controllers based on type context."""
from typing import Union

from controller.combat_controller import CombatController
from controller.decision_controller import DecisionController
from model.combat_model import CombatData
from model.decision_scene import DecisionSceneData
from model.interface import SceneData

_scene_type_to_class = {CombatData: CombatController,
                        DecisionSceneData: DecisionController}


def build_scene(data: SceneData) -> Union[CombatController,
                                          DecisionController]:
    if type(data) not in _scene_type_to_class:
        raise ValueError('Unrecognized data type ({})'.format(type(data)))

    return _scene_type_to_class[type(data)](data)  # type: ignore
