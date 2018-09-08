"""Module for defining decision scenes."""
from typing import NamedTuple, Dict

from model.interface import SceneData


class DecisionSceneData(NamedTuple, SceneData):  # type: ignore
    prompt: str
    image_file: str
    choices: Dict[str, str]


class EffectData(NamedTuple):  # type: ignore
    description: str
