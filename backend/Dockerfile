FROM python:3.11-slim

RUN groupadd -g 1000 appuser && useradd -m -u 1000 -g appuser appuser


WORKDIR /app


RUN apt-get update && apt-get install -y --no-install-recommends build-essential git curl && rm -rf /var/lib/apt/lists/*


COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY app.py ./


# Ensure models cache folder
RUN mkdir -p /app/cache && chown -R appuser:appuser /app/cache


USER appuser
EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
