from abc import ABC, abstractmethod

import pandas as pd


class Indicator(ABC):
    """Indicator base class.

    Notes:
        indicator has the following responsibility.
        - Interface of

    """

    @abstractmethod
    def __call__(self, df: pd.DataFrame) -> pd.DataFrame:
        """Main method of Indicator.

        Args:
            df: pd.DataFrame.

        Returns:
            indicator values.
        """
        raise NotImplementedError()
