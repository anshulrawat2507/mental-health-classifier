# Push to GitHub - Run this after creating repository
git remote add origin https://github.com/anshulrawat2507/mental-health-classifier.git
git branch -M main
git push -u origin main

Write-Host "`n✅ Pushed to GitHub successfully!`n" -ForegroundColor Green
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Visit: https://github.com/anshulrawat2507/mental-health-classifier"
Write-Host "2. Verify all files uploaded"
Write-Host "3. Deploy Streamlit app: https://share.streamlit.io"
Write-Host "4. Deploy API: https://render.com or https://railway.app"
Write-Host "`nSee DEPLOYMENT_GUIDE.md for detailed instructions`n"
