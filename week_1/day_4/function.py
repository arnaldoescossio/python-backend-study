
# 1️⃣ Funções bem definidas
def divide(a: float, b: float) -> float:
    """Divides two numbers and returns the result.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

# 2️⃣ Parâmetros default
def format_currency(value: float, currency: str = "USD", precision: int = 2) -> str:
    """Formats a number as a currency string.

    Args:
        value (float): The monetary value.
        currency (str, optional): The currency code. Defaults to "USD".
        precision (int, optional): Number of decimal places. Defaults to 2.

    Returns:
        str: The formatted currency string.
    """
    return f"{currency} {value:.{precision}f}"

# 3️⃣ Exceptions: tratar vs propagar
def safe_divide(a: float, b: float) -> float:
    """Safely divides two numbers, returning 0.0 if division fails.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division, or 0.0 if division fails.
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return 0.0
    
def process_payment(amount: float) -> None:
    """Processes a payment, ensuring the amount is valid.

    Args:
        amount (float): The payment amount.
    
    Raises:
        ValueError: If the amount is negative.
    """
    if amount < 0:
        raise ValueError("Payment amount cannot be negative.")
    print(f"Processing payment of ${amount:.2f}")

# 4️⃣ Funções pequenas e reutilizáveis
def validate_transaction(amount: float) -> None:
    """Validates a transaction amount.

    Args:
        amount (float): The transaction amount.

    Raises:
        ValueError: If the amount is negative.
    """
    if amount < 0:
        raise ValueError("Transaction amount cannot be negative.")
        
def calculate_average(values: list[float]) -> float:
    """Calculates the average of a list of numbers.

    Args:
        values (list[float]): A list of numerical values.

    Returns:
        float: The average of the values.
    """
    if not values:
        raise ValueError("The list of values cannot be empty.")
    return sum(values) / len(values)