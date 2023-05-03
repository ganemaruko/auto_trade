import pandas as pd

from src.indicator.indicator_ import Indicator


class MA(Indicator):
    """Simple Moving Average class."""

    def __init__(self, window: int, col_name: str):
        """Initialize.

        Args:
            window: moving average window size.
            col_name: target column name.
        """
        self.window = window
        self.col_name = col_name

    def __call__(self, df: pd.DataFrame):
        return df[self.col_name].rolling(self.window).mean()


if __name__ == '__main__':
    ma_10 = MA(10, "CLOSE")
    print(ma_10)
