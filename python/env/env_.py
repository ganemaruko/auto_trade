from abc import ABC

from broker.broker_ import Broker
from market.market_ import Market


class Environment(ABC):
    """Environment base class."""

    def __init__(self, market: Market, broker: Broker):
        self._market = market
        self._broker = broker
