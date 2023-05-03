from typing import List

from src.core.exception.strategy import ValidationError
from src.core.logger import create_logger
from src.indicator.moving_average import MA
from src.order.order_ import Order
from src.strategy.strategy_ import Strategy
from src.util.math import cross

logger = create_logger(__name__)


class GoldenCross(Strategy):
    """Simple golden cross algorithm."""

    def __init__(self, target_col: str, large_window_: int, small_window_: int):
        logger.info(f"target_col: {target_col}, large_window_: {large_window_}, small_window_: {small_window_}")
        super().__init__({
            "large_window_": large_window_,
            "small_window_": small_window_
        })
        self.target_col = target_col
        self.ma_large = MA(self.parameters["large_window_"], col_name=self.target_col)
        self.ma_small = MA(self.parameters["small_window_"], col_name=self.target_col)

    def order(self, env) -> List[Order]:
        data = env.get_market().get_data()
        ma_small = self.ma_small(data)
        ma_large = self.ma_large(data)
        logger.info(ma_small.values)
        logger.info(ma_large.values)
        cross_value = cross(ma_small.values, ma_large.values)
        if cross_value == 1:
            return [Order()]
        elif cross_value == -1:
            return [Order()]
        else:
            return []

    def validate(self, env):
        if self.target_col not in env.get_market().get_data().columns:
            raise ValidationError(f"target_col: {self.target_col} does not exist in given data.")
