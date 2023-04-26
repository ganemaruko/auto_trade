from abc import ABC

import pandas as pd


class Indicator(ABC):
    """Indicator base class.

    Notes:
        indicator has the following responsibility.
        - Interface of

    """

    def __call__(self, df: pd.DataFrame):
        pass
