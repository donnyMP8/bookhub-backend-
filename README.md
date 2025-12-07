# bookhub-backend-
This repo will contain:  FastAPI app (main.py)  SQLAlchemy models and relationships  Alembic migrations  Pipenv environment  Database seeding script  Your CLI module (Phase 3 requirement)  API route modules  Utility services  Tests (optional but good)
## Backend Setup & Run

### Prerequisites
- Python 3.8+
- Pipenv

### Installation

1. Navigate to the backend directory:
```bash
cd bookhub-backend-
```

2. Install dependencies:
```bash
pipenv install
```

3. Activate the virtual environment:
```bash
pipenv shell
```

### Running the Backend

#### Start the API Server:
```bash
cd backend
uvicorn main:app --reload
```
The API will be available at: `http://localhost:8000`

- **API Documentation:** http://localhost:8000/docs
- **Alternative Docs:** http://localhost:8000/redoc

#### Run the CLI Application:
```bash
# From the project root (bookhub-backend-)
python -m cli.cli menu
```

Or using Typer directly:
```bash
python cli/cli.py menu
```

### Database Management

#### Create a new migration (after model changes):
```bash
alembic revision --autogenerate -m "description of changes"
```

#### Apply migrations:
```bash
alembic upgrade head
```

#### Reset database:
```bash
rm dev.db
python -c 'from backend.db.database import Base, engine; Base.metadata.create_all(engine)'
python -c "from backend.db.seed import seed_data; seed_data()"
```
