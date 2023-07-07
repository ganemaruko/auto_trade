from backtesting import Strategy

from src.asset_control.core import AssetControllerInterface


class FixedRiskController(AssetControllerInterface):
    def __init__(self, num_unit: int, trade_risk: float, initial_balance: float):
        """Fixed risk.

        Args:
            num_unit: fixed unit amount.
                How many you want to trade, assuming you keep losing.
            trade_risk: trade risk per unit trade.
                Basically, use the difference between the trap price and the stop loss stop price plus the commission.
        """
        super().__init__()
        self.num_unit = num_unit
        self.trade_risk = trade_risk
        # Acceptable risk at one time
        self.fixed_risk_amount = initial_balance / num_unit

    def calc_size(self, strategy: Strategy) -> float:
        balance = strategy.equity
        # get last middle price
        current_data = strategy.data.df.iloc[-1, :]
        price = (current_data["High"] + current_data["Low"]) / 2

        trade_amount = self.fixed_risk_amount / self.trade_risk
        return trade_amount * price / balance
