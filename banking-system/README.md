3# Banking System (simple)

A small Django-based example banking application with account management,
transactions, and interest calculation (Celery scheduled tasks).

Quick start

1. Create and activate a Python virtual environment

```bash
python -m venv venv
venv\Scripts\activate    # Windows
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Apply migrations and run the development server

```bash
python manage.py migrate
python manage.py runserver
```

Notes

- The repository includes a local `db.sqlite3` for convenience.
- For scheduled interest tasks, run Celery worker and beat (Redis recommended).
- Update `banking_system/settings.py` before deploying (don't keep DEBUG=True or hard-coded SECRET_KEY).

That's it — open http://127.0.0.1:8000/ to explore the app.
