from dataclasses import dataclass

@dataclass
class TransactionReport:
    valid_count: int
    total_amount: float
    average_amount: float
    failed_count: int