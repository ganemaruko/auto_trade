from abc import ABC, abstractmethod
from typing import List

import pandas as pd

from env.env_ import Environment
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
    def order(self, env: Environment) -> List[Order]:
        """Estimate.

        Args:
            env: Environment

        Returns:
                orders list.
        """
        raise NotImplementedError()
