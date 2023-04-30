from typing import List

from src.broker.broker_ import Broker
from src.broker.order_result import OrderResult
from src.broker.virtual_broker.virtual_account import VirtualAccount
from src.order.order_ import Order


class VirtualBroker(Broker):
    def __init__(self):
        self.accounts: List[VirtualAccount] =  

    def take_order(self, order: Order) -> OrderResult:
        pass
