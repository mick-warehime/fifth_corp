"""Resolutions to scenes."""
import random
from typing import Dict, NamedTuple


class ChoiceData(NamedTuple):
    outcome_odds: Dict[str, int]


class Choice(object):
    """Represents a choice made by the player during a DecisionScene.

    Right now, the outcome of a choice is determined probabilistically.
    """

    def __init__(self, choice_data: ChoiceData) -> None:
        """Initialize the choice.

        Args:
            choice_data: The information describing the odds of the choice.
        """
        outcome_odds = choice_data.outcome_odds
        assert outcome_odds, 'At least one outcome must be specified.'
        assert all(odd > 0 for odd in outcome_odds.values())
        self._outcome_odds = outcome_odds
        self._total_counts = sum(outcome_odds.values())

    def resolve(self) -> str:
        """Probabilitically sample from outcome odds.

        Returns:
            An outcome specified in self._outcome_odds, with probability
            matching its value in self._outcome_odds.
        """
        outcomes = set(self._outcome_odds)
        outcome_ind = random.randint(1, self._total_counts)

        while outcome_ind > 0:
            outcome = outcomes.pop()
            outcome_ind -= self._outcome_odds[outcome]

        return outcome
