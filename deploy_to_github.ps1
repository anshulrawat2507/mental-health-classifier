# 🚀 Automated Deployment Script for Mental Health Classifier
# This script will initialize Git, commit files, and prepare for GitHub upload

Write-Host "`n╔══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║     MENTAL HEALTH CLASSIFIER - DEPLOYMENT SCRIPT        ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

# Step 1: Check if Git is installed
Write-Host "📋 Step 1: Checking Git installation..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✅ Git is installed: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Git is not installed!" -ForegroundColor Red
    Write-Host "Please install Git from: https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Step 2: Navigate to project directory
Write-Host "`n📂 Step 2: Navigating to project directory..." -ForegroundColor Yellow
Set-Location -Path "e:\mental_health_project"
Write-Host "✅ Current directory: $(Get-Location)" -ForegroundColor Green

# Step 3: Check if Git is already initialized
Write-Host "`n🔍 Step 3: Checking Git repository status..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "⚠️  Git repository already initialized" -ForegroundColor Yellow
    $reinit = Read-Host "Do you want to reinitialize? (y/n)"
    if ($reinit -eq 'y') {
        Remove-Item -Recurse -Force .git
        Write-Host "✅ Removed existing Git repository" -ForegroundColor Green
    }
}

# Step 4: Initialize Git repository
if (-not (Test-Path ".git")) {
    Write-Host "`n🎬 Step 4: Initializing Git repository..." -ForegroundColor Yellow
    git init
    Write-Host "✅ Git repository initialized" -ForegroundColor Green
} else {
    Write-Host "`n✅ Step 4: Git repository already exists" -ForegroundColor Green
}

# Step 5: Configure Git (if needed)
Write-Host "`n👤 Step 5: Configuring Git user..." -ForegroundColor Yellow
$userName = git config user.name
$userEmail = git config user.email

if (-not $userName) {
    Write-Host "Git user name not configured" -ForegroundColor Yellow
    $newUserName = Read-Host "Enter your name"
    git config user.name "$newUserName"
    Write-Host "✅ Set user name: $newUserName" -ForegroundColor Green
} else {
    Write-Host "✅ Git user: $userName ($userEmail)" -ForegroundColor Green
}

if (-not $userEmail) {
    $newUserEmail = Read-Host "Enter your email"
    git config user.email "$newUserEmail"
    Write-Host "✅ Set user email: $newUserEmail" -ForegroundColor Green
}

# Step 6: Check file status
Write-Host "`n📊 Step 6: Checking project files..." -ForegroundColor Yellow
$fileCount = (Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notmatch '\\mental_env\\|\\__pycache__\\|\\.git\\' }).Count
Write-Host "✅ Found $fileCount files to commit" -ForegroundColor Green

# Step 7: Add all files
Write-Host "`n➕ Step 7: Adding files to Git..." -ForegroundColor Yellow
git add .
Write-Host "✅ All files staged for commit" -ForegroundColor Green

# Step 8: Show status
Write-Host "`n📋 Step 8: Git status..." -ForegroundColor Yellow
git status --short

# Step 9: Create commit
Write-Host "`n💾 Step 9: Creating commit..." -ForegroundColor Yellow
$commitMessage = "🚀 Initial commit: Mental Health Classifier

Features:
- 81% accuracy SVM model for mental health text classification
- Streamlit web interface with beautiful UI
- FastAPI REST API with 7 endpoints
- Complete data cleaning and preprocessing pipeline
- Model interpretability analysis
- Comprehensive testing suite

Categories: Stress, Depression, Bipolar, Personality, Anxiety
Tech Stack: Python, scikit-learn, FastAPI, Streamlit, TF-IDF"

git commit -m "$commitMessage"
Write-Host "✅ Commit created successfully" -ForegroundColor Green

# Step 10: GitHub repository setup instructions
Write-Host "`n`n╔══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║              NEXT STEPS: GITHUB SETUP                   ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

Write-Host "📝 Step 10: Create GitHub Repository" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Go to: https://github.com/new" -ForegroundColor White
Write-Host "2. Repository name: mental-health-classifier" -ForegroundColor White
Write-Host "3. Description: AI-powered mental health text classification with 81% accuracy" -ForegroundColor White
Write-Host "4. Set to: PUBLIC (required for free deployment)" -ForegroundColor White
Write-Host "5. DO NOT initialize with README, .gitignore, or license" -ForegroundColor White
Write-Host "6. Click 'Create repository'" -ForegroundColor White
Write-Host ""

Write-Host "📌 After creating the repository on GitHub:" -ForegroundColor Yellow
Write-Host ""

# Ask for GitHub username
$githubUsername = Read-Host "Enter your GitHub username"

Write-Host "`n📤 Step 11: Commands to push to GitHub:" -ForegroundColor Yellow
Write-Host ""
Write-Host "Copy and run these commands:" -ForegroundColor Cyan
Write-Host ""
Write-Host "git remote add origin https://github.com/$githubUsername/mental-health-classifier.git" -ForegroundColor Green
Write-Host "git branch -M main" -ForegroundColor Green
Write-Host "git push -u origin main" -ForegroundColor Green
Write-Host ""

# Create a command file for easy execution
$pushScript = @"
# Push to GitHub
git remote add origin https://github.com/$githubUsername/mental-health-classifier.git
git branch -M main
git push -u origin main
"@

$pushScript | Out-File -FilePath "push_to_github.ps1" -Encoding UTF8
Write-Host "✅ Created 'push_to_github.ps1' for easy pushing" -ForegroundColor Green

# Step 12: Deployment summary
Write-Host "`n`n╔══════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║            DEPLOYMENT OPTIONS SUMMARY                   ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════════════════════╝`n" -ForegroundColor Cyan

Write-Host "🌐 STREAMLIT APP (Web Interface):" -ForegroundColor Yellow
Write-Host "   1. Go to: https://share.streamlit.io" -ForegroundColor White
Write-Host "   2. Sign in with GitHub" -ForegroundColor White
Write-Host "   3. Click 'New app'" -ForegroundColor White
Write-Host "   4. Select your repo: mental-health-classifier" -ForegroundColor White
Write-Host "   5. Main file: app.py" -ForegroundColor White
Write-Host "   6. Deploy!" -ForegroundColor White
Write-Host ""

Write-Host "🔌 API DEPLOYMENT (Choose one):" -ForegroundColor Yellow
Write-Host ""
Write-Host "   Option A - Render.com (Recommended, FREE):" -ForegroundColor Cyan
Write-Host "     1. Go to: https://render.com" -ForegroundColor White
Write-Host "     2. Sign up with GitHub" -ForegroundColor White
Write-Host "     3. New Web Service" -ForegroundColor White
Write-Host "     4. Connect your repo" -ForegroundColor White
Write-Host "     5. Start command: uvicorn api:app --host 0.0.0.0 --port `$PORT" -ForegroundColor White
Write-Host ""
Write-Host "   Option B - Railway.app (Easy, FREE trial):" -ForegroundColor Cyan
Write-Host "     1. Go to: https://railway.app" -ForegroundColor White
Write-Host "     2. Sign in with GitHub" -ForegroundColor White
Write-Host "     3. New Project → Deploy from GitHub" -ForegroundColor White
Write-Host "     4. Uses Procfile automatically" -ForegroundColor White
Write-Host ""

Write-Host "`n📚 DOCUMENTATION:" -ForegroundColor Yellow
Write-Host "   - Complete guide: DEPLOYMENT_GUIDE.md" -ForegroundColor White
Write-Host "   - API testing: API_TESTING_RESULTS.md" -ForegroundColor White
Write-Host "   - Quick start: QUICK_START.md" -ForegroundColor White
Write-Host ""

Write-Host "`n✅ PROJECT SUMMARY:" -ForegroundColor Green
Write-Host ""
Write-Host "   Files ready for deployment:" -ForegroundColor White
Write-Host "   ✅ .gitignore (excludes unnecessary files)" -ForegroundColor White
Write-Host "   ✅ requirements.txt (all dependencies)" -ForegroundColor White
Write-Host "   ✅ Procfile (for API deployment)" -ForegroundColor White
Write-Host "   ✅ runtime.txt (Python version)" -ForegroundColor White
Write-Host "   ✅ .streamlit/config.toml (Streamlit config)" -ForegroundColor White
Write-Host "   ✅ README.md (project documentation)" -ForegroundColor White
Write-Host "   ✅ All notebooks and code files" -ForegroundColor White
Write-Host ""

Write-Host "`n🎉 Git repository is ready! Follow the steps above to deploy." -ForegroundColor Green
Write-Host "`n💡 Tip: Run './push_to_github.ps1' after creating your GitHub repository`n" -ForegroundColor Cyan

# Create a checklist file
$checklist = @"
# 🚀 Deployment Checklist

## ✅ Completed
- [x] Git repository initialized
- [x] All files committed
- [x] .gitignore configured
- [x] Deployment files created
- [x] Documentation complete

## 📋 Next Steps

### 1. GitHub Upload
- [ ] Create repository on GitHub
- [ ] Run: git remote add origin https://github.com/$githubUsername/mental-health-classifier.git
- [ ] Run: git branch -M main
- [ ] Run: git push -u origin main
- [ ] Verify all files uploaded

### 2. Deploy Streamlit App (5 minutes)
- [ ] Go to https://share.streamlit.io
- [ ] Sign in with GitHub
- [ ] New app → Select repo
- [ ] Main file: app.py
- [ ] Click Deploy
- [ ] Test live URL
- [ ] Update README with URL

### 3. Deploy API (10 minutes)
- [ ] Choose platform (Render/Railway)
- [ ] Create new web service
- [ ] Connect GitHub repo
- [ ] Configure build command
- [ ] Deploy
- [ ] Test /docs endpoint
- [ ] Update README with URL

### 4. Post-Deployment
- [ ] Test all features on live app
- [ ] Test all API endpoints
- [ ] Add deployment URLs to README
- [ ] Create GitHub repository description
- [ ] Add topics/tags to repo
- [ ] Share on social media

### 5. Portfolio & Promotion
- [ ] Add to LinkedIn projects
- [ ] Update resume
- [ ] Write blog post
- [ ] Share on Reddit
- [ ] Add to GitHub profile

## 🆘 Need Help?
- Check: DEPLOYMENT_GUIDE.md
- Review: API_TESTING_RESULTS.md
- Reference: QUICK_START.md

Generated: $(Get-Date -Format "yyyy-MM-dd HH:mm")
"@

$checklist | Out-File -FilePath "DEPLOYMENT_CHECKLIST.md" -Encoding UTF8
Write-Host "📝 Created DEPLOYMENT_CHECKLIST.md for tracking progress" -ForegroundColor Green
Write-Host ""
