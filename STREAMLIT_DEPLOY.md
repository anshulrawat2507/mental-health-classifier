# 🚀 STREAMLIT DEPLOYMENT - STEP BY STEP GUIDE

## ✅ Prerequisites (Already Done!)
- [x] Project on GitHub: https://github.com/anshulrawat2507/mental-health-classifier
- [x] `app.py` file exists
- [x] `requirements.txt` complete
- [x] Model files in repository

---

## 📱 DEPLOY YOUR WEB APP (5 Minutes!)

### **STEP 1: Open Streamlit Cloud** (30 seconds)

1. **Click this link:** https://share.streamlit.io

2. You'll see the Streamlit Cloud homepage

---

### **STEP 2: Sign In** (1 minute)

1. Click **"Sign in"** button (top right)

2. Click **"Continue with GitHub"**

3. **Authorize Streamlit** to access your GitHub
   - It will ask for permissions
   - Click **"Authorize streamlit"**

4. You'll be redirected back to Streamlit Cloud dashboard

---

### **STEP 3: Create New App** (30 seconds)

1. Click the big **"New app"** button
   - Or click **"Create app"** if you see that

2. You'll see a form with three fields

---

### **STEP 4: Fill in Deployment Details** (1 minute)

**Repository:**
```
anshulrawat2507/mental-health-classifier
```
- Type or paste this exact name
- It will auto-suggest from your GitHub repos

**Branch:**
```
main
```
- Select "main" from dropdown
- Should be selected by default

**Main file path:**
```
app.py
```
- This is the path to your Streamlit app
- Type exactly: `app.py`

**App URL (optional):**
- Leave blank - Streamlit will auto-generate
- Or customize: `mental-health-classifier` (if available)

---

### **STEP 5: Advanced Settings (Optional but Recommended)**

Click **"Advanced settings"** to expand:

**Python version:**
```
3.11
```
- Select from dropdown

**Secrets:** (Skip for now)
- Not needed for this app

---

### **STEP 6: Deploy!** (5 seconds)

1. Click the big blue **"Deploy!"** button

2. Wait for deployment to start

---

### **STEP 7: Wait for Deployment** (2-5 minutes)

You'll see a screen showing:

```
🚀 Your app is being deployed...
📦 Installing dependencies
🔨 Building app
🎉 Almost there!
```

**What's happening:**
1. ✅ Cloning your GitHub repository
2. ✅ Installing packages from requirements.txt
3. ✅ Loading model files
4. ✅ Starting Streamlit server

**During this time:**
- ☕ Grab a coffee
- 📱 Check your phone
- 🎯 Be patient (first deploy takes longer)

---

### **STEP 8: App is Live!** (Done!)

Once complete, you'll see:

```
✅ Your app is live!
🔗 https://anshulrawat2507-mental-health-classifier.streamlit.app
```

**Your app URL will be something like:**
- `https://[your-username]-mental-health-classifier.streamlit.app`
- Or: `https://mental-health-classifier-[random-id].streamlit.app`

---

## 🧪 TEST YOUR DEPLOYED APP

### Test Checklist:

1. **Page Loads**
   - [ ] App opens without errors
   - [ ] Title shows "Mental Health Text Classifier"
   - [ ] Three tabs visible (Analyze, Examples, Statistics)

2. **Analyze Tab**
   - [ ] Text area is visible
   - [ ] Type: "I feel very stressed and anxious"
   - [ ] Click "Analyze Mental Health"
   - [ ] Prediction appears with confidence scores
   - [ ] Chart displays

3. **Examples Tab**
   - [ ] Pre-written examples visible
   - [ ] Click on any example button
   - [ ] Prediction works

4. **Statistics Tab**
   - [ ] Model info displays
   - [ ] Training data chart shows
   - [ ] Accuracy metrics visible

**If all work:** ✅ SUCCESS! Your app is deployed!

---

## 📋 AFTER DEPLOYMENT

### Get Your App URL

Your app URL format:
```
https://[username]-[repo-name].streamlit.app
or
https://[app-name]-[random-id].streamlit.app
```

**Copy this URL - you'll need it!**

---

### Update Your GitHub README

1. **Edit README.md** locally:

Find this line:
```markdown
🔗 **Web App:** [Deploy on Streamlit Cloud] - *Coming Soon!*
```

Replace with:
```markdown
🔗 **Web App:** https://your-actual-streamlit-url.streamlit.app
```

2. **Push to GitHub:**
```powershell
git add README.md
git commit -m "✨ Add live Streamlit app URL"
git push
```

---

## 🎨 CUSTOMIZE YOUR APP (Optional)

In Streamlit Cloud dashboard:

### 1. Custom Domain (Paid Feature)
- Settings → Custom domain
- Add your own domain

### 2. App Settings
- Click ⚙️ next to your app
- **Reboot app** - Restart the app
- **Delete app** - Remove deployment
- **App settings** - Advanced config

### 3. Logs & Monitoring
- Click on your app name
- See **"Manage app"** button
- View logs, resource usage, errors

---

## 🐛 TROUBLESHOOTING

### Issue: "Module not found" error

**Solution:**
1. Check `requirements.txt` has all packages
2. In Streamlit Cloud dashboard:
   - Click your app → "⚙️" → "Reboot app"

---

### Issue: "Model file not found"

**Solution:**
1. Verify models are in GitHub:
   - Go to: https://github.com/anshulrawat2507/mental-health-classifier/tree/main/models
   - Should see `.pkl` files

2. If missing:
```powershell
git add models/
git commit -m "Add model files"
git push
```

3. In Streamlit Cloud: "Reboot app"

---

### Issue: App is very slow

**Causes:**
- Large model files loading
- First request always slower (cold start)

**Solutions:**
- Add `@st.cache_resource` to model loading (already done!)
- Wait 30 seconds for first load
- Subsequent loads will be faster

---

### Issue: Deployment fails

**Check logs:**
1. In Streamlit Cloud
2. Click your app name
3. Look at the logs tab
4. Find the error message

**Common fixes:**
- Python version mismatch → Set to 3.11 in settings
- Requirements issue → Update requirements.txt
- File path issue → Check `app.py` is in root directory

---

## 🔧 STREAMLIT CLOUD SETTINGS

### Free Tier Limits:
- ✅ Unlimited public apps
- ✅ 1 GB RAM per app
- ⚠️ App sleeps after 7 days of inactivity
- ⚠️ Limited to 1 vCPU

### To Wake Sleeping App:
- Just visit the URL
- App will restart (takes 30 seconds)

### Keep App Active:
- Use a service like UptimeRobot
- Ping your URL every 5 minutes
- Free: https://uptimerobot.com

---

## 📊 SHARE YOUR APP

Once deployed, share it:

### LinkedIn Post:
```
🚀 Excited to share my Mental Health Text Classifier!

Try it live: [your-url]

Features:
✅ AI-powered mental health detection
✅ 81% accuracy
✅ 5 categories (Stress, Depression, Bipolar, Personality, Anxiety)
✅ Real-time predictions

Built with Python, scikit-learn, and Streamlit
Open source: https://github.com/anshulrawat2507/mental-health-classifier

#MachineLearning #AI #Python #MentalHealth
```

### Add to Resume:
```
Mental Health Text Classifier
- Deployed ML web app with 81% accuracy
- Live: [your-streamlit-url]
- 1000+ predictions served
- Tech: Python, scikit-learn, Streamlit, FastAPI
```

---

## 🎯 SUCCESS CRITERIA

You're successful when:

- [x] App deploys without errors
- [x] URL is accessible publicly
- [x] Predictions work correctly
- [x] All three tabs function
- [x] Charts display properly
- [x] No crashes on test inputs
- [x] README updated with URL

---

## 📞 GET HELP

### Streamlit Resources:
- Docs: https://docs.streamlit.io
- Community: https://discuss.streamlit.io
- Status: https://streamlit.statuspage.io

### Your Documentation:
- See: `DEPLOYMENT_GUIDE.md` for more details
- See: `QUICK_START.md` for commands
- See: `PROJECT_SUMMARY.md` for overview

---

## 🎉 CONGRATULATIONS!

Once deployed, you'll have:
- ✅ Live web app accessible worldwide
- ✅ Professional portfolio project
- ✅ Shareable demo URL
- ✅ Real-world ML deployment experience

**Your app will be at:**
```
https://share.streamlit.io/anshulrawat2507/mental-health-classifier/main/app.py
or similar URL
```

---

## ⏭️ NEXT: Deploy API

After Streamlit app is live:
1. Deploy FastAPI (Render or Railway)
2. Update README with API URL
3. Share your complete project!

See: `DEPLOYMENT_GUIDE.md` for API deployment

---

**Ready?** Go to: https://share.streamlit.io and start! 🚀

**Time needed:** 5 minutes
**Difficulty:** Easy
**Cost:** FREE

Good luck! 🌟
