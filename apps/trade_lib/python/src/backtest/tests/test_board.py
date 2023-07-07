import time

from src.backtest.board import PositionBoard
from src.core.enums.instrument import InstrumentType
from src.core.enums.order import OrderType
from src.order.order_ import Order


def test_board():
    board = PositionBoard()
    board.add_order(
        Order(order_type=OrderType.MARKET,
              instrument=InstrumentType.FX_USDJPY,
              units=100,
              timestamp=time.time()
              )
    )
