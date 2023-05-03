import pandas as pd
import pytest

from src.broker.virtual_broker.virtual_broker_ import VirtualBroker
from src.core.exception.strategy import ValidationError
from src.env.env_ import Environment
from src.market.market_ import Market
from src.strategy.golden_cross import GoldenCross


def test_validate():
    """Test validate function."""

    dummy_data = pd.DataFrame(
        {"OPEN": [
            1, 2, 3, 4, 5
        ]}
    )
    golden_cross = GoldenCross(target_col="CLOSE", large_window_=20, small_window_=5)
    broker = VirtualBroker()
    market = Market(
        data=dummy_data
    )
    env = Environment(
        market=market,
        broker=broker
    )
    with pytest.raises(ValidationError):
        _ = golden_cross.validate(env)


def test_order():
    dummy_data = pd.DataFrame(
        {"CLOSE": range(30)}
    )
    golden_cross = GoldenCross(target_col="CLOSE", large_window_=20, small_window_=5)
    broker = VirtualBroker()
    market = Market(
        data=dummy_data
    )
    env = Environment(
        market=market,
        broker=broker
    )
    orders = golden_cross.order(env)
    assert len(orders) == 0
