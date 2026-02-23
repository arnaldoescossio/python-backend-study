transactions: list[dict[str, int | float]] = [
    {"id": 1, "amount": 100.0},
    {"id": 2, "amount": 250.5},
    {"id": 3, "amount": -50.0},
]

valid_transactions = [t for t in transactions if t["amount"] > 0]

total_amount: float = sum(t["amount"] for t in valid_transactions)

average_amount: float | None = (
    total_amount / len(valid_transactions) if valid_transactions else None
)

print(f"Total: {total_amount}")
print(f"Average: {average_amount}")
