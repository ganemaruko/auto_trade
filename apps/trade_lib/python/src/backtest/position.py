from src.core.enums.instrument import InstrumentType
from src.core.logger import create_logger

logger = create_logger(__name__)


class Position:
    def __init__(self,
                 instrument: InstrumentType,
                 units: float,
                 open_price: float
                 ):
        """Create position.

        Args:
            instrument: order instrument. Please see InstrumentType docstring.
            units: position quantity.
            open_price: price when create this position.
        """
        logger.info(f"position create. instrument:{instrument}, units:{units}, price:{open_price}")
        self.instrument = instrument
        self.units = units
        self.open_price = open_price
