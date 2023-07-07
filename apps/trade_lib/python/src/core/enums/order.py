from enum import Enum


class OrderType(Enum):
    """Order type.

    Notes:
        The naming of this Enum is based on OANDA's API.
        - MARKET
            a market order.
        - TAKE_PROFIT
            an order with take profit.
        - STOP_LOSS
            an order with stop loss.
        - LIMIT
            an order with both of stop loss and take profit.
        - MARKET_IF_TOUCHED
            ...

    References:
        - https://developer.oanda.com/rest-live-v20/order-ep/.
    """
    MARKET = "MARKET"
    TAKE_PROFIT = "TAKE_PROFIT"
    STOP_LOSS = "STOP_LOSS"
    LIMIT = "LIMIT"
    MARKET_IF_TOUCHED = "MARKET_IF_TOUCHED"
