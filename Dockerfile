FROM python:3.12-slim

# Install uv
RUN pip install uv

WORKDIR /app

# Copy pyproject.toml first
COPY pyproject.toml ./

# Copy application code before installation!
COPY app/ ./app

# Add __init__.py if not already there
RUN touch app/__init__.py

# Install FastAPI app with uv using editable mode
RUN uv pip install --system --editable .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
