"""Module for defining decision scenes."""
from typing import NamedTuple, Dict, Sequence

from model.interface import SceneData


class DecisionSceneData(NamedTuple, SceneData):  # type: ignore
    prompt: str
    image_file: str
    choices: Dict[str, str]
    effects: Sequence[str]


# This sets a default value for effects to be an empty tuple.
DecisionSceneData.__new__.__defaults__ = ((),)  # type: ignore
