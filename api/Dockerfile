FROM python:3.12-slim

# Install Poetry
RUN pip install poetry

WORKDIR /app

# Copy only Poetry files first (better caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies (no dev deps, no virtualenv)
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copy the actual application
COPY api ./api

CMD ["uvicorn", "api.app.main:app", "--host", "0.0.0.0", "--port", "8000"]