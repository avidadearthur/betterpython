from TradingBot import TradingBot
from typing import List


class MinMaxTrader(TradingBot):

    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)
