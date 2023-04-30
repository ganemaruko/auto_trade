from src.broker.broker_ import Broker
from src.market.market_ import Market


class Environment:
    """Environment base class."""

    def __init__(self, market: Market, broker: Broker):
        self._market = market
        self._broker = broker

    def get_market(self) -> Market:
        return self._market

    def get_broker(self) -> Broker:
        return self._broker
