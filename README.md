# 🧠 Mental Health Text Classifier - AI-Powered Mental Health Detection

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-success.svg)](https://github.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)

> **An end-to-end machine learning system for classifying mental health conditions from text with 81% accuracy**

---

## 🌟 **Live Demo**

🔗 **Web App:** https://anshulrawat2507-mental-health-classifier.streamlit.app ⚡  
🔗 **API Docs:** [Coming Soon - Deploy on Render/Railway]  
🔗 **GitHub:** https://github.com/anshulrawat2507/mental-health-classifier

---

## 📋 **Project Overview**

This project is a **production-ready AI system** that analyzes text and predicts mental health categories using machine learning. It includes both a user-friendly web interface and a RESTful API for developers.

### **🎯 Categories:**
- 😰 **Stress** - Work, academic, or life pressure
- 😔 **Depression** - Persistent sadness and hopelessness
- 🎭 **Bipolar** - Extreme mood swings
- 🤔 **Personality** - Identity and relationship struggles
- 😨 **Anxiety** - Excessive worry and panic

### **📊 Model Performance:**
- **Accuracy**: ~81% on test set
- **Model**: Support Vector Machine (LinearSVC)
- **Features**: TF-IDF vectorization with 5,000 features
- **Training Data**: 5,957 labeled samples
- **Validation**: Stratified cross-validation

---

## 🚀 **Quick Start Guide**

### **1. Install Required Dependencies**

```bash
# Navigate to project directory
cd e:\mental_health_project

# Install core dependencies
pip install pandas numpy scikit-learn matplotlib seaborn joblib

# Install for web app
pip install streamlit plotly

# Install for API
pip install fastapi uvicorn pydantic

# Install for visualizations
pip install wordcloud
```

### **2. Project Structure**

```
mental_health_project/
│
├── data/
│   ├── cleaned_data.csv                    # Processed dataset
│   └── data_to_be_cleansed.csv/
│       └── data_to_be_cleansed.csv        # Original dataset
│
├── models/
│   ├── mental_health_svm_model_*.pkl      # Trained model
│   └── tfidf_vectorizer_*.pkl             # TF-IDF vectorizer
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb             # Data preprocessing
│   ├── 02_baseline_model.ipynb            # Initial model training
│   ├── 03_advanced_model.ipynb            # Advanced techniques
│   └── 04_model_interpretability.ipynb    # Model analysis
│
├── app.py                                  # Streamlit web application
├── api.py                                  # FastAPI REST API
└── README.md                               # This file
```

---

## 📊 **Running the Notebooks**

### **Notebook 1: Data Cleaning**
```bash
# Open in VS Code or Jupyter
jupyter notebook notebooks/01_data_cleaning.ipynb
```

**What it does:**
- Loads raw data
- Cleans and preprocesses text
- Removes duplicates
- Creates cleaned dataset

### **Notebook 2: Baseline Model**
```bash
jupyter notebook notebooks/02_baseline_model.ipynb
```

**What it does:**
- Trains baseline SVM model
- Compares multiple algorithms
- Evaluates performance
- Saves trained model

### **Notebook 3: Advanced Model**
```bash
jupyter notebook notebooks/03_advanced_model.ipynb
```

**What it does:**
- Tests different vectorizers
- Hyperparameter tuning
- Ensemble methods
- Cross-validation
- Feature importance analysis

### **Notebook 4: Model Interpretability**
```bash
jupyter notebook notebooks/04_model_interpretability.ipynb
```

**What it does:**
- Feature importance visualization
- Word clouds for each category
- Misclassification analysis
- Performance breakdown
- Key insights

---

## 🌐 **Running the Web Application**

### **Option 1: Streamlit Web App (Recommended)**

```bash
# Start the Streamlit app
streamlit run app.py
```

**Features:**
- ✨ Beautiful modern UI
- 🔍 Real-time text analysis
- 📊 Interactive confidence charts
- 📝 Sample examples
- 📈 Performance statistics

**Access:** Opens automatically in browser at `http://localhost:8501`

---

## 🔌 **Running the REST API**

### **Option 2: FastAPI REST API**

```bash
# Install API dependencies
pip install fastapi uvicorn pydantic

# Start the API server
uvicorn api:app --reload --port 8000
```

**Features:**
- 🚀 Fast JSON API
- 📝 Auto-generated documentation
- 🔄 Batch predictions
- 🎯 Multiple endpoints

**Access API Documentation:** `http://localhost:8000/docs`

### **API Endpoints:**

1. **Health Check**
   ```bash
   curl http://localhost:8000/health
   ```

2. **Single Prediction**
   ```bash
   curl -X POST "http://localhost:8000/predict" \
        -H "Content-Type: application/json" \
        -d '{"text": "I feel anxious and stressed"}'
   ```

3. **Batch Prediction**
   ```bash
   curl -X POST "http://localhost:8000/batch-predict" \
        -H "Content-Type: application/json" \
        -d '{"texts": ["I feel anxious", "I feel sad"]}'
   ```

4. **Get Categories**
   ```bash
   curl http://localhost:8000/categories
   ```

---

## 🧪 **Testing the System**

### **Sample Test Cases:**

#### **Anxiety Example:**
```
"I've been feeling really anxious lately and having panic attacks. 
My heart races and I can't breathe properly."
```

#### **Depression Example:**
```
"I feel empty inside and nothing brings me joy anymore. 
Everything feels pointless and I'm exhausted all the time."
```

#### **Stress Example:**
```
"Work deadlines are killing me. I'm working 14-hour days 
and feel completely overwhelmed."
```

#### **Bipolar Example:**
```
"Last week I felt invincible, now I can't get out of bed. 
My moods are like a roller coaster."
```

#### **Personality Example:**
```
"I don't know who I really am. My personality changes 
depending on who I'm with and I push people away."
```

---

## 📈 **Next Steps for Improvement**

### **1. Data Enhancement**
- Collect more training data
- Balance dataset if needed
- Add data augmentation

### **2. Model Improvements**
- Try BERT or transformers
- Implement ensemble methods
- Fine-tune hyperparameters

### **3. Feature Engineering**
- Add sentiment analysis
- Include n-grams (trigrams, 4-grams)
- Try character-level features

### **4. Deployment**
- Deploy to cloud (AWS, Azure, GCP)
- Add authentication
- Implement rate limiting
- Add logging and monitoring

### **5. Advanced Features**
- Multi-language support
- Severity scoring (mild/moderate/severe)
- Temporal analysis
- User feedback collection

---

## 🛠️ **Troubleshooting**

### **Issue: Model not found**
```bash
# Make sure you've run notebook 02_baseline_model.ipynb first
# Check if models directory exists
ls models/
```

### **Issue: Import errors**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### **Issue: Streamlit not starting**
```bash
# Check if port 8501 is available
# Try a different port
streamlit run app.py --server.port 8502
```

### **Issue: API errors**
```bash
# Check if port 8000 is available
# Check model files exist in models/ directory
```

---

## 📚 **Additional Resources**

### **Documentation:**
- Scikit-learn: https://scikit-learn.org/
- Streamlit: https://docs.streamlit.io/
- FastAPI: https://fastapi.tiangolo.com/

### **Research Papers:**
- Text Classification with SVM
- Mental Health Detection from Text
- TF-IDF Feature Extraction

---

## ⚠️ **Disclaimer**

This project is for **educational and research purposes only**. It is not intended to:
- Replace professional medical diagnosis
- Provide medical advice or treatment
- Be used for clinical decision-making

Always consult qualified mental health professionals for medical advice.

---

## 📝 **License & Credits**

**Created:** October 2025  
**Model:** Support Vector Machine (SVM)  
**Framework:** Scikit-learn, Streamlit, FastAPI  
**Dataset:** Mental health text data (5,957 samples)

---

## 🤝 **Contributing**

To improve this project:
1. Add more training data
2. Implement advanced models (BERT, GPT)
3. Improve UI/UX
4. Add new features
5. Write tests
6. Improve documentation

---

## 📞 **Support**

For questions or issues:
1. Check the troubleshooting section
2. Review notebook outputs
3. Check API documentation
4. Review model interpretability results

---

**Made with ❤️ using Python, Scikit-learn, Streamlit & FastAPI**