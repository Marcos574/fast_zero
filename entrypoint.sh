
poetry run alembic upgrade head

poetry run uvicorn fast_zero.app:app --host 0.0.0.0 --port 8000