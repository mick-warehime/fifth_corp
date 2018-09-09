"""Effects that occur during a scene."""
from typing import NamedTuple


class EffectData(NamedTuple):  # type: ignore
    description: str
    description_color: str


class Effect(object):
    """Does something to the player or game history.

    Currently the action is not yet implemented, only a description.
    """

    def __init__(self, data: EffectData) -> None:
        pass
