import pytest

from fixture_stats import mean, median, variance


def test_mean() -> None:
    assert mean([1, 2, 3, 4]) == 2.5


def test_median_odd_and_even() -> None:
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 3, 2]) == 2.5


def test_variance() -> None:
    assert variance([1, 2, 3, 4]) == 1.25
    assert variance([5]) == 0


def test_variance_accepts_a_generator() -> None:
    assert variance(x for x in [1, 2, 3, 4]) == 1.25


def test_empty_sequences_are_refused() -> None:
    with pytest.raises(ValueError):
        mean([])
    with pytest.raises(ValueError):
        median([])
    with pytest.raises(ValueError):
        variance([])
    with pytest.raises(ValueError):
        variance(x for x in [])
