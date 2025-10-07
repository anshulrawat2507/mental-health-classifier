"""
Mental Health Text Classification API
FastAPI-based REST API for mental health text classification

Run with: uvicorn api:app --reload --port 8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import numpy as np
from typing import Dict, List
import os
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Mental Health Text Classifier API",
    description="AI-powered mental health category detection from text",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables for model and vectorizer
model = None
vectorizer = None
class_names = ["Stress", "Depression", "Bipolar", "Personality", "Anxiety"]

# Request/Response models
class TextInput(BaseModel):
    text: str = Field(..., min_length=10, description="Text to classify (minimum 10 characters)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "I've been feeling really anxious lately and having panic attacks"
            }
        }

class PredictionResponse(BaseModel):
    predicted_class: str
    class_number: int
    confidence_scores: Dict[str, float]
    timestamp: str
    text_length: int

class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    version: str
    timestamp: str

# Load model on startup
@app.on_event("startup")
async def load_model():
    """Load the trained model and vectorizer"""
    global model, vectorizer
    
    try:
        models_dir = "models"
        
        # Find the most recent model files
        model_files = [f for f in os.listdir(models_dir) if f.startswith("mental_health_svm_model_")]
        vectorizer_files = [f for f in os.listdir(models_dir) if f.startswith("tfidf_vectorizer_")]
        
        if not model_files or not vectorizer_files:
            print("⚠️ Warning: Model files not found!")
            return
        
        # Get the most recent files
        latest_model = max(model_files)
        latest_vectorizer = max(vectorizer_files)
        
        model = joblib.load(f"{models_dir}/{latest_model}")
        vectorizer = joblib.load(f"{models_dir}/{latest_vectorizer}")
        
        print(f"✅ Model loaded successfully: {latest_model}")
        print(f"✅ Vectorizer loaded successfully: {latest_vectorizer}")
        
    except Exception as e:
        print(f"❌ Error loading model: {str(e)}")

# API Endpoints
@app.get("/", response_model=Dict)
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Mental Health Text Classifier API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "predict": "/predict (POST)",
            "batch_predict": "/batch-predict (POST)",
            "categories": "/categories",
            "docs": "/docs"
        }
    }

@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if model is not None else "model_not_loaded",
        "model_loaded": model is not None,
        "version": "1.0.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/categories", response_model=Dict)
async def get_categories():
    """Get all available mental health categories"""
    return {
        "categories": class_names,
        "count": len(class_names),
        "descriptions": {
            "Stress": "Work, academic, or life pressure related stress",
            "Depression": "Persistent sadness, hopelessness, and loss of interest",
            "Bipolar": "Extreme mood swings between highs and lows",
            "Personality": "Identity struggles and relationship difficulties",
            "Anxiety": "Excessive worry, panic, and fear"
        }
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: TextInput):
    """
    Predict mental health category from text
    
    - **text**: The text to analyze (minimum 10 characters)
    
    Returns the predicted category with confidence scores
    """
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        # Transform text
        text_tfidf = vectorizer.transform([input_data.text])
        
        # Get prediction
        prediction = model.predict(text_tfidf)[0]
        decision_scores = model.decision_function(text_tfidf)[0]
        
        # Normalize to probabilities using softmax
        exp_scores = np.exp(decision_scores - np.max(decision_scores))
        normalized_scores = exp_scores / np.sum(exp_scores)
        
        # Create response
        return {
            "predicted_class": class_names[prediction],
            "class_number": int(prediction),
            "confidence_scores": {
                class_name: float(score) 
                for class_name, score in zip(class_names, normalized_scores)
            },
            "timestamp": datetime.now().isoformat(),
            "text_length": len(input_data.text)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")

class BatchTextInput(BaseModel):
    texts: List[str] = Field(..., min_length=1, max_length=100)
    
    class Config:
        json_schema_extra = {
            "example": {
                "texts": [
                    "I'm feeling very anxious about everything",
                    "I feel so hopeless and empty inside"
                ]
            }
        }

@app.post("/batch-predict", response_model=List[PredictionResponse])
async def batch_predict(input_data: BatchTextInput):
    """
    Predict mental health categories for multiple texts
    
    - **texts**: List of texts to analyze (max 100 texts)
    
    Returns predictions for all texts
    """
    if model is None or vectorizer is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    if len(input_data.texts) > 100:
        raise HTTPException(status_code=400, detail="Maximum 100 texts allowed per batch")
    
    try:
        results = []
        
        for text in input_data.texts:
            if len(text) < 10:
                results.append({
                    "predicted_class": "ERROR",
                    "class_number": -1,
                    "confidence_scores": {},
                    "timestamp": datetime.now().isoformat(),
                    "text_length": len(text)
                })
                continue
            
            # Transform and predict
            text_tfidf = vectorizer.transform([text])
            prediction = model.predict(text_tfidf)[0]
            decision_scores = model.decision_function(text_tfidf)[0]
            
            # Normalize scores
            exp_scores = np.exp(decision_scores - np.max(decision_scores))
            normalized_scores = exp_scores / np.sum(exp_scores)
            
            results.append({
                "predicted_class": class_names[prediction],
                "class_number": int(prediction),
                "confidence_scores": {
                    class_name: float(score) 
                    for class_name, score in zip(class_names, normalized_scores)
                },
                "timestamp": datetime.now().isoformat(),
                "text_length": len(text)
            })
        
        return results
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Batch prediction error: {str(e)}")

@app.get("/stats", response_model=Dict)
async def get_stats():
    """Get model statistics and information"""
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    return {
        "model_type": "Support Vector Machine (LinearSVC)",
        "accuracy": "~81%",
        "num_categories": len(class_names),
        "categories": class_names,
        "features": "TF-IDF with 5000 features",
        "training_samples": 5957,
        "model_status": "loaded"
    }

# Run with: uvicorn api:app --reload --port 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)