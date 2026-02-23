from abc import ABC, abstractmethod
from week_2.day_1.transaction import Transaction


class TransactionRepository(ABC):
    
    @abstractmethod
    def get_all(self) -> list[Transaction]:
        pass