FROM python:3.9-slim

WORKDIR /app

# Copy requirements FIRST for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Then copy the rest of the application
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
