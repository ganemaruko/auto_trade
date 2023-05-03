import numpy as np
import pandas as pd
import pytest

from src.indicator.moving_average import MA


def test_moving_average():
    ma_10 = MA(4, "CLOSE")
    dummy_data = pd.DataFrame(
        {"CLOSE": [
            1, 2, 3, 4, 5
        ]}
    )
    assert np.isnan(ma_10(dummy_data)[0])
    assert pytest.approx(ma_10(dummy_data)[3]) == 2.5
    assert pytest.approx(ma_10(dummy_data)[4]) == 3.5
