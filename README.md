<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06b6d4,100:6366f1&height=200&section=header&text=Health%20Premium%20Prediction&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=ML-Powered%20Insurance%20Premium%20Estimator&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<!-- Badges Row -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-Powered-EC7D2C?style=for-the-badge&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Live-22c55e?style=for-the-badge"/>
</p>

<!-- Live Demo Button -->
<a href="https://health-premium-prediction-by-rushik-reddy.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Click%20Here-6366f1?style=for-the-badge&labelColor=1e1b4b"/>
</a>

<br/><br/>

<!-- Animated Divider -->
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

</div>

---

## 🧠 About The Project

> **Health Premium Prediction** is an end-to-end machine learning system that predicts health insurance premiums based on personal, medical, and lifestyle attributes. It uses a **segmented modeling strategy** — separate models for **young adults (age ≤ 25)** and **rest of population (age > 25)** — achieving superior accuracy over a single global model.

The project spans the complete ML lifecycle: **data exploration → feature engineering → model training → hyperparameter tuning → Streamlit deployment**.

---

## ✨ Key Highlights

| 🔍 Feature | 📋 Details |
|---|---|
| 🎯 **Dual Segmentation** | Separate models for Young (≤25) & Rest (>25) age groups |
| 🌳 **Random Forest** | Baseline ensemble model with feature importance analysis |
| ⚡ **XGBoost** | Gradient boosting with tuned hyperparameters for high accuracy |
| 📊 **EDA & Visualization** | Deep exploratory analysis with Matplotlib & Seaborn |
| 🌐 **Live Web App** | Interactive Streamlit interface for real-time predictions |
| 📁 **Modular Notebooks** | Clean, iterative development across multiple notebooks |

---

## 🗂️ Repository Structure

```
Health-Premium-Prediction/
│
├── 📓 ML_Preminu_Prediction.ipynb              # Core EDA & baseline modeling
├── 📓 ML_Splitting_Data.ipynb                  # Data segmentation (Young vs Rest)
├── 📓 ML_Preminu_Prediction_Young.ipynb        # Model for age ≤ 25
├── 📓 ML_Preminu_Prediction_Rest.ipynb         # Model for age > 25
├── 📓 ML_Preminu_Prediction_Young_With_Gr.ipynb  # Young model + Genetical Risk
├── 📓 ML_Preminu_Prediction_Rest_With_Gr.ipynb   # Rest model + Genetical Risk
│
├── 📊 premiums.xlsx                            # Full dataset
├── 📊 premiums_young.xlsx                      # Young segment data
├── 📊 premiums_rest.xlsx                       # Rest segment data
├── 📊 premiums_young_with_gr.xlsx              # Young + genetical risk data
│
├── 🌐 app/                                     # Streamlit web application
│
└── 📋 requirements.txt                         # Python dependencies
```

---

## 🔬 ML Pipeline

```
Raw Data
   │
   ▼
┌─────────────────────────┐
│   Exploratory Analysis  │  ← Distributions, correlations, outlier detection
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│    Data Segmentation    │  ← Split by age: Young (≤25) | Rest (>25)
└──────┬──────────────────┘
       │
  ┌────┴────┐
  ▼         ▼
Young      Rest
Model      Model
  │         │
  └────┬────┘
       │
       ▼
┌─────────────────────────┐
│  Feature Engineering    │  ← Encoding, scaling, genetical risk feature
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Model Training        │  ← Random Forest + XGBoost
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ Hyperparameter Tuning   │  ← GridSearchCV / RandomizedSearchCV
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│   Streamlit Deployment  │  ← Live web app
└─────────────────────────┘
```

---

## 📥 Input Features

| Feature | Type | Description |
|---|---|---|
| 🎂 **Age** | Numeric | 18 – 100 years |
| 👨‍👩‍👧 **Number of Dependants** | Numeric | Financially dependent members |
| 💰 **Income (in Lakhs)** | Numeric | Annual income in ₹ |
| 🧬 **Genetical Risk** | 0–5 Scale | Family health history score |
| 🏥 **Insurance Plan** | Categorical | Bronze / Silver / Gold |
| 💼 **Employment Status** | Categorical | Salaried / Self-employed / Freelancer |
| 🚬 **Smoking Status** | Categorical | Non-smoker / Occasional / Regular |
| ⚖️ **BMI Category** | Categorical | Underweight / Normal / Overweight / Obese |
| 🩺 **Medical History** | Categorical | Pre-existing conditions |
| 🏙️ **Region** | Categorical | Geographic location |
| 👤 **Gender** | Categorical | Male / Female |
| 👨‍👩‍👦 **Marital Status** | Categorical | Married / Unmarried |

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-EC7D2C?style=for-the-badge&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white"/>
  <img src="https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Joblib-5cb85c?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Statsmodels-4B0082?style=for-the-badge&logo=python&logoColor=white"/>
</p>

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/rushikreddie/Health-Premium-Prediction.git
cd Health-Premium-Prediction

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the Streamlit app
streamlit run app/app.py
```

> The app will open at `http://localhost:8501` in your browser.

---

## 📊 Notebook Walkthrough

| Notebook | Purpose |
|---|---|
| `ML_Preminu_Prediction.ipynb` | Initial EDA, data understanding, baseline Random Forest |
| `ML_Splitting_Data.ipynb` | Age-based segmentation logic |
| `ML_Preminu_Prediction_Young.ipynb` | Model building for Young (≤25) segment |
| `ML_Preminu_Prediction_Rest.ipynb` | Model building for Rest (>25) segment |
| `ML_Preminu_Prediction_Young_With_Gr.ipynb` | Young model + Genetical Risk feature |
| `ML_Preminu_Prediction_Rest_With_Gr.ipynb` | Rest model + Genetical Risk feature (final) |

---

## 🌐 Live Application

<div align="center">

**🔗 [health-premium-prediction-by-rushik-reddy.streamlit.app](https://health-premium-prediction-by-rushik-reddy.streamlit.app/)**

*Enter your details → Get your estimated health insurance premium instantly*

</div>

---

## 👨‍💻 Author

<div align="center">

**Rushik Reddy**
B.Tech in Computer Science (AI Specialisation) · Dr. MGR Educational and Research Institute

<p>
  <a href="https://github.com/rushikreddie">
    <img src="https://img.shields.io/badge/GitHub-rushikreddie-181717?style=for-the-badge&logo=github"/>
  </a>
</p>

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:06b6d4&height=100&section=footer&animation=fadeIn" width="100%"/>

*Built with ❤️ and a lot of XGBoost*

</div>
