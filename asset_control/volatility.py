from asset_control.core import AssetControllerInterface


class FixedVolatility(AssetControllerInterface):
    def calc_size(self, balance) -> float:
        return 0.1
