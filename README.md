# 🧾 Loan Application Processing Service

A microservice built with FastAPI to handle loan application submissions and processing asynchronously using Kafka, PostgreSQL, and Redis. The design adheres to Clean Architecture and SOLID principles, emphasizing scalability, testability, and separation of concerns.

---

## 📐 Architecture Overview

This service uses a layered architecture structured as:

```
app/
├── domain/            # Core entities and interfaces (no dependencies)
├── usecases/          # Business logic/services
├── infrastructure/    # External systems (DB, Redis, Kafka)
├── interfaces/        # API (FastAPI) and Kafka consumer
├── main.py            # App entrypoint
tests/                 # Unit tests
```

### Clean Architecture Principles:
- **Domain Layer**: Contains `LoanApplication` entity and `ApplicationRepository` interface.
- **Use Cases Layer**: `ApplicationService` handles validation and decision logic.
- **Infrastructure Layer**: Implements database, Redis, and Kafka producers/consumers.
- **Interfaces Layer**: FastAPI routes and Kafka consumer logic.

---

## 🛠 Tech Stack

- **Language**: Python 3.11+
- **Web Framework**: FastAPI (async)
- **Database**: PostgreSQL + SQLAlchemy (async)
- **Cache**: Redis (via `redis.asyncio`)
- **Message Broker**: Kafka (via `aiokafka`)
- **Containerization**: Docker (optional)
- **Testing**: Pytest

---

## 🚀 Features

- **POST /application**  
  Accepts a loan application and asynchronously publishes it to Kafka.

  ```json
  {
    "applicant_id": "string",
    "amount": 1000,
    "term_months": 12
  }
  ```

- **GET /application/{applicant_id}**  
  Retrieves the latest status for an applicant — first from Redis, then PostgreSQL fallback.

- **Kafka Consumer**
  - Validates application: `amount > 0`, `1 <= term_months <= 60`
  - Determines status: `"approved"` if amount ≤ 5000, otherwise `"rejected"`
  - Persists to PostgreSQL and caches in Redis (TTL: 1 hour)

---

## ⚙️ Installation

### 1. Clone the Repo
```bash
git clone https://github.com/your-username/loan-app-service.git
cd loan-app-service
```

### 2. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL and Redis
You can use Docker:

```bash
docker-compose up -d
```

Or install them locally.

### 5. Run Database Migrations (optional)
If you're managing migrations:
```bash
alembic upgrade head
```

---

## ▶️ Running the Service

### Start FastAPI Server
```bash
uvicorn app.main:app --reload
```

### Start Kafka Consumer
```bash
python app/interfaces/consumers/kafka_consumer.py
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🧼 Project Structure

| Folder/File | Purpose |
|-------------|---------|
| `app/domain/` | Core business models and interfaces |
| `app/usecases/` | Application logic (validation, decisions) |
| `app/infrastructure/db/` | PostgreSQL models and repository |
| `app/infrastructure/redis/` | Redis cache layer |
| `app/infrastructure/kafka/` | Kafka producer |
| `app/interfaces/api/` | FastAPI route handlers |
| `app/interfaces/consumers/` | Kafka consumer logic |
| `tests/` | Unit tests for use cases |

---

## 📌 Notes

- Use `Depends` for dependency injection in FastAPI routes.
- Kafka producer and consumer are designed to work asynchronously.
- The architecture ensures that the domain logic is framework-agnostic and testable in isolation.

---

## 🧳 Author

**Thomas Nynas** – Full Stack Python Engineer  
✉️ Available for remote opportunities  
🌍 Based in United States

---

## 📃 License

MIT License