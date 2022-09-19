from typing import List
from abc import ABC, abstractclassmethod


class TradingBot(ABC):
    def connect(self):
        print(f"Connecting to Crypto exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]

#    def list_average(self, l: List[float]) -> float:
#        return sum(l) / len(l)

    def should_buy(self, prices: List[float]) -> bool:
        pass

    def should_sell(self, prices: List[float]) -> bool:
        pass

    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")
