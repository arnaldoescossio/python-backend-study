from typing import TypedDict

class Transaction(TypedDict):
    id: int
    amount: float
    status: str


def is_valid_transaction(transaction: Transaction) -> bool:
    return transaction["status"] == "SUCCESS" and transaction["amount"] > 0

def validate_transactions(transactions: list[Transaction]) -> None:
    success_count: int = sum(1 for t in transactions if is_valid_transaction(t))

    if success_count == 0:
        raise ValueError("No successful transactions found.")

def filter_valid_transactions(transactions: list[Transaction]) -> list[Transaction]:
    return [t for t in transactions if is_valid_transaction(t)]

def calculate_sumary(transactions: list[Transaction]) -> tuple[int, float, float, int]:
    valid_transactions = filter_valid_transactions(transactions)

    total_amount: float = sum(t["amount"] for t in valid_transactions)
    count: int = sum(1 for t in valid_transactions)
    avarage_amount: float = total_amount / count 
    failed_count: int = sum(1 for t in transactions if t["status"] == "FAILED")
    
    return count, total_amount, avarage_amount, failed_count

def generate_report(transactions: list[Transaction]) -> None:
    count, total_amount, avarage_amount, failed_count = calculate_sumary(transactions)

    print(f"Valid transactions: {count}")
    print(f"Total amount: {total_amount}")
    print(f"Average amount: {avarage_amount}")
    print(f"Failed transactions: {failed_count}")

if "__main__" == __name__:
    transactions: list[Transaction] = [
        {"id": 1, "amount": 100.0, "status": "SUCCESS"},
        {"id": 2, "amount": 250.5, "status": "SUCCESS"},
        {"id": 3, "amount": -20.0, "status": "FAILED"},
        {"id": 4, "amount": 0.0, "status": "FAILED"},
    ]
    
    try:
        validate_transactions(transactions)
        
        generate_report(transactions)
    except ValueError as e:
        print(f"Error: {e}")
        exit(1)
