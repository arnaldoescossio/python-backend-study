# Python Backend Enterprise Project (Clean Architecture)

This project demonstrates how to build a **production-ready backend
service** using modern Python backend practices.\
The goal is to evolve from simple Python scripts to a **professional
microservice architecture** similar to what is used in international
companies.

The stack and practices used here follow industry standards for backend
engineering.

------------------------------------------------------------------------

# Technology Stack

-   Python 3.11
-   FastAPI
-   PostgreSQL
-   SQLAlchemy 2.0
-   Docker & Docker Compose
-   Alembic (Database migrations)
-   Pytest (Testing)
-   Pytest-Cov (Test coverage)
-   JWT Authentication
-   Structlog (Structured logging)
-   GitHub Actions (CI/CD)

------------------------------------------------------------------------

# Project Architecture

The project follows **Clean Architecture** principles.

    project/
    │
    ├── domain/
    │   ├── entities/
    │   │   └── transaction.py
    │   ├── repositories/
    │   │   └── transaction_repository.py
    │   └── exceptions.py
    │
    ├── application/
    │   ├── dtos/
    │   │   └── transaction_report_dto.py
    │   └── use_cases/
    │       └── generate_transaction_report.py
    │
    ├── infrastructure/
    │   ├── database.py
    │   ├── models/
    │   │   └── transaction_model.py
    │   └── repositories/
    │       └── postgres_transaction_repository.py
    │
    ├── interfaces/
    │   └── api/
    │       ├── main.py
    │       └── security.py
    │
    ├── migrations/
    │
    ├── tests/
    │   └── test_generate_transaction_report.py
    │
    ├── Dockerfile
    ├── docker-compose.yml
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# Step 1 --- Create Virtual Environment

Create the project folder.

    mkdir python-backend-study
    cd python-backend-study

Create virtual environment.

    python -m venv venv

Activate it (Windows):

    venv\Scripts\activate

------------------------------------------------------------------------

# Step 2 --- Install Core Dependencies

    pip install fastapi uvicorn sqlalchemy psycopg2-binary
    pip install python-jose passlib[bcrypt]
    pip install structlog
    pip install pytest pytest-cov
    pip install alembic

------------------------------------------------------------------------

# Step 3 --- Create Transaction Entity

Example:

``` python
from dataclasses import dataclass

@dataclass
class Transaction:
    id: int
    amount: float
    status: str

    def is_valid(self) -> bool:
        return self.status == "SUCCESS" and self.amount > 0
```

This entity represents the **core domain model**.

------------------------------------------------------------------------

# Step 4 --- Repository Interface (DIP)

    domain/repositories/transaction_repository.py

``` python
from abc import ABC, abstractmethod

class TransactionRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass
```

This allows dependency inversion.

------------------------------------------------------------------------

# Step 5 --- Use Case

    application/use_cases/generate_transaction_report.py

The use case contains the **business logic**.

Responsibilities:

-   Load transactions
-   Filter valid transactions
-   Calculate totals
-   Return report

------------------------------------------------------------------------

# Step 6 --- Database with SQLAlchemy

    infrastructure/database.py

Example:

``` python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
```

------------------------------------------------------------------------

# Step 7 --- SQLAlchemy Model

    infrastructure/models/transaction_model.py

Example:

``` python
from sqlalchemy import Column, Integer, Float, String
from infrastructure.database import Base

class TransactionModel(Base):

    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    status = Column(String, nullable=False)
```

------------------------------------------------------------------------

# Step 8 --- PostgreSQL Repository

Repository implementation that loads data from PostgreSQL.

    infrastructure/repositories/postgres_transaction_repository.py

The repository converts database rows into **domain entities**.

------------------------------------------------------------------------

# Step 9 --- FastAPI API Layer

    interfaces/api/main.py

Example endpoint:

    GET /transactions/report

Run the API:

    uvicorn interfaces.api.main:app --reload

Open:

    http://localhost:8000/docs

Swagger documentation will appear automatically.

------------------------------------------------------------------------

# Step 10 --- JWT Authentication

    interfaces/api/security.py

JWT is used to protect endpoints.

Requests must include:

    Authorization: Bearer TOKEN

------------------------------------------------------------------------

# Step 11 --- Structured Logging

Install:

    pip install structlog

Example:

``` python
import structlog

logger = structlog.get_logger()

logger.info("transaction_report_generated", count=5)
```

Logs are generated in JSON format.

------------------------------------------------------------------------

# Step 12 --- Docker Setup

## Dockerfile

``` dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "interfaces.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

------------------------------------------------------------------------

# Docker Compose

    docker-compose.yml

Example services:

-   API container
-   PostgreSQL database

Run:

    docker compose up --build

------------------------------------------------------------------------

# Step 13 --- Database Migrations with Alembic

Initialize migrations:

    alembic init migrations

Create migration:

    alembic revision --autogenerate -m "create transactions table"

Apply migration:

    alembic upgrade head

------------------------------------------------------------------------

# Step 14 --- Unit Tests

Example test:

    tests/test_generate_transaction_report.py

Run tests:

    pytest

------------------------------------------------------------------------

# Step 15 --- Test Coverage

Run:

    pytest --cov=.

Generate HTML report:

    pytest --cov=. --cov-report=html

Open:

    htmlcov/index.html

Goal:

-   85%+ coverage

------------------------------------------------------------------------

# Step 16 --- Continuous Integration

Create:

    .github/workflows/ci.yml

Pipeline runs:

-   dependency installation
-   tests
-   coverage

This ensures code quality automatically.

------------------------------------------------------------------------

# Running the Full System

Start everything:

    docker compose up --build

API:

    http://localhost:8000

Swagger:

    http://localhost:8000/docs

------------------------------------------------------------------------

# Future Improvements

Possible enterprise upgrades:

-   Redis cache
-   Kafka / RabbitMQ messaging
-   Kubernetes deployment
-   Terraform infrastructure
-   Prometheus + Grafana observability
-   Role-based access control (RBAC)

------------------------------------------------------------------------

# Author

Backend engineering learning project focused on:

-   Clean Architecture
-   Scalable backend design
-   Production-ready Python services
