from typing import List
from abc import ABC, abstractmethod
from SupportTicket import SupportTicket


class TicketOrderingStrategy(ABC):

    def __init__(self) -> None:
        pass

    @abstractmethod
    # Note the type hint: "list: List[SupportTicket])"
    # and return hint: "-> List[SupportTicket]"
    def create_ordering(self, list: List[SupportTicket]) -> List[SupportTicket]:
        pass
