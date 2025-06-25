# Backend

A FastAPI backend providing registration and login endpoints.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure the database connection:
   - Copy `.env.sample` to `.env` and modify if needed, or set the `DATABASE_URL` environment variable.
   - The default configuration uses SQLite `./database/test.db`.
3. Start the server:

   ```bash
   uvicorn app:app --reload
   ```

## Database

### SQLite

Store the database in code/backend/database

### Migrations

Alembic manages database schema migrations. The configuration lives in
`alembic.ini` (located in this directory) and migration scripts reside under `database/migrations`.

Create a new migration after modifying models:

```bash
alembic revision --autogenerate -m "describe changes"
```

Apply migrations to the database:

```bash
alembic upgrade head
```
