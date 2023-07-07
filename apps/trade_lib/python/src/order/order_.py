from typing import Optional

from src.core.enums.instrument import InstrumentType
from src.core.enums.order import OrderType
from src.core.logger import create_logger

logger = create_logger(__name__)


class Order:
    def __init__(self,
                 order_type: OrderType,
                 instrument: InstrumentType,
                 units: float,
                 timestamp: float,
                 price: Optional[float] = None,
                 ):
        """Initialize an order.

        Args:
            order_type: order type. Please see OrderType docstring.
            instrument: order instrument. Please see InstrumentType docstring.
            units: order quantity.
            timestamp: UNIX time on create this order.
            price: order price.
        """
        logger.info(
            f"order create. order_type:{order_type}, "
            f"instrument:{instrument}, "
            f"units:{units}, "
            f"price:{price}, "
            f"timestamp: {timestamp}."
        )
        self.order_type = order_type
        self.instrument = instrument
        self.units = units
        self.timestamp = timestamp
        self.price = price
