from week_2.day_2.domain.entities.transaction import Transaction
from week_2.day_2.domain.enums.transaction_status import TransactionStatus
from week_2.day_2.application.use_cases.generate_transaction_report import GenerateTransactionReportUseCase
from week_2.day_2.domain.exceptions.no_valid_transactions_exception import NoValidTransactionException
from week_2.day_2.domain.entities.transaction import Transaction
from week_2.day_2.infrastructure.repositories.in_memory_transaction_repository import InMemoryTransactionRepository

def main() -> None:
   
    repository = InMemoryTransactionRepository()
    use_case = GenerateTransactionReportUseCase(repository)

    try:
        # transactions = repository.get_all()
        report = use_case.execute()

        print(f"Valid transactions: {report.valid_count}")
        print(f"Total amount: {report.total_amount}")
        print(f"Average amount: {report.average_amount}")
        print(f"Failed transactions: {report.failed_count}")
    except NoValidTransactionException as e:
        print(f"Error: {e}")
        exit(1)

if "__main__" == __name__:
    main()    