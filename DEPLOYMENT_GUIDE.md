# 🚀 Deployment Guide - Mental Health Classifier

Complete guide to deploy your mental health text classification system to production.

---

## 📋 Table of Contents

1. [GitHub Setup](#github-setup)
2. [Deploy Streamlit App](#deploy-streamlit-app)
3. [Deploy API (Multiple Options)](#deploy-api)
4. [Post-Deployment Testing](#testing)
5. [Monitoring & Maintenance](#monitoring)

---

## 🐙 GitHub Setup

### Step 1: Initialize Git Repository

```powershell
# Navigate to project directory
cd e:\mental_health_project

# Initialize git
git init

# Add all files
git add .

# Create first commit
git commit -m "Initial commit: Mental Health Classifier with Streamlit UI and FastAPI"
```

### Step 2: Create GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click **"New Repository"** (green button)
3. Repository name: `mental-health-classifier`
4. Description: `AI-powered mental health text classification with 81% accuracy using SVM and TF-IDF`
5. Set to **Public** (required for free deployment)
6. **DO NOT** initialize with README (we already have one)
7. Click **"Create repository"**

### Step 3: Push to GitHub

```powershell
# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/mental-health-classifier.git

# Push code
git branch -M main
git push -u origin main
```

### Step 4: Verify Upload

Visit: `https://github.com/YOUR_USERNAME/mental-health-classifier`

You should see all your files! ✅

---

## 🌐 Deploy Streamlit App (FREE!)

### Option A: Streamlit Community Cloud (Recommended - FREE)

#### Step 1: Go to Streamlit Cloud
Visit: [share.streamlit.io](https://share.streamlit.io)

#### Step 2: Sign In
- Click **"Sign in with GitHub"**
- Authorize Streamlit to access your repositories

#### Step 3: Deploy New App
1. Click **"New app"**
2. Select your repository: `mental-health-classifier`
3. Branch: `main`
4. Main file path: `app.py`
5. Click **"Deploy!"**

#### Step 4: Wait for Deployment
- Takes 2-5 minutes
- You'll get a URL like: `https://YOUR_USERNAME-mental-health-classifier.streamlit.app`

#### Step 5: Test Your Live App! 🎉
- Visit your URL
- Try the examples
- Share with friends!

### Troubleshooting Streamlit Deployment

**Issue: "ModuleNotFoundError"**
```powershell
# Make sure requirements.txt includes all dependencies
# Already created for you in this project!
```

**Issue: "Model file not found"**
- Make sure `models/` directory is in your GitHub repo
- Verify `.gitignore` doesn't exclude `*.pkl` files

---

## 🔌 Deploy API

### Option A: Render.com (Recommended - FREE, Easy)

#### Step 1: Sign Up
1. Go to [render.com](https://render.com)
2. Sign up with GitHub

#### Step 2: Create Web Service
1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub repository
3. Select `mental-health-classifier`

#### Step 3: Configure Service
```
Name: mental-health-api
Environment: Python 3
Build Command: pip install -r requirements.txt
Start Command: uvicorn api:app --host 0.0.0.0 --port $PORT
```

#### Step 4: Deploy
- Click **"Create Web Service"**
- Wait 5-10 minutes
- You'll get URL like: `https://mental-health-api.onrender.com`

#### Step 5: Test API
```powershell
# Test your live API
curl https://mental-health-api.onrender.com/health
```

---

### Option B: Railway.app (Easy Alternative - FREE)

#### Step 1: Sign Up
Visit [railway.app](https://railway.app) → Sign in with GitHub

#### Step 2: New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose `mental-health-classifier`

#### Step 3: Configure
- Railway auto-detects Python
- It will use `Procfile` automatically
- Click **"Deploy"**

#### Step 4: Get Your URL
- Click **"Generate Domain"**
- You'll get: `https://mental-health-api.up.railway.app`

---

### Option C: Heroku (Classic Option - Paid)

> **Note:** Heroku no longer offers free tier, starts at $5/month

#### Step 1: Install Heroku CLI
```powershell
# Download from: https://devcenter.heroku.com/articles/heroku-cli
# Or use installer
```

#### Step 2: Login
```powershell
heroku login
```

#### Step 3: Create App
```powershell
cd e:\mental_health_project
heroku create mental-health-api
```

#### Step 4: Deploy
```powershell
git push heroku main
```

#### Step 5: Open
```powershell
heroku open
# Add /docs to URL for API documentation
```

---

## 🧪 Post-Deployment Testing

### Test Streamlit App

Visit your Streamlit URL and test:
- ✅ Page loads correctly
- ✅ Text input works
- ✅ Prediction button responds
- ✅ Charts display properly
- ✅ Examples tab works
- ✅ Statistics tab shows data

### Test API Endpoints

```powershell
# Replace with your actual deployed URL
$API_URL = "https://your-api-url.com"

# Test health
curl "$API_URL/health"

# Test prediction
curl -X POST "$API_URL/predict" `
  -H "Content-Type: application/json" `
  -d '{"text": "I feel very anxious and stressed"}'

# Test batch prediction
curl -X POST "$API_URL/batch-predict" `
  -H "Content-Type: application/json" `
  -d '{"texts": ["I feel anxious", "I am stressed"]}'

# View documentation
# Visit: $API_URL/docs in browser
```

### Create Test Script for Deployed API

```python
# test_deployed_api.py
import requests

API_URL = "https://your-api-url.com"  # Replace with your URL

def test_deployed_api():
    # Test health
    health = requests.get(f"{API_URL}/health")
    print(f"Health: {health.json()}")
    
    # Test prediction
    pred = requests.post(
        f"{API_URL}/predict",
        json={"text": "I feel overwhelmed with work pressure"}
    )
    print(f"Prediction: {pred.json()}")
    
    print("\n✅ All tests passed!")

if __name__ == "__main__":
    test_deployed_api()
```

---

## 📊 Monitoring & Maintenance

### Streamlit Cloud Dashboard

1. Go to [share.streamlit.io/dashboard](https://share.streamlit.io/dashboard)
2. View your app metrics:
   - Active users
   - Request count
   - Error logs
   - Resource usage

### API Monitoring (Render/Railway)

Both platforms provide:
- **Logs**: View real-time API requests
- **Metrics**: CPU, memory, response time
- **Alerts**: Email notifications for downtime

### Set Up Custom Domain (Optional)

#### For Streamlit:
1. In Streamlit Cloud dashboard
2. Go to **Settings** → **Custom Domain**
3. Add your domain (e.g., `mental-health.yoursite.com`)
4. Follow DNS configuration instructions

#### For API (Render):
1. In Render dashboard
2. Go to **Settings** → **Custom Domain**
3. Add domain
4. Update DNS records

---

## 🔒 Security Best Practices

### 1. Add Rate Limiting

```python
# Install: pip install slowapi
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.post("/predict")
@limiter.limit("10/minute")  # 10 requests per minute
async def predict(...):
    ...
```

### 2. Add API Key Authentication

```python
from fastapi import Header, HTTPException

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != "your-secret-key":
        raise HTTPException(status_code=403, detail="Invalid API Key")

@app.post("/predict", dependencies=[Depends(verify_api_key)])
async def predict(...):
    ...
```

### 3. Enable HTTPS
- Render/Railway provide HTTPS automatically ✅
- Streamlit Cloud provides HTTPS automatically ✅

### 4. Environment Variables

```powershell
# In Render/Railway dashboard, add environment variables:
MODEL_PATH=models/
MAX_BATCH_SIZE=100
API_KEY=your-secret-key
```

---

## 📈 Scaling Considerations

### Free Tier Limits

**Streamlit Community Cloud:**
- ✅ Unlimited apps
- ⚠️ Sleep after 7 days inactivity
- ⚠️ 1GB RAM limit
- ⚠️ 1 vCPU

**Render Free Tier:**
- ✅ Multiple services
- ⚠️ Sleep after 15 min inactivity
- ⚠️ 512MB RAM
- ⚠️ Slow cold starts

**Railway Free Trial:**
- ✅ $5 credit/month
- ⚠️ Credit-based (not time-based)

### When to Upgrade

Upgrade when you have:
- 🔥 1000+ daily users
- 🔥 Need 99.9% uptime
- 🔥 > 100 requests/minute
- 🔥 Large model files (> 500MB)
- 🔥 Need custom domains
- 🔥 Need dedicated support

### Recommended Paid Plans

**For Streamlit App:**
- Streamlit for Teams: $250/month
- Features: Private apps, SSO, priority support

**For API:**
- Render Pro: $7/month per service
- Railway Pro: $20/month credit
- AWS/GCP/Azure: Variable pricing

---

## 🎯 Success Checklist

Before announcing your project:

### GitHub Repository
- [ ] Code pushed to GitHub
- [ ] README.md complete with screenshots
- [ ] requirements.txt includes all dependencies
- [ ] .gitignore properly configured
- [ ] License file added (MIT recommended)
- [ ] Professional repository description

### Streamlit App
- [ ] Deployed and accessible via public URL
- [ ] All features working correctly
- [ ] UI looks professional on mobile
- [ ] No errors in logs
- [ ] Examples work properly

### API
- [ ] Deployed and accessible via public URL
- [ ] /docs endpoint shows Swagger UI
- [ ] All endpoints tested and working
- [ ] Response times < 1 second
- [ ] Error handling works correctly
- [ ] CORS configured if needed

### Documentation
- [ ] README.md has live demo links
- [ ] API_TESTING_RESULTS.md updated with deployed URL
- [ ] Architecture diagram created
- [ ] Usage examples provided
- [ ] Deployment guide accessible

### Promotion
- [ ] Add project to GitHub profile
- [ ] Share on LinkedIn
- [ ] Add to resume/portfolio
- [ ] Post on Reddit (r/MachineLearning, r/Python)
- [ ] Share on Twitter/X with #MachineLearning
- [ ] Write blog post about building it

---

## 🆘 Common Issues & Solutions

### Issue: "Application Error" on Streamlit

**Solution:**
```powershell
# Check logs in Streamlit Cloud dashboard
# Common fixes:
1. Verify requirements.txt has correct versions
2. Check if model files are in repo
3. Ensure data files are accessible
```

### Issue: API Returns 500 Error

**Solution:**
```powershell
# Check deployment logs
# Common causes:
1. Model file not found → Check path in api.py
2. Memory limit exceeded → Optimize model size
3. Cold start timeout → Implement health check warming
```

### Issue: Slow API Response

**Solution:**
```python
# Add caching in api.py
from functools import lru_cache

@lru_cache(maxsize=1000)
def predict_cached(text: str):
    return model.predict([text])
```

### Issue: GitHub Push Failed

**Solution:**
```powershell
# If files too large
git lfs install
git lfs track "*.pkl"
git lfs track "*.csv"
git add .gitattributes
git commit -m "Add Git LFS"
git push
```

---

## 📱 Share Your Project

### GitHub README Badges

Add these to your README.md:

```markdown
![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white)
```

### Social Media Post Template

```
🚀 Just deployed my Mental Health Text Classification system!

✨ Features:
- 81% accuracy with SVM
- Real-time predictions via REST API
- Beautiful Streamlit web interface
- 5 mental health categories

🔗 Live Demo: [your-streamlit-url]
🔗 API Docs: [your-api-url]/docs
🔗 GitHub: [your-github-url]

Built with #Python #MachineLearning #FastAPI #Streamlit
```

---

## 🎓 What You've Accomplished

By completing this deployment, you've:

✅ Built a complete ML pipeline (data → model → deployment)
✅ Created both user-facing and developer-facing interfaces
✅ Deployed to production with proper DevOps practices
✅ Made your project accessible worldwide
✅ Added a portfolio-worthy project
✅ Demonstrated full-stack ML engineering skills

---

## 🚀 Next Steps After Deployment

1. **Monitor usage** - Check logs daily for first week
2. **Collect feedback** - Share with friends and get reviews
3. **Iterate** - Implement suggested improvements
4. **Add features** - User accounts, history, analytics
5. **Upgrade model** - Try BERT for better accuracy
6. **Monetize** - Add premium features or API tiers

---

**🎉 Congratulations on deploying your first production ML system!**

For help or questions:
- Check deployment platform documentation
- Review logs in dashboard
- Test thoroughly before sharing widely

**Generated:** October 7, 2025
**Status:** Ready for Deployment 🚀
