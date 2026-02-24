from sqlalchemy.orm import Session
from week_2.day_2.domain.entities.transaction import Transaction, TransactionStatus
from week_2.day_2.domain.repositories.transaction_repository import TransactionRepository
from week_2.day_2.infrastructure.models.transaction_model import TransactionModel

class PostgresTransactionRepository(TransactionRepository):

    def __init__(self, db: Session):
        self._db = db

    def get_all(self) -> list[Transaction]:
        models = self._db.query(TransactionModel).all()
        return [self._to_entity(model) for model in models]
        # return [self._to_entity(model) for model in transaction_models]

    def _to_entity(self, model: TransactionModel) -> Transaction:
        return Transaction(
            id=model.id,
            amount=model.amount,
            status=TransactionStatus(model.status)
        )