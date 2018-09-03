"""Test class for resolutions."""
import random

from model import resolutions
from model.resolutions import ChoiceData

# Ensures tests are deterministic
random.seed(11)


def test_choice_single_outcome_resolves():
    data = ChoiceData({'only outcome': 1})
    single_outcome = resolutions.Choice(data)
    assert single_outcome.resolve() == 'only outcome'


def test_choice_two_equiprobable_approximately_same():
    outcome_0 = 'A'
    outcome_1 = 'B'
    data = ChoiceData({outcome_0: 100, outcome_1: 100})
    two_outcomes = resolutions.Choice(data)

    num_counts = {outcome_0: 0, outcome_1: 0}
    num_samples = 1000
    for _ in range(num_samples):
        num_counts[two_outcomes.resolve()] += 1

    assert abs(num_counts[outcome_0] - num_samples / 2) < num_samples / 10
    assert abs(num_counts[outcome_1] - num_samples / 2) < num_samples / 10
