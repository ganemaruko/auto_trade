import pandas as pd

from order.order_ import Order
from strategy.strategy_ import Strategy


class GoldenCross(Strategy):

    def order(self, env):
        return Order()



