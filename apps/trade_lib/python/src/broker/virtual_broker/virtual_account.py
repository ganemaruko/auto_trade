from src.broker.account import Account


class VirtualAccount(Account):
    """Virtual account for backtest."""

    def __init__(self, initial_amount: float):
        super().__init__(initial_amount)


if __name__ == '__main__':
    print(VirtualAccount(100))
