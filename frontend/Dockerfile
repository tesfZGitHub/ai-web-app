FROM python:3.11-slim

RUN apt update && apt install -y curl && rm -rf /var/lib/apt/lists/*

RUN useradd -m -u 1000 appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
