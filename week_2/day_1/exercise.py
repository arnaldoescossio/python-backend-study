from transaction import Transaction
from transaction_report import TransactionReport
from status import Status


def validate_transactions(transactions: list[Transaction]) -> None:
    success_count: int = sum(1 for t in transactions if t.is_valid())

    if success_count == 0:
        raise ValueError("No successful transactions found.")

def filter_valid_transactions(transactions: list[Transaction]) -> list[Transaction]:
    return [t for t in transactions if t.is_valid()]

def calculate_summary(transactions: list[Transaction]) -> TransactionReport:
    valid_transactions = filter_valid_transactions(transactions)

    total_amount: float = sum(t.amount for t in valid_transactions)
    valid_count: int = sum(1 for t in valid_transactions)
    average_amount: float = total_amount / valid_count if valid_count > 0 else 0
    failed_count: int = sum(1 for t in transactions if t.is_failed())
    
    return TransactionReport(valid_count, total_amount, average_amount, failed_count)

def generate_report(transactions: list[Transaction]) -> None:
    report = calculate_summary(transactions)

    print(f"Valid transactions: {report.valid_count}")
    print(f"Total amount: {report.total_amount}")
    print(f"Average amount: {report.average_amount}")
    print(f"Failed transactions: {report.failed_count}")

if "__main__" == __name__:
    transactions: list[Transaction] = [
        Transaction(id=1, amount=100.0, status=Status.SUCCESS),
        Transaction(id=2, amount=250.5, status=Status.SUCCESS),
        Transaction(id=3, amount=-20.0, status=Status.FAILED),
        Transaction(id=4, amount=0.0, status=Status.FAILED),
    ]
    
    try:
        validate_transactions(transactions)
        
        generate_report(transactions)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
