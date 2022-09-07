from abc import ABC, abstractmethod

from backtesting import Strategy


class AssetControllerInterface(ABC):

    @abstractmethod
    def calc_size(self, strategy: Strategy) -> float:
        raise NotImplementedError()
