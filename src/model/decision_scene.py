"""Module for defining decision scenes."""
from typing import NamedTuple, Dict


class DecisionSceneData(NamedTuple):  # type: ignore
    prompt: str
    image_file: str
    choices: Dict[str, str]
