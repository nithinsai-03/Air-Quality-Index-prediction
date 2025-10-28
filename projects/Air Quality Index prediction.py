import streamlit as st
import numpy as np
import joblib
import os
import pandas as pd
import plotly.graph_objects as go

# ------------------------------------------------
# 🎨 PAGE CONFIGURATION
# ------------------------------------------------
st.set_page_config(
    page_title="🌫️ AQI Predictor Dashboard",
    page_icon="🌍",
    layout="centered"
)

# ------------------------------------------------
# 🧠 LOAD MODELS
# ------------------------------------------------
models = {}
model_files = {
    "XGBoost Regressor": "best_model.pkl",
    "Linear Regression": "linear_regression.pkl",
    "Lasso Regression": "lasso.pkl",
    "Ridge Regression": "ridge.pkl"
}

for name, file in model_files.items():
    if os.path.exists(file):
        models[name] = joblib.load(file)

# ------------------------------------------------
# 🖌️ CUSTOM CSS
# ------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
body {
    font-family: 'Poppins', sans-serif;
    background: linear-gradient(135deg, #f0f4ff, #e8f0fe);
    color: #1f2937;
}
.main-title {
    text-align:center;
    font-size:2.6rem;
    color:#1E3A8A;
    font-weight:700;
    margin-bottom:1rem;
}
.subtext {
    text-align:center;
    font-size:1.1rem;
    color:#374151;
    margin-bottom:2rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# 🧭 SIDEBAR NAVIGATION
# ------------------------------------------------
st.sidebar.title("🌍 AQI Predictor Menu")
page = st.sidebar.radio("Navigate to:", ["🏠 Prediction", "📊 Model Comparison", "📖 About Air Pollution"])
st.sidebar.markdown("---")
st.sidebar.caption("💡 Developed with Streamlit + Multiple ML Models")

# ==========================================================
# PAGE 1️⃣ — AQI PREDICTION PAGE
# ==========================================================
if page == "🏠 Prediction":

    st.markdown("<div class='main-title'>🌍 Air Quality Index (AQI) Predictor</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Predict the overall Air Quality Index using pollutant AQI values</div>", unsafe_allow_html=True)

    # Model Selection
    model_choice = st.selectbox("🧠 Choose a Model", list(models.keys()))

    # Input Sliders
    st.write("### 🧪 Enter Pollutant AQI Values")
    col1, col2 = st.columns(2)
    with col1:
        CO_AQI_Value = st.slider("CO AQI (0–300)", 0, 300, 50)
        NO2_AQI_Value = st.slider("NO₂ AQI (0–400)", 0, 400, 60)
    with col2:
        Ozone_AQI_Value = st.slider("Ozone AQI (0–300)", 0, 300, 80)
        PM25_AQI_Value = st.slider("PM2.5 AQI (0–500)", 0, 500, 120)

    st.markdown("<br>", unsafe_allow_html=True)

    # ------------------------------------------------
    # 🚀 Prediction Section
    # ------------------------------------------------
    if st.button("🔍 Predict AQI Level", key="predict"):
        model = models.get(model_choice)

        if not model:
            st.error(f"⚠️ '{model_choice}' model file not found in the project folder.")
        else:
            sample = np.array([[CO_AQI_Value, Ozone_AQI_Value, NO2_AQI_Value, PM25_AQI_Value]])
            prediction = model.predict(sample)[0]

            # AQI classification
            if prediction <= 50:
                aqi_status, color, msg, bg = "Good", "🟢", "Air quality is excellent.", "#00e400"
            elif prediction <= 100:
                aqi_status, color, msg, bg = "Moderate", "🟡", "Acceptable; minor concern for sensitive groups.", "#ffff00"
            elif prediction <= 150:
                aqi_status, color, msg, bg = "Unhealthy (Sensitive)", "🟠", "Children or elderly may experience effects.", "#ff7e00"
            elif prediction <= 200:
                aqi_status, color, msg, bg = "Unhealthy", "🔴", "Health effects possible for everyone.", "#ff0000"
            elif prediction <= 300:
                aqi_status, color, msg, bg = "Very Unhealthy", "🟣", "Emergency health warning conditions.", "#8f3f97"
            else:
                aqi_status, color, msg, bg = "Hazardous", "⚫", "Serious health effects for the entire population.", "#7e0023"

            # Result card (black background, white text)
            st.markdown(
                f"""
                <div style='
                background-color:black;
                padding:2rem;
                border-radius:20px;
                text-align:center;
                color:white;
                box-shadow:0 4px 15px rgba(0,0,0,0.5);
                transition: all 0.3s ease;
                margin-top:20px;
            '>
                <h2 style='font-size:2rem; font-weight:700;'>{color} Predicted AQI: {prediction:.2f}</h2>
                <h3 style='font-size:1.5rem;'>Status: {aqi_status}</h3>
                <p style='font-size:1.1rem; opacity:0.9;'>{msg}</p>
            </div>
            """, unsafe_allow_html=True
            )

            # Gauge chart
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prediction,
                title={'text': "Predicted AQI"},
                gauge={
                    'axis': {'range': [0, 500]},
                    'bar': {'color': bg},
                    'steps': [
                        {'range': [0, 50], 'color': "#00e400"},
                        {'range': [51, 100], 'color': "#ffff00"},
                        {'range': [101, 150], 'color': "#ff7e00"},
                        {'range': [151, 200], 'color': "#ff0000"},
                        {'range': [201, 300], 'color': "#8f3f97"},
                        {'range': [301, 500], 'color': "#7e0023"}
                    ]
                }
            ))
            st.plotly_chart(fig, use_container_width=True)

            # ------------------------------------------------
            # 📝 DOWNLOAD REPORT SECTION
            # ------------------------------------------------
            report = f"""
🌍 **AQI Prediction Report**

**Selected Model:** {model_choice}  
**Predicted AQI:** {prediction:.2f}  
**Status:** {aqi_status} {color}  
**Message:** {msg}

**Pollutant Inputs:**
- CO AQI Value: {CO_AQI_Value}
- NO₂ AQI Value: {NO2_AQI_Value}
- Ozone AQI Value: {Ozone_AQI_Value}
- PM2.5 AQI Value: {PM25_AQI_Value}

⚙️ *Generated via AQI Predictor Dashboard (Streamlit App)*
"""
            st.download_button(
                label="📄 Download AQI Report",
                data=report,
                file_name="AQI_Prediction_Report.txt",
                mime="text/plain"
            )

    # Model info expander
    with st.expander("ℹ️ About This Model"):
        st.write(f"""
        - **Selected Model:** {model_choice}  
        - **Training Data:** Historical AQI pollutant records  
        - **Features Used:** CO, Ozone, NO₂, PM2.5  
        - **Target Variable:** Overall AQI  
        - **Evaluation Metrics:**  
            - R² Score ≈ 0.99 
            - Root Mean Squared Error ≈ 4.35  
        """)

# ==========================================================
# PAGE 2️⃣ — MODEL COMPARISON
# ==========================================================
elif page == "📊 Model Comparison":
    st.markdown("<div class='main-title'>📊 Model Comparison Dashboard</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Compare the performance of different AQI prediction models</div>", unsafe_allow_html=True)

    performance_data = pd.DataFrame({
        "Model": ["XGBoost Regressor", "Linear Regression", "Lasso Regression", "Ridge Regression"],
        "Accuracy" : [99.3,79.3,97.3,97.2],
        "R² Score": [0.99, 0.79, 0.97, 0.97],
        "Root Mean Squared Error": [4.35, 8.44, 6.54, 6.32]
    })

    st.dataframe(performance_data, use_container_width=True)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=performance_data["Model"], y=performance_data["R² Score"], name="R² Score"))
    fig.add_trace(go.Bar(x=performance_data["Model"], y=performance_data["Root Mean Squared Error"], name="RMSE"))
    fig.add_trace(go.Bar(x=performance_data["Model"], y=performance_data["Accuracy"], name="Accuracy"))
    fig.update_layout(
        barmode="group",
        title="Model Performance Comparison",
        xaxis_title="Model",
        yaxis_title="Score / Error",
        legend_title="Metric"
    )
    st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# PAGE 3️⃣ — ABOUT AIR POLLUTION
# ==========================================================
elif page == "📖 About Air Pollution":
    st.markdown("<div class='main-title'>🌫️ Understanding Air Pollution & AQI</div>", unsafe_allow_html=True)
    st.markdown("""
    Air pollution refers to the presence of harmful or excessive quantities of substances in the air.  
    The **Air Quality Index (AQI)** is a standardized system for measuring and comparing air pollution levels.

    ### 🧩 Major Pollutants:
    - **CO (Carbon Monoxide):** Produced by incomplete fuel combustion. Affects oxygen delivery in the body.  
    - **NO₂ (Nitrogen Dioxide):** From vehicles and industries. Causes respiratory irritation.  
    - **O₃ (Ozone):** Formed by sunlight reacting with pollutants. Harms lungs and plants.  
    - **PM2.5:** Fine particles <2.5μm. Penetrate deep into lungs, causing long-term diseases.

    ### ⚙️ AQI Scale:
    | AQI Range | Category | Health Impact |
    |------------|-----------|----------------|
    | 0–50 | 🟢 Good | Air quality is satisfactory |
    | 51–100 | 🟡 Moderate | Acceptable; minor concern for sensitive people |
    | 101–150 | 🟠 Unhealthy (Sensitive) | May affect sensitive individuals |
    | 151–200 | 🔴 Unhealthy | Affects everyone |
    | 201–300 | 🟣 Very Unhealthy | Emergency conditions |
    | 301–500 | ⚫ Hazardous | Serious health effects for all |

    🌱 **Tip:** Using electric vehicles, planting trees, and reducing industrial emissions can help improve AQI.
    """)
