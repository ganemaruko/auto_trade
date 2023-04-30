from strategy.golden_cross import GoldenCross


def test_validate():
    golden_cross = GoldenCross(target_col="CLOSE", large_window_=20, small_window_=5)
