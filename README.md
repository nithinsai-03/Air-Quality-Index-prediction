# 🌍 Air Quality Index (AQI) Prediction Dashboard  

## 🧠 Overview  
The **Air Quality Index (AQI) Prediction Dashboard** is a **machine learning web application** built with **Streamlit** that predicts the overall AQI based on major air pollutants such as **CO, NO₂, O₃, and PM2.5**.  

It integrates multiple regression models — **XGBoost, Linear Regression, Lasso, and Ridge Regression** — allowing users to compare performance and visualize results interactively.  

---

## 🚀 Features  
- 🧩 **Multiple ML Models:** XGBoost, Linear, Lasso, and Ridge Regressors.  
- 🎛️ **Interactive Input Sliders:** Enter pollutant AQI values dynamically.  
- 📈 **Gauge Visualization:** Real-time AQI visualization using Plotly.  
- 🗂️ **Download Report:** Export prediction results as a text file.  
- 📊 **Model Comparison Page:** Compare R² scores and MSE values.  
- 📖 **Air Pollution Info Page:** Educational section explaining pollutants and AQI scale.  
- 🧠 **Accurate Predictions:** Trained on historical AQI data with high R² (≈0.99).  

---

## 🧰 Tech Stack  
| Component | Technology |
|------------|-------------|
| **Frontend / UI** | Streamlit |
| **Backend (Model)** | Python (scikit-learn, XGBoost) |
| **Visualization** | Plotly, Pandas |
| **Model Persistence** | joblib |
| **Dataset** | Historical Air Quality Data |

---

## ⚙️ Installation  


# ------------------------------------------------
# 1️⃣ Clone the Repository
# ------------------------------------------------
# Clone your project from GitHub
git clone https://github.com/<your-username>/aqi-predictor-dashboard.git

# Navigate to the project folder
cd aqi-predictor-dashboard


# ------------------------------------------------
# 2️⃣ Create a Virtual Environment
# ------------------------------------------------
# Create a new Python virtual environment
python -m venv ml_venv

# Activate the virtual environment

# 🪟 Windows (Command Prompt)
ml_venv\Scripts\activate

# 🪟 Windows (PowerShell)
.\ml_venv\Scripts\activate

# 🐧 macOS / Linux
source ml_venv/bin/activate


# ------------------------------------------------
# 3️⃣ Install Dependencies
# ------------------------------------------------
# Upgrade pip to the latest version
pip install --upgrade pip

# Install all required libraries
pip install streamlit numpy pandas scikit-learn xgboost plotly joblib

# Optional — Save dependencies to a requirements.txt file
pip freeze > requirements.txt


# ------------------------------------------------
# 4️⃣ Run the Application
# ------------------------------------------------
# Launch the Streamlit AQI Predictor Dashboard
streamlit run aqi_predictor_app.py


# ------------------------------------------------
# 5️⃣ (Optional) Project Folder Structure
# ------------------------------------------------
# You can organize your project as follows:

# aqi-predictor-dashboard/
# ├── aqi_predictor_app.py       # Main Streamlit app file
# ├── linear_regression.pkl      # Linear Regression model
# ├── lasso.pkl                  # Lasso model
# ├── ridge.pkl                  # Ridge model
# ├── best_model.pkl             # XGBoost (best) model
# ├── requirements.txt           # Dependencies list
# ├── README.md                  # Project description
# └── SETUP.md                   # (This setup file)


# ------------------------------------------------
# ✅ You’re all set!
# ------------------------------------------------
# Once the app launches, open your browser at:
# 👉 http://localhost:8501

