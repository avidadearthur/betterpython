from random import random
from typing import List
import random
from SupportTicket import SupportTicket

from TicketOrderingStrategyInterface import TicketOrderingStrategy


class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        random.shuffle(list_copy)
        return list_copy
