from abc import ABC, abstractmethod
from typing import List

from src.env.env_ import Environment
from src.order.order_ import Order


class Strategy(ABC):
    """Strategy."""

    def __init__(self, parameters: dict):
        """

        Args:
            parameters: strategy parameters, used in optimization.

        """
        self.parameters = parameters

    def propose(self, env: Environment) -> List[Order]:
        """Analyze the given environment and suggest orders.

        Args:
            env: Environment.

        Notes:
            - This method is implemented by 'Template pattern'.

        Returns:
                orders list.
        """

    @abstractmethod
    def order(self, env: Environment) -> List[Order]:
        """Analyze the given environment and suggest orders.

        Args:
            env: Environment.

        Notes:
            - This method is called by 'propose' function.

        Returns:
                orders list.
        """
        raise NotImplementedError()

    @abstractmethod
    def validate(self, env: Environment):
        """Validate the given environment.

        Args:
            env: Environment.

        Notes:
            - This function should be implemented to make explicit the elements required for env.

        Raises:
            ValidationError
        """
        raise NotImplementedError()
