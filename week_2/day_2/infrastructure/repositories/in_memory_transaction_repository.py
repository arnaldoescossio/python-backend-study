from week_2.day_2.domain.entities.transaction import Transaction
from week_2.day_2.domain.enums.transaction_status import TransactionStatus
from week_2.day_2.domain.repositories.transaction_repository import TransactionRepository

class InMemoryTransactionRepository(TransactionRepository):
    def get_all(self) -> list[Transaction]:
        return [
            Transaction(id=1, amount=100.0, status=TransactionStatus.SUCCESS),
            Transaction(id=2, amount=250.5, status=TransactionStatus.SUCCESS),  
            Transaction(id=3, amount=-20.0, status=TransactionStatus.FAILED),
            Transaction(id=4, amount=0.0, status=TransactionStatus.FAILED)
        ]