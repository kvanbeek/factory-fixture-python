"""Small statistics helpers, used as a disposable fixture."""

from collections.abc import Iterable, Sequence


def mean(values: Sequence[float]) -> float:
    """The arithmetic mean of a non-empty sequence."""
    if not values:
        raise ValueError("mean of an empty sequence")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """The median of a non-empty sequence."""
    if not values:
        raise ValueError("median of an empty sequence")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def variance(values: Iterable[float]) -> float:
    """The population variance of a non-empty iterable."""
    values = list(values)
    if not values:
        raise ValueError("variance of an empty sequence")
    centre = sum(values) / len(values)
    return sum((value - centre) ** 2 for value in values) / len(values)
