from abc import ABC, abstractmethod

from src.broker.order_result import OrderResult
from src.order.order_ import Order


class Broker(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def take_order(self, order: Order) -> OrderResult:
        raise NotImplementedError()
