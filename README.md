# AI Web Application (Flask + FastAPI + Hugging Face)

This project deploys a two-tier AI inference service on a single VM:
- **Backend:** FastAPI serving Hugging Face sentiment analysis (`distilbert-base-uncased-finetuned-sst-2-english`)
- **Frontend:** Flask UI that sends text to the backend and displays results

## 🐳 Run locally with Docker

```bash
docker compose up --build
# Last deployment: Wed Oct  8 12:37:28 EAT 2025
