from typing import List, Optional

import pandas as pd

from src.backtest.position import Position
from src.order.order_ import Order
from src.core.logger import create_logger

logger = create_logger(__name__)


class PositionBoard:
    """Position board class for dealing virtual order.

    """

    def __init__(self):
        self.positions: List[Position] = []
        self.orders: List[Order] = []
        self.market_data = pd.DataFrame()
        self.current_order = List

    def add_order(self, order: Order):
        logger.info(f"add order order:{order}.")
        self.orders.append(order)

    def add_market_data(self):
        pass

    def simulate(self, timestamp_col_name: Optional[str] = None):
        """Simulate profit and loss by given positions and orders.

        Notes:
            Main function of this class.

        Returns:
        """
        logger.info(f"Start simulate. market data: {self.market_data.shape}")
        self.market_data.sort_values(by=timestamp_col_name)

        for i, row in self.market_data.iterrows():
            self._check_order_realize()

    def _check_order_realize(self):
        pass
