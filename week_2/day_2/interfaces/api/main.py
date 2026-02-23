from fastapi import FastAPI, Depends
from week_2.day_2.application.use_cases.generate_transaction_report import GenerateTransactionReportUseCase
from week_2.day_2.domain.exceptions.no_valid_transactions_exception import NoValidTransactionException
from week_2.day_2.infrastructure.repositories.in_memory_transaction_repository import InMemoryTransactionRepository

app = FastAPI()

def get_use_case():
    repository = InMemoryTransactionRepository()
    use_case = GenerateTransactionReportUseCase(repository)
    return use_case

@app.get("/transactions/report")
def generate_report(
    use_case: GenerateTransactionReportUseCase = Depends(get_use_case)
):
    try:
        return use_case.execute()
    except NoValidTransactionException as e:
        print(f"Error: {e}")
        exit(1)
  