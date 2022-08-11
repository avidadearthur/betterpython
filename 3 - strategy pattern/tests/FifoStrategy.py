from typing import List
from abc import ABC, abstractmethod
from SupportTicket import SupportTicket

from TicketOrderingStrategyInterface import TicketOrderingStrategy


class FIFOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        return list.copy()
