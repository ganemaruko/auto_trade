from typing import List

from src.core.exception.strategy import ValidationError
from src.order.order_ import Order
from src.strategy.strategy_ import Strategy


class GoldenCross(Strategy):
    """Simple golden cross algorithm."""

    def __init__(self, target_col: str, large_window_: int, small_window_: int):
        super().__init__({
            "large_window_": large_window_,
            "small_window_": small_window_
        })
        self.target_col = target_col

    def order(self, env) -> List[Order]:
        data = env.get_market().get_data()
        #
        data[self.target_col]

        return Order()

    def validate(self, env):
        if self.target_col in env.get_market().get_data().columns:
            raise ValidationError(f"target_col: {self.target_col} does not exist in given data.")
