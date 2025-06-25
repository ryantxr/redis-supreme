# Backend

A FastAPI backend providing registration and login endpoints.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure the database by setting the `DATABASE_URL` environment variable. By default, it uses SQLite `test.db`.
3. Start the server:
   ```bash
   uvicorn app:app --reload
   ```
