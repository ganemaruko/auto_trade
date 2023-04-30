from src.indicator.indicator_ import Indicator


class MA(Indicator):
    def __init__(self, window: int):
        """

        Args:
            window: moving average window size.
        """
        self.window = window

    def __call__(self, *args, **kwargs):
        pass


if __name__ == '__main__':
    ma_10 = MA(10)
    ma_10()
