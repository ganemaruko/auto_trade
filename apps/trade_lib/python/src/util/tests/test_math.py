import pytest

from src.util.math import cross


def test_cross_raise():
    """Test cross function."""
    asc = [0]
    desc = [0]
    with pytest.raises(ValueError):
        _ = cross(asc, desc)


def test_cross_logic():
    """Test cross function."""
    asc = [0, 1]
    desc = [1, 0]
    assert cross(asc, desc) == 1
    assert cross(desc, asc) == -1

    asc = [0, 0]
    desc = [1, 1]
    assert cross(asc, desc) == 0


if __name__ == '__main__':
    pytest.main()
