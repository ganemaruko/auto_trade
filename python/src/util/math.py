"""Math util functions."""
from typing import List


def cross(asc: List[float], desc: List[float]) -> int:
    """Check if the two given arrays intersect.

    Args:
        asc: the float list that is ascending.
        desc: the float list that is descending.

    Notes:
        Please see test_cross for more detail.

    Returns:
        0: no cross.
        1: cross.
        -1: cross in the opposite direction.
    """
    # validate
    if len(desc) <= 1 or len(asc) <= 1:
        raise ValueError(f"The length of the given arguments is not long enough. up: {len(desc)}, down: {len(asc)}")
    # check cross.
    if desc[-2] > asc[-2] and desc[-1] <= asc[-1]:
        return 1
    elif desc[-2] <= asc[-2] and desc[-1] > asc[-1]:
        return -1
    else:
        return 0
