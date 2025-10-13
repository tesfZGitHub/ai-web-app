FROM python:3.11-slim

RUN groupadd -g 1000 appuser && useradd -m -u 1000 -g appuser appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code with correct ownership
COPY --chown=appuser:appuser . .

USER appuser

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app", "--workers", "2"]
