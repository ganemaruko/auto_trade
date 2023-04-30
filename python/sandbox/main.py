from backtesting import Backtest, Strategy
from backtesting.lib import crossover

from backtesting.test import SMA, GOOG

from src.asset_control.fixed_risk import FixedRiskController


class SmaCross(Strategy):
    n1 = 10
    n2 = 20

    def init(self):
        close = self.data.Close
        self.sma1 = self.I(SMA, close, self.n1)
        self.sma2 = self.I(SMA, close, self.n2)
        self.balance_controller = FixedRiskController(20, 200, 10000)

    def next(self):
        if crossover(self.sma1, self.sma2):
            size = self.balance_controller.calc_size(self)
            print("buy", size, self.equity, self.position, self.data)
            order = self.buy(size=size)
        elif crossover(self.sma2, self.sma1):
            size = self.balance_controller.calc_size(self)
            print("sell", size, self.equity, self.position, self.data)
            order = self.sell(size=size)


bt = Backtest(GOOG, SmaCross,
              cash=10000, commission=.002,
              exclusive_orders=True)

output = bt.run()
bt.plot()
