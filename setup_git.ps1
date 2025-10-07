# Simple Git Setup Script
Write-Host "`n=== Mental Health Classifier - Git Setup ===" -ForegroundColor Cyan

# Initialize Git
Write-Host "`n1. Initializing Git repository..." -ForegroundColor Yellow
if (Test-Path ".git") {
    Write-Host "Git already initialized" -ForegroundColor Green
} else {
    git init
    Write-Host "Git initialized successfully" -ForegroundColor Green
}

# Add files
Write-Host "`n2. Adding files to Git..." -ForegroundColor Yellow
git add .
Write-Host "Files added" -ForegroundColor Green

# Create commit
Write-Host "`n3. Creating commit..." -ForegroundColor Yellow
git commit -m "Initial commit: Mental Health Classifier with SVM (81% accuracy), Streamlit UI, and FastAPI"
Write-Host "Commit created" -ForegroundColor Green

# Instructions
Write-Host "`n=== NEXT STEPS ===" -ForegroundColor Cyan
Write-Host "`n1. Create GitHub repository at: https://github.com/new"
Write-Host "   - Name: mental-health-classifier"
Write-Host "   - Public repository"
Write-Host "   - DO NOT initialize with README"

Write-Host "`n2. Enter your GitHub username:"
$username = Read-Host

Write-Host "`n3. Run these commands:"
Write-Host "git remote add origin https://github.com/$username/mental-health-classifier.git" -ForegroundColor Green
Write-Host "git branch -M main" -ForegroundColor Green
Write-Host "git push -u origin main" -ForegroundColor Green

Write-Host "`n=== DEPLOYMENT ===" -ForegroundColor Cyan
Write-Host "`nStreamlit App: https://share.streamlit.io"
Write-Host "API (Render): https://render.com"
Write-Host "API (Railway): https://railway.app"

Write-Host "`nSee DEPLOYMENT_GUIDE.md for detailed instructions`n" -ForegroundColor Yellow
