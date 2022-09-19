from abc import ABC, abstractclassmethod
from typing import List


class Exchange(ABC):
    @abstractclassmethod
    def connect(self):
        pass

    @abstractclassmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass
