from typing import List

from indicator.moving_average import MA
from order.order_ import Order
from strategy.strategy_ import Strategy


class GoldenCross(Strategy):
    """Simple golden cross algorithm."""

    def __init__(self, parameters):
        super().__init__(parameters)


    def order(self, env) -> List[Order]:
        data = env.get_market().get_data()

        return Order()
