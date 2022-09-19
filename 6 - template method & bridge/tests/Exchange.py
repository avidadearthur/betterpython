from abc import ABC, abstractclassmethod
from typing import List


class Exchange(ABC):
    @abstractclassmethod
    def connect(self):
        pass

    @abstractclassmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass


class Binance(Exchange):
    def connect(self):
        print(f"Connecting to Binance exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 14]


class Coinbase(Exchange):
    def connect(self):
        print(f"Connecting to Coinbase exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 12, 18, 20]
