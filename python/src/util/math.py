"""Math util functions."""
from typing import Iterable


def cross(up: Iterable, down: Iterable) -> int:
    """Check whether

    Args:
        up:
        down:

    Returns:
        0: no cross.
        1: cross.
        -1: cross up
    """
    if up[-2] < up[-1]:
        return 1
