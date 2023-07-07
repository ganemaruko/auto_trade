from abc import ABC, abstractmethod
from typing import List

from src.broker.account import Account
from src.broker.order_result import OrderResult
from src.order.order_ import Order


class Broker(ABC):
    def __init__(self):
        self._accounts: List[Account]

    @abstractmethod
    def take_order(self, order: Order) -> OrderResult:
        raise NotImplementedError()

    def get_accounts(self):
        return self._accounts

    def set_account(self):
        pass
