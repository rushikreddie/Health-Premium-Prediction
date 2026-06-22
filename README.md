<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:06b6d4,100:6366f1&height=200&section=header&text=Health%20Premium%20Prediction&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=ML-Powered%20Insurance%20Premium%20Estimator&descAlignY=58&descSize=18&animation=fadeIn" width="100%"/>

<!-- Badges -->
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-Powered-EC7D2C?style=for-the-badge&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/Status-Live-22c55e?style=for-the-badge"/>
</p>

<a href="https://health-premium-prediction-by-rushik-reddy.streamlit.app/" target="_blank">
  <img src="https://img.shields.io/badge/🚀%20Live%20Demo-Click%20Here-6366f1?style=for-the-badge&labelColor=1e1b4b"/>
</a>

<br/><br/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%"/>

</div>

---

## 🧠 About The Project

> **Health Premium Prediction** is a full end-to-end machine learning system that predicts health insurance premiums based on personal, medical, and lifestyle attributes. What makes this project unique is its **residual-driven segmentation strategy** — instead of blindly splitting data by age, the model is first trained on the full dataset, residuals and percentage errors are computed, and the **high-error cases are forensically analysed** to discover *why* the model struggles. That diagnosis — extreme errors concentrated in young policyholders (age ≤ 25) — then motivates a principled split into two specialised sub-models, each re-trained with a custom feature set including a **disease-based Genetical Risk Score**.

---

## 🔬 The Core Methodology (How It Actually Works)

The real innovation in this project is the **iterative, evidence-based approach** to model improvement:

### Phase 1 — Global Model & Residual Analysis
```
Full Dataset
     │
     ▼
 Data Cleaning ──► Remove age > 100, fix negative dependants,
                   cap income at 99.9th percentile
     │
     ▼
 Feature Engineering
  ├─ Disease Risk Score: diabetes=6, heart disease=8,
  │   high blood pressure=6, thyroid=5 → normalised 0–1
  ├─ Ordinal Encoding: Insurance Plan (Bronze=1, Silver=2, Gold=3)
  │                    Income Level (<10L=1 … >40L=4)
  └─ One-Hot Encoding: gender, region, marital_status,
                       bmi_category, smoking_status, employment_status
     │
     ▼
 Multicollinearity Check (VIF)
  └─ income_level dropped due to high VIF
     │
     ▼
 MinMax Scaling → age, dependants, income, insurance plan
     │
     ▼
 Train: Linear Regression | Ridge | XGBoost + RandomizedSearchCV
     │
     ▼
 Residual Analysis
  ├─ Compute: residuals_pct = (predicted - actual) / actual × 100
  ├─ Flag extreme errors: |error%| > 10%
  └─ Find: extreme_errors_pct → % of test set badly predicted
     │
     ▼
 Error Forensics (Reverse-Scale → Inspect Age Distribution)
  └─ FINDING: extreme errors concentrated in Age ≤ 25
```

### Phase 2 — Data Segmentation (Evidence-Driven)
```
premiums.xlsx
     ├──► premiums_young.xlsx  (Age ≤ 25)
     └──► premiums_rest.xlsx   (Age > 25)
```

> The split at age 25 is not arbitrary — it is the direct outcome of residual inspection. Young policyholders have fundamentally different premium patterns that a single model cannot capture.

### Phase 3 — Specialised Sub-Models
```
Young (≤ 25)                         Rest (> 25)
──────────────────                   ──────────────────
Linear Regression ✓ (best fit)       XGBoost + Tuning ✓
+ Genetical Risk feature             + Genetical Risk feature
```

Each sub-model goes through the complete pipeline independently: EDA → cleaning → risk scoring → encoding → VIF → scaling → training → residual check.

---

## 🗂️ Repository Structure

```
Health-Premium-Prediction/
│
├── 📓 ML_Preminu_Prediction.ipynb              # Phase 1: Global EDA, risk scoring,
│                                               #   full-data model, residual forensics
├── 📓 ML_Splitting_Data.ipynb                  # Age-based segmentation → export splits
│
├── 📓 ML_Preminu_Prediction_Young.ipynb        # Young segment model (no genetical risk)
├── 📓 ML_Preminu_Prediction_Young_With_Gr.ipynb# Young model + Genetical Risk (final)
├── 📓 ML_Preminu_Prediction_Rest.ipynb         # Rest segment model (no genetical risk)
├── 📓 ML_Preminu_Prediction_Rest_With_Gr.ipynb # Rest model + Genetical Risk (final)
│
├── 📊 premiums.xlsx                            # Full raw dataset
├── 📊 premiums_young.xlsx                      # Age ≤ 25 segment
├── 📊 premiums_rest.xlsx                       # Age > 25 segment
├── 📊 premiums_young_with_gr.xlsx              # Young + genetical risk column
│
├── 🌐 app/                                     # Streamlit web application
└── 📋 requirements.txt
```

---

## 🧬 Feature Engineering Details

### Disease Risk Scoring (Custom)

Medical history is parsed, split by `" & "`, and mapped to a weighted severity score:

| Disease | Risk Score |
|---|---|
| Heart Disease | 8 |
| Diabetes | 6 |
| High Blood Pressure | 6 |
| Thyroid | 5 |
| No Disease / None | 0 |

> Combined scores are then **min-max normalised to [0, 1]** as `normalized_risk_score`, used as a model feature.

### Encoding Strategy

| Type | Columns | Method |
|---|---|---|
| Ordinal | `insurance_plan` | Bronze=1, Silver=2, Gold=3 |
| Ordinal | `income_level` | `<10L`=1 → `>40L`=4 |
| Nominal | gender, region, marital_status, bmi_category, smoking_status, employment_status | One-Hot (drop_first=True) |

### Smoking Status Normalisation
Inconsistent labels (`'Smoking=0'`, `'Does Not Smoke'`, `'Not Smoking'`) are all unified to `'No Smoking'`.

### Multicollinearity Removal
VIF analysis showed `income_level` was collinear with `income_lakhs` → **dropped** from model features.

---

## 📥 Input Features

| Feature | Type | Description |
|---|---|---|
| 🎂 Age | Numeric | 18–100 |
| 👨‍👩‍👧 Number of Dependants | Numeric | Absolute value (negatives corrected) |
| 💰 Income (Lakhs) | Numeric | Capped at 99.9th percentile |
| 🧬 Genetical Risk | 0–5 Scale | Family health history score |
| 🏥 Insurance Plan | Bronze / Silver / Gold | Ordinal encoded |
| 💼 Employment Status | Categorical | One-hot encoded |
| 🚬 Smoking Status | Categorical | Normalised + encoded |
| ⚖️ BMI Category | Categorical | One-hot encoded |
| 🩺 Medical History | Text | Parsed → risk score |
| 🏙️ Region | Categorical | One-hot encoded |
| 👤 Gender | Categorical | One-hot encoded |
| 💍 Marital Status | Categorical | One-hot encoded |

---

## 🛠️ Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white"/>
  <img src="https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white"/>
  <img src="https://img.shields.io/badge/XGBoost-EC7D2C?style=for-the-badge&logo=xgboost&logoColor=white"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Seaborn-4c8cbf?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Statsmodels-4B0082?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Joblib-5cb85c?style=for-the-badge&logo=python&logoColor=white"/>
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

> Opens at `http://localhost:8501`

---

## 📓 Notebook Walkthrough

| Notebook | What Happens Inside |
|---|---|
| `ML_Preminu_Prediction.ipynb` | Full EDA, cleaning, risk scoring, Linear/Ridge/XGBoost, **residual % analysis**, error forensics, reverse-scaling to inspect age of extreme-error cases |
| `ML_Splitting_Data.ipynb` | Splits `premiums.xlsx` → `premiums_young.xlsx` and `premiums_rest.xlsx` by age ≤/> 25 |
| `ML_Preminu_Prediction_Young.ipynb` | Re-runs full pipeline on young segment (without genetical risk) |
| `ML_Preminu_Prediction_Young_With_Gr.ipynb` | Young model with `genetical_risk` scaled & added — **Linear Regression chosen as best** |
| `ML_Preminu_Prediction_Rest.ipynb` | Re-runs full pipeline on rest segment (without genetical risk) |
| `ML_Preminu_Prediction_Rest_With_Gr.ipynb` | Rest model with `genetical_risk` — **XGBoost + RandomizedSearchCV as best** |

---

## 🌐 Live Application

<div align="center">

**🔗 [health-premium-prediction-by-rushik-reddy.streamlit.app](https://health-premium-prediction-by-rushik-reddy.streamlit.app/)**

*Enter your details → the app routes you to the correct sub-model → get your estimated premium instantly*

</div>

---

## 👨‍💻 Author

<div align="center">

**Rushik Reddy**  
B.Tech in Computer Science (AI Specialisation) · Dr. MGR Educational and Research Institute · CGPA 8.66/10

<a href="https://github.com/rushikreddie">
  <img src="https://img.shields.io/badge/GitHub-rushikreddie-181717?style=for-the-badge&logo=github"/>
</a>

</div>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:6366f1,100:06b6d4&height=100&section=footer&animation=fadeIn" width="100%"/>

*Built with ❤️ and evidence-driven model iteration*
</div>
