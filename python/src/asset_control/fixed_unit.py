from typing import Final

from backtesting import Strategy

from src.asset_control.core import AssetControllerInterface


class FixedUnitController(AssetControllerInterface):
    def __init__(self, num_unit):
        """Fixed unit number risk controller.

        Args:
            num_unit: fixed unit amount.
                How many you want to trade, assuming you keep losing.

        Notes:
            This method differs from FixedRisk in that
                it calculates the amount of risk per trade each time.
        """
        super().__init__()
        self.num_unit: Final = num_unit

    def calc_size(self, strategy: Strategy) -> float:
        balance = strategy.equity
        # Acceptable risk at one time
        fixed_risk_amount = balance / self.num_unit
        # get last middle price
        current_data = strategy.data.df.iloc[-1, :]
        price = (current_data["High"] + current_data["Low"]) / 2
        risk_per_trade = balance / self.num_unit

        trade_amount = fixed_risk_amount / self.trade_risk
        return trade_amount * price / balance
