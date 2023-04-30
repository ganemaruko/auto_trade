from abc import ABC

import pandas as pd

from src.core.logger import create_logger

logger = create_logger(__name__)


class Market(ABC):
    """Market abstract class.

    Notes:
        Market class has the following responsibility.
        - has data such as pandas.
    """

    def __init__(self, data: pd.DataFrame):
        logger.debug(f"initialize {self.__class__.__name__} data: {data.shape}.")
        self._data: pd.DataFrame = pd.DataFrame()
        self.set_data(data)

    def get_data(self):
        return self._data

    def set_data(self, value: pd.DataFrame):
        """Setter for data.

        Returns:
            None.
        """
        self._data = value
