from typing import List

from broker.broker_ import Broker
from broker.order_result import OrderResult
from broker.virtual_broker.virtual_account import VirtualAccount
from order.order_ import Order


class VirtualBroker(Broker):
    def __init__(self):
        self.accounts: List[VirtualAccount] =  

    def take_order(self, order: Order) -> OrderResult:
        pass
