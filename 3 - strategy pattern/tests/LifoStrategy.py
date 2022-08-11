from typing import List
from abc import ABC, abstractmethod
from SupportTicket import SupportTicket

from TicketOrderingStrategyInterface import TicketOrderingStrategy


class LIFOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = list.copy()
        list_copy.reverse()
        return list_copy
