# 🎯 Quick Start Guide - Mental Health Classifier API

## ⚡ Start the API (In 3 Steps)

### Step 1: Start Server
```powershell
cd e:\mental_health_project
uvicorn api:app --reload --port 8000
```

### Step 2: Open Browser
Visit: **http://localhost:8000/docs**

### Step 3: Test It!
Click "Try it out" on any endpoint in the Swagger UI

---

## 🔥 Quick Test Commands

### Test with Python
```python
import requests

# Simple prediction
r = requests.post("http://localhost:8000/predict", 
                  json={"text": "I feel so stressed out"})
print(r.json())
```

### Test with cURL (PowerShell)
```powershell
# Health check
curl http://localhost:8000/health

# Make prediction
curl -X POST "http://localhost:8000/predict" `
  -H "Content-Type: application/json" `
  -d '{"text": "I feel very anxious and worried"}'
```

---

## 📊 What You Can Do Now

### ✅ Completed (You Just Did This!)
- [x] Installed API dependencies (FastAPI, Uvicorn, Pydantic)
- [x] Started API server on port 8000
- [x] Tested all 7 endpoints
- [x] Verified predictions working (80% accuracy)
- [x] Confirmed error handling works
- [x] Accessed interactive docs at /docs

### 🎯 Recommended Next Actions

#### Option 1: Analyze Your Model (20 mins)
**Run the interpretability notebook to understand what your model learned:**
```
1. Open: notebooks/04_model_interpretability.ipynb
2. Click: "Run All" (or Ctrl+Enter on each cell)
3. See: 
   - Top words for each mental health category
   - Beautiful word clouds
   - Where model makes mistakes
   - Performance metrics
```

#### Option 2: Deploy to Production (1 hour)
**Make your API publicly accessible:**

**Streamlit Cloud (Easiest):**
```powershell
# 1. Create GitHub repo
git init
git add .
git commit -m "Mental health classifier"
git remote add origin https://github.com/YOUR_USERNAME/mental-health-api.git
git push -u origin main

# 2. Go to share.streamlit.io and deploy
```

**Heroku (For API):**
```powershell
# 1. Create Procfile
echo "web: uvicorn api:app --host=0.0.0.0 --port=$PORT" > Procfile

# 2. Deploy
heroku create mental-health-api
git push heroku main
```

#### Option 3: Improve Model (1-2 hours)
**Try advanced techniques to beat 81% accuracy:**
```
1. Open: notebooks/03_advanced_model.ipynb
2. Run all cells to:
   - Test different feature extraction methods
   - Hyperparameter tuning
   - Ensemble models
   - Cross-validation
3. Save best model and update API
```

#### Option 4: Add New Features (30 mins each)
**Enhance your API:**
- [ ] Add user authentication (JWT tokens)
- [ ] Add request logging
- [ ] Add rate limiting
- [ ] Create usage dashboard
- [ ] Add email notifications
- [ ] Multi-language support

---

## 🐛 Troubleshooting

### Server Won't Start
```powershell
# Check if port is in use
netstat -ano | findstr :8000

# Kill process if needed
taskkill /PID <process_id> /F

# Restart server
uvicorn api:app --reload --port 8000
```

### Import Errors
```powershell
# Reinstall dependencies
pip install -r requirements.txt
```

### Scikit-learn Version Warning
```powershell
# Upgrade to match model version
pip install --upgrade scikit-learn==1.7.2
```

### Model Not Found
```powershell
# Check models directory
ls models/

# Retrain model if needed
jupyter notebook notebooks/02_baseline_model.ipynb
```

---

## 📚 Useful Resources

### Your Files
- **API Code:** `api.py`
- **Test Script:** `test_api.py`
- **Test Results:** `API_TESTING_RESULTS.md`
- **Documentation:** `README.md`
- **Requirements:** `requirements.txt`

### Endpoints
- **Interactive Docs:** http://localhost:8000/docs
- **API Root:** http://localhost:8000/
- **Health Check:** http://localhost:8000/health
- **Predictions:** http://localhost:8000/predict (POST)

### External Links
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Uvicorn Docs](https://www.uvicorn.org/)
- [Streamlit Cloud](https://share.streamlit.io/)
- [Heroku](https://www.heroku.com/)

---

## 💡 Pro Tips

1. **Keep server running** in background while testing
2. **Use /docs** for interactive testing (no code needed)
3. **Check health endpoint** first when debugging
4. **Save test results** from test_api.py for comparison
5. **Monitor confidence scores** - low scores (<40%) = uncertain

---

## 🎓 What You've Learned

✅ How to build a REST API with FastAPI  
✅ How to serve ML models in production  
✅ How to test APIs comprehensively  
✅ How to handle errors and validation  
✅ How to create interactive API documentation  
✅ How to process batch predictions efficiently  

---

## 🚀 Ready for More?

### Phase 3: Advanced Models
Try BERT/Transformers for 85%+ accuracy

### Phase 4: Production Deployment
Deploy to AWS/Azure/Heroku with monitoring

### Phase 5: Mobile App
Create mobile interface using React Native

### Phase 6: Real-time Analysis
Add WebSocket support for streaming predictions

---

**Need Help?**
- Check `API_TESTING_RESULTS.md` for detailed test results
- Check `README.md` for complete documentation
- Run `python test_api.py` to verify API is working

**Last Updated:** October 7, 2025  
**Status:** ✅ API Fully Functional and Tested
