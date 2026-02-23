def calculate_average(transactions: list[float]) -> float:
    if not transactions:
        raise ValueError("No transactions to calculate average.")

    valid_transactions = filter_valid_transactions(transactions)
    if not valid_transactions:
        raise ValueError("No valid transactions to calculate average.")
    
    return sum(valid_transactions) / len(valid_transactions)

def filter_valid_transactions(transactions: list[float]) -> list[float]:
    valid_transactions = []
    for transaction in transactions:
        try:
            validate_amount(transaction)
            valid_transactions.append(transaction)
        except ValueError:
            continue
    return valid_transactions

def validate_amount(amount: float) -> None:
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

if __name__ == "__main__":
    transactions = [100.0, 250.5, -20.0, 0.0]
    average = calculate_average(transactions)
    print(f"Average transaction: {average:.2f}")