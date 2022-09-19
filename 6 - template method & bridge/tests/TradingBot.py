from typing import List
from abc import ABC, abstractclassmethod
from Exchange import Exchange


class TradingBot(ABC):
    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    @abstractclassmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractclassmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass

    def check_prices(self, coin: str):

        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)

        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}!")
        elif should_sell:
            print(f"You should sell {coin}!")
        else:
            print(f"No action needed for {coin}.")
