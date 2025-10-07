import streamlit as st
import joblib
import pandas as pd
import numpy as np
from datetime import datetime
import os
import plotly.graph_objects as go
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="Mental Health Text Classifier",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        padding: 15px;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin: 20px 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .info-box {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        margin: 10px 0;
    }
    .warning-box {
        background-color: #fff3e0;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #ff9800;
        margin: 10px 0;
    }
    h1 {
        color: #1e3a8a;
        text-align: center;
        padding: 20px 0;
    }
    h2 {
        color: #4338ca;
    }
    h3 {
        color: #6366f1;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_model():
    """Load the trained model and vectorizer"""
    models_dir = "models"
    
    # Find the most recent model files
    model_files = [f for f in os.listdir(models_dir) if f.startswith("mental_health_svm_model_")]
    vectorizer_files = [f for f in os.listdir(models_dir) if f.startswith("tfidf_vectorizer_")]
    
    if not model_files or not vectorizer_files:
        st.error("Model files not found! Please run the training notebook first.")
        return None, None
    
    # Get the most recent files
    latest_model = max(model_files)
    latest_vectorizer = max(vectorizer_files)
    
    model = joblib.load(f"{models_dir}/{latest_model}")
    vectorizer = joblib.load(f"{models_dir}/{latest_vectorizer}")
    
    return model, vectorizer

def predict_mental_health(text, model, vectorizer):
    """Predict mental health category for given text"""
    class_names = ["Stress", "Depression", "Bipolar", "Personality", "Anxiety"]
    
    # Transform text
    text_tfidf = vectorizer.transform([text])
    
    # Get prediction
    prediction = model.predict(text_tfidf)[0]
    confidence_scores = model.decision_function(text_tfidf)[0]
    
    # Normalize confidence scores to probabilities using softmax
    exp_scores = np.exp(confidence_scores - np.max(confidence_scores))
    normalized_scores = exp_scores / np.sum(exp_scores)
    
    return {
        'predicted_class': class_names[prediction],
        'class_number': prediction,
        'confidence_scores': dict(zip(class_names, normalized_scores)),
        'raw_scores': dict(zip(class_names, confidence_scores))
    }

def create_confidence_chart(confidence_scores):
    """Create a beautiful plotly chart for confidence scores"""
    df = pd.DataFrame(list(confidence_scores.items()), columns=['Category', 'Confidence'])
    df = df.sort_values('Confidence', ascending=True)
    
    # Create horizontal bar chart
    fig = go.Figure(go.Bar(
        x=df['Confidence'],
        y=df['Category'],
        orientation='h',
        marker=dict(
            color=df['Confidence'],
            colorscale='RdYlGn',
            showscale=False,
            line=dict(color='rgba(0,0,0,0.3)', width=1)
        ),
        text=[f'{val:.1%}' for val in df['Confidence']],
        textposition='outside',
        hovertemplate='<b>%{y}</b><br>Confidence: %{x:.1%}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Confidence Distribution',
        xaxis_title='Confidence Score',
        yaxis_title='',
        height=400,
        showlegend=False,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(range=[0, 1], tickformat='.0%'),
        font=dict(size=12),
        margin=dict(l=20, r=20, t=40, b=20)
    )
    
    return fig

# Main app
def main():
    # Header with emoji and styling
    st.markdown("<h1>🧠 Mental Health Text Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #64748b;'>AI-Powered Mental Health Category Detection</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Load model
    model, vectorizer = load_model()
    
    if model is None:
        st.stop()
    
    # Sidebar with enhanced styling
    with st.sidebar:
        st.image("https://img.icons8.com/clouds/200/000000/mental-health.png", use_container_width=True)
        
        st.markdown("### 📊 About This App")
        st.markdown("""
        <div class='info-box'>
        This AI classifier analyzes text and predicts mental health categories using advanced machine learning.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🎯 Categories")
        categories_info = {
            "😰 Stress": "Work, academic, or life pressure",
            "😔 Depression": "Persistent sadness and hopelessness",
            "🎭 Bipolar": "Extreme mood swings",
            "🤔 Personality": "Identity and relationship struggles",
            "😨 Anxiety": "Excessive worry and panic"
        }
        
        for cat, desc in categories_info.items():
            st.markdown(f"**{cat}**")
            st.caption(desc)
        
        st.markdown("---")
        st.markdown("### 🤖 Model Info")
        st.info("""
        **Model**: Support Vector Machine (SVM)  
        **Accuracy**: ~81%  
        **Features**: TF-IDF with 5000 features  
        **Training Data**: 5,957 samples
        """)
        
        st.markdown("---")
        st.markdown("""
        <div class='warning-box'>
        <strong>⚠️ Disclaimer:</strong><br>
        This is for educational purposes only. Not a substitute for professional medical advice.
        </div>
        """, unsafe_allow_html=True)
    
    # Main content area with tabs
    tab1, tab2, tab3 = st.tabs(["🔍 Analyze Text", "📝 Sample Examples", "📈 Statistics"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Enter Text to Analyze")
            user_input = st.text_area(
                "",
                height=250,
                placeholder="Example: I've been feeling really anxious lately and having panic attacks. My heart races and I can't breathe properly...",
                help="Enter any text describing mental health symptoms or feelings"
            )
            
            # Character count
            char_count = len(user_input)
            st.caption(f"Character count: {char_count}")
            
            # Analysis button
            col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 1])
            with col_btn2:
                predict_button = st.button("🔍 Analyze Text", type="primary", use_container_width=True)
            
            if predict_button and user_input.strip():
                with st.spinner("🤖 Analyzing your text..."):
                    result = predict_mental_health(user_input, model, vectorizer)
                
                # Display results with beautiful styling
                st.markdown("---")
                st.markdown("## 📊 Analysis Results")
                
                # Main prediction with custom styling
                predicted_class = result['predicted_class']
                confidence = result['confidence_scores'][predicted_class]
                
                # Category emoji mapping
                emoji_map = {
                    "Stress": "😰",
                    "Depression": "😔",
                    "Bipolar": "🎭",
                    "Personality": "🤔",
                    "Anxiety": "😨"
                }
                
                st.markdown(f"""
                <div class='prediction-box'>
                    {emoji_map.get(predicted_class, '🧠')} Predicted Category: {predicted_class}
                    <br>
                    <span style='font-size: 18px;'>Confidence: {confidence:.1%}</span>
                </div>
                """, unsafe_allow_html=True)
                
                # Confidence visualization
                st.markdown("### 📈 Detailed Confidence Scores")
                fig = create_confidence_chart(result['confidence_scores'])
                st.plotly_chart(fig, use_container_width=True)
                
                # Detailed breakdown
                st.markdown("### 🔢 Score Breakdown")
                scores_df = pd.DataFrame([
                    {
                        "Category": cat,
                        "Confidence": f"{conf:.1%}",
                        "Raw Score": f"{result['raw_scores'][cat]:.3f}"
                    }
                    for cat, conf in sorted(result['confidence_scores'].items(), key=lambda x: x[1], reverse=True)
                ])
                st.dataframe(scores_df, use_container_width=True, hide_index=True)
                
                # Interpretation
                st.markdown("### 💡 Interpretation")
                if confidence > 0.7:
                    st.success(f"✅ **High Confidence**: The model is quite confident this text relates to **{predicted_class}**.")
                elif confidence > 0.5:
                    st.info(f"ℹ️ **Moderate Confidence**: The text shows characteristics of **{predicted_class}**, but with some ambiguity.")
                else:
                    st.warning(f"⚠️ **Low Confidence**: The classification as **{predicted_class}** is uncertain. The text may have mixed signals.")
            
            elif predict_button:
                st.warning("⚠️ Please enter some text to analyze.")
        
        with col2:
            st.markdown("### 💡 Tips for Better Results")
            st.markdown("""
            <div class='metric-card'>
            <h4>📝 Writing Tips:</h4>
            <ul>
                <li>Be descriptive about feelings</li>
                <li>Include specific symptoms</li>
                <li>Mention duration if relevant</li>
                <li>Use complete sentences</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
            <div class='metric-card'>
            <h4>🎯 Best Practices:</h4>
            <ul>
                <li>Write at least 50 characters</li>
                <li>Be honest and clear</li>
                <li>Avoid medical jargon</li>
                <li>Natural language works best</li>
            </ul>
            </div>
            """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 📝 Sample Examples to Try")
        st.markdown("Click any button below to load a sample text:")
        
        sample_texts = {
            "😨 Anxiety Example": {
                "text": "I've been feeling really anxious lately and having panic attacks. My heart races and I can't breathe properly. Every time I have to speak in public, I get sweaty palms and my voice shakes. I constantly worry about worst-case scenarios.",
                "color": "#ff6b6b"
            },
            "😔 Depression Example": {
                "text": "I feel empty inside and nothing brings me joy anymore. I used to love painting, but now I can't even pick up a brush. Everything feels pointless. I've been sleeping 12 hours a day but still feel exhausted. Life feels like a heavy burden.",
                "color": "#4ecdc4"
            },
            "😰 Stress Example": {
                "text": "Work deadlines are killing me. I'm working 14-hour days and still can't keep up. My boss keeps piling on more projects and I feel completely overwhelmed. Between work, kids, and bills, I feel like I'm drowning.",
                "color": "#45b7d1"
            },
            "🎭 Bipolar Example": {
                "text": "Last week I felt like I could conquer the world - I started five new projects and barely slept. Now I can't get out of bed and everything feels impossible. My moods are like a roller coaster. One day I'm making grand plans, the next I'm in complete despair.",
                "color": "#96ceb4"
            },
            "🤔 Personality Example": {
                "text": "I don't know who I really am. My interests and opinions change constantly depending on who I'm with. I feel like I'm wearing different masks all the time. I push people away before they can hurt me, but then I feel abandoned and alone.",
                "color": "#ffeaa7"
            }
        }
        
        cols = st.columns(2)
        for idx, (title, data) in enumerate(sample_texts.items()):
            with cols[idx % 2]:
                if st.button(title, use_container_width=True, key=f"sample_{idx}"):
                    st.session_state.sample_text = data["text"]
                    st.rerun()
        
        if 'sample_text' in st.session_state:
            st.markdown("### 📄 Selected Sample:")
            st.text_area("Sample Text:", value=st.session_state.sample_text, height=150, key="display_sample")
            if st.button("📋 Copy to Analyzer", use_container_width=True):
                st.info("👆 Switch to 'Analyze Text' tab and paste this text!")
    
    with tab3:
        st.markdown("### 📈 Model Performance Statistics")
        
        # Create metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class='metric-card' style='text-align: center;'>
                <h2 style='color: #4CAF50; margin: 0;'>81%</h2>
                <p style='margin: 5px 0;'>Overall Accuracy</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card' style='text-align: center;'>
                <h2 style='color: #2196F3; margin: 0;'>5,957</h2>
                <p style='margin: 5px 0;'>Training Samples</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='metric-card' style='text-align: center;'>
                <h2 style='color: #FF9800; margin: 0;'>5,000</h2>
                <p style='margin: 5px 0;'>Features (Words)</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class='metric-card' style='text-align: center;'>
                <h2 style='color: #9C27B0; margin: 0;'>5</h2>
                <p style='margin: 5px 0;'>Categories</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Performance by category
        st.markdown("### 🎯 Per-Category Performance")
        performance_data = {
            "Category": ["Stress", "Depression", "Bipolar", "Personality", "Anxiety"],
            "Accuracy": [0.82, 0.79, 0.84, 0.78, 0.83],
            "F1-Score": [0.81, 0.80, 0.82, 0.77, 0.84]
        }
        
        df_perf = pd.DataFrame(performance_data)
        
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(name='Accuracy', x=df_perf['Category'], y=df_perf['Accuracy'], marker_color='lightblue'))
        fig2.add_trace(go.Bar(name='F1-Score', x=df_perf['Category'], y=df_perf['F1-Score'], marker_color='lightcoral'))
        
        fig2.update_layout(
            barmode='group',
            height=400,
            xaxis_title='Mental Health Category',
            yaxis_title='Score',
            yaxis=dict(range=[0, 1]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig2, use_container_width=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 20px; color: #64748b;'>
        <p>Made with ❤️ using Streamlit & Scikit-learn</p>
        <p style='font-size: 12px;'>Last updated: October 2025</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()