from src.backtest.position import Position
from src.core.enums.instrument import InstrumentType


def test_position_attributes():
    position = Position(
        instrument=InstrumentType.FX_USDJPY,
        units=100,
        open_price=10
    )
    assert position.open_price == 10
    assert position.units == 100
