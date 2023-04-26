from broker.broker_ import Broker
from env.env_ import Environment
from strategy.strategy_ import Strategy


class Runner:
    """Runner class.

    Notes:
        This method has the below

    """
    def __init__(self, env: Environment, strategy: Strategy, broker: Broker):
        self._broker = broker
        self._strategy = strategy
        self._env = env

    def run(self):
        """Main function of auto trade.

        Notes:
            - this method use 'template method'.

        Returns:
        """
        # 1. create environment.

        # 2. order.
        order_result = self._strategy.order(self._env)

        # 3. execute orders.
        for order in order_result:
            self._broker.take_order(order)
