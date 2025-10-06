from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import os

app = FastAPI()

print("Loading sentiment analysis model...")
# Use a simpler model that loads faster for testing
classifier = pipeline("sentiment-analysis", 
                     model="distilbert-base-uncased-finetuned-sst-2-english")
print("Model loaded successfully!")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "AI Backend is running"}

@app.post("/predict")
async def predict(request: TextRequest):
    try:
        result = classifier(request.text)[0]
        return {
            "text": request.text,
            "sentiment": result['label'],
            "confidence": round(result['score'], 4)
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Add this to make sure the root endpoint works
@app.get("/test")
def test_endpoint():
    return {"message": "Test endpoint working"}
