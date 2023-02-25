from abc import ABC, abstractmethod
from typing import List

import pandas as pd

from order.order_ import Order


class Strategy(ABC):
    """Strategy.

    """

    def __init__(self, parameters):
        """

        Args:
            parameters:

        """
        self.parameters = parameters

    @abstractmethod
    def order(self, data: pd.DataFrame) -> List[Order]:
        """Estimate.

        Args:
            data:

        Returns:

        """
        raise NotImplementedError()
