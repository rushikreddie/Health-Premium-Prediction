import streamlit as st
import streamlit.components.v1 as components
from prediction_helper import predict

st.set_page_config(
    page_title="Health Premium Estimator",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----------------------------------------------------------------------------
# DESIGN SYSTEM
# A "vitals monitor" aesthetic: deep clinical navy, a coral heartbeat-line
# motif as the page's signature element, and monospace type for anything
# numeric — the visual language of a readout, not a generic form.
# ----------------------------------------------------------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap');

:root{
    --bg:#0E1A24;
    --bg-soft:#101E2A;
    --surface:#16283A;
    --surface-hover:#1C3247;
    --border:#24405A;
    --coral:#FF6F59;
    --coral-soft:rgba(255,111,89,0.14);
    --teal:#2DD4BF;
    --text:#F4F7F6;
    --text-muted:#8FA3B0;
    --font-display:'Space Grotesk', sans-serif;
    --font-body:'Inter', sans-serif;
    --font-mono:'JetBrains Mono', monospace;
}

html, body, [class*="css"]{ font-family: var(--font-body); }

.stApp{
    background:
        radial-gradient(circle at 12% -8%, rgba(255,111,89,0.10), transparent 45%),
        radial-gradient(circle at 90% 10%, rgba(45,212,191,0.08), transparent 40%),
        var(--bg);
    color: var(--text);
}

#MainMenu{ visibility:hidden; }
footer{ visibility:hidden; }
header[data-testid="stHeader"]{ background: transparent; }

.block-container{
    padding-top: 2.2rem;
    padding-bottom: 3rem;
    max-width: 1080px;
}

h1, h2, h3, h4 { font-family: var(--font-display); color: var(--text); }

/* ---------- Hero ---------- */
.hero-eyebrow{
    font-family: var(--font-mono);
    text-transform: uppercase;
    letter-spacing: 0.18em;
    font-size: 0.78rem;
    color: var(--teal);
    margin-bottom: 0.6rem;
}
.hero-title{
    font-family: var(--font-display);
    font-weight: 700;
    font-size: 2.7rem;
    line-height: 1.1;
    margin: 0;
    background: linear-gradient(100deg, #FFFFFF 35%, var(--coral) 110%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
}
.hero-sub{
    color: var(--text-muted);
    font-size: 1.02rem;
    max-width: 560px;
    margin-top: 0.7rem;
    line-height: 1.5;
}

/* Signature element: a scrolling ECG / pulse line, used sparingly */
.pulse-line{
    height: 42px;
    margin: 1.3rem 0 1.8rem 0;
    background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 160 60'><path d='M0 30 L40 30 L46 22 L52 38 L58 6 L64 54 L70 30 L76 27 L82 30 L160 30' fill='none' stroke='%23FF6F59' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'/></svg>");
    background-repeat: repeat-x;
    background-size: 160px 100%;
    opacity: 0.8;
    animation: pulse-scroll 3.4s linear infinite;
}
.pulse-line.subtle{ opacity:0.35; height:26px; }
@keyframes pulse-scroll{
    from{ background-position-x: 0; }
    to{ background-position-x: -160px; }
}
@media (prefers-reduced-motion: reduce){
    .pulse-line{ animation: none; }
}

/* ---------- Vitals strip (live selection summary) ---------- */
.vitals-strip{
    display:flex; flex-wrap:wrap; gap:0.6rem;
    margin: 0.4rem 0 1.6rem 0;
}
.vital-chip{
    display:flex; align-items:center; gap:0.5rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 999px;
    padding: 0.45rem 1rem;
    font-family: var(--font-mono);
    font-size: 0.78rem;
    color: var(--text-muted);
}
.vital-chip .dot{
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--teal);
    box-shadow: 0 0 8px var(--teal);
}
.vital-chip strong{ color: var(--text); font-weight: 600; }

/* ---------- Section cards ---------- */
div[data-testid="stVerticalBlockBorderWrapper"]{
    background: var(--surface);
    border: 1px solid var(--border) !important;
    border-radius: 18px !important;
    padding: 0.4rem 0.2rem;
    margin-bottom: 1.1rem;
    transition: border-color 0.25s ease, box-shadow 0.25s ease;
}
div[data-testid="stVerticalBlockBorderWrapper"]:hover{
    border-color: var(--coral) !important;
    box-shadow: 0 10px 32px rgba(0,0,0,0.25);
}

.section-header{
    display:flex; align-items:center; gap:0.85rem;
    margin: 0.4rem 0 1.2rem 0;
    padding-bottom: 0.9rem;
    border-bottom: 1px solid var(--border);
}
.section-icon{
    font-size: 1.4rem; width:44px; height:44px; flex-shrink:0;
    display:flex; align-items:center; justify-content:center;
    background: var(--coral-soft);
    border-radius: 12px;
}
.section-title{
    font-family: var(--font-display);
    font-size: 1.08rem; font-weight:600; color: var(--text);
}
.section-sub{
    font-size: 0.8rem; color: var(--text-muted); margin-top: 1px;
}

/* ---------- Inputs ---------- */
.stNumberInput label, .stSelectbox label{
    font-family: var(--font-body) !important;
    font-size: 0.74rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: var(--text-muted) !important;
}
.stNumberInput input, .stSelectbox div[data-baseweb="select"] > div{
    background: var(--bg-soft) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text) !important;
    font-family: var(--font-mono) !important;
}
.stNumberInput input:focus, .stSelectbox div[data-baseweb="select"]:focus-within > div{
    border-color: var(--coral) !important;
    box-shadow: 0 0 0 3px var(--coral-soft) !important;
}
.stNumberInput button{
    background: var(--bg-soft) !important;
    border-color: var(--border) !important;
    color: var(--text-muted) !important;
}
div[data-baseweb="popover"] li{
    background: var(--surface) !important;
    color: var(--text) !important;
}
div[data-baseweb="popover"] li:hover{
    background: var(--surface-hover) !important;
}

/* ---------- Predict button ---------- */
.stButton > button{
    width: 100%;
    background: linear-gradient(135deg, var(--coral) 0%, #E8503B 100%);
    color: #fff;
    border: none;
    border-radius: 14px;
    padding: 0.95rem 1rem;
    font-family: var(--font-display);
    font-weight: 600;
    font-size: 1.05rem;
    letter-spacing: 0.02em;
    box-shadow: 0 8px 24px rgba(255,111,89,0.28);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.stButton > button:hover{
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(255,111,89,0.4);
}
.stButton > button:active{ transform: translateY(0); }
.stButton > button:focus-visible{
    outline: 2px solid var(--teal);
    outline-offset: 3px;
}

.disclaimer{
    font-size: 0.78rem;
    color: var(--text-muted);
    text-align:center;
    margin-top: 0.8rem;
}

/* scrollbar polish */
::-webkit-scrollbar{ width: 10px; }
::-webkit-scrollbar-track{ background: var(--bg); }
::-webkit-scrollbar-thumb{ background: var(--border); border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# HERO
# ----------------------------------------------------------------------------
# st.markdown('<div class="hero-eyebrow">Predictive risk modeling · Random Forest + XGBoost + Monte Carlo</div>', unsafe_allow_html=True)
st.markdown('<h1 class="hero-title">Health Insurance Premium Estimator</h1>', unsafe_allow_html=True)
st.markdown(
    '<div class="hero-sub">Enter a profile below and the model reads it — '
    'demographic, financial, and health signals — to estimate an annual premium.</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="pulse-line"></div>', unsafe_allow_html=True)

# ----------------------------------------------------------------------------
# FORM DATA
# ----------------------------------------------------------------------------
categorical_options = {
    'Gender': ['Male', 'Female'],
    'Marital Status': ['Unmarried', 'Married'],
    'BMI Category': ['Normal', 'Obesity', 'Overweight', 'Underweight'],
    'Smoking Status': ['No Smoking', 'Regular', 'Occasional'],
    'Employment Status': ['Salaried', 'Self-Employed', 'Freelancer', ''],
    'Region': ['Northwest', 'Southeast', 'Northeast', 'Southwest'],
    'Medical History': [
        'No Disease', 'Diabetes', 'High blood pressure', 'Diabetes & High blood pressure',
        'Thyroid', 'Heart disease', 'High blood pressure & Heart disease', 'Diabetes & Thyroid',
        'Diabetes & Heart disease'
    ],
    'Insurance Plan': ['Bronze', 'Silver', 'Gold']
}

# ----------------------------------------------------------------------------
# SECTION 1 — PERSONAL DETAILS
# ----------------------------------------------------------------------------
with st.container(border=True):
    st.markdown(
        '<div class="section-header"><span class="section-icon">🧍</span>'
        '<div><div class="section-title">Personal Details</div>'
        '<div class="section-sub">Who the policy is for</div></div></div>',
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        age = st.number_input('Age', min_value=18, step=1, max_value=100)
        gender = st.selectbox('Gender', categorical_options['Gender'])
    with c2:
        marital_status = st.selectbox('Marital Status', categorical_options['Marital Status'])
        region = st.selectbox('Region', categorical_options['Region'])

# ----------------------------------------------------------------------------
# SECTION 2 — FAMILY & FINANCES
# ----------------------------------------------------------------------------
with st.container(border=True):
    st.markdown(
        '<div class="section-header"><span class="section-icon">💼</span>'
        '<div><div class="section-title">Family &amp; Finances</div>'
        '<div class="section-sub">Income, dependants, and coverage tier</div></div></div>',
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        number_of_dependants = st.number_input('Number of Dependants', min_value=0, step=1, max_value=20)
        employment_status = st.selectbox(
            'Employment Status',
            categorical_options['Employment Status'],
            format_func=lambda x: x if x else 'Not Specified',
        )
    with c2:
        income_lakhs = st.number_input('Income in Lakhs', step=1, min_value=0, max_value=200)
        insurance_plan = st.selectbox('Insurance Plan', categorical_options['Insurance Plan'])

# ----------------------------------------------------------------------------
# SECTION 3 — HEALTH PROFILE
# ----------------------------------------------------------------------------
with st.container(border=True):
    st.markdown(
        '<div class="section-header"><span class="section-icon">🩺</span>'
        '<div><div class="section-title">Health Profile</div>'
        '<div class="section-sub">The signals that move risk the most</div></div></div>',
        unsafe_allow_html=True,
    )
    c1, c2 = st.columns(2)
    with c1:
        bmi_category = st.selectbox('BMI Category', categorical_options['BMI Category'])
        smoking_status = st.selectbox('Smoking Status', categorical_options['Smoking Status'])
    with c2:
        medical_history = st.selectbox('Medical History', categorical_options['Medical History'])
        genetical_risk = st.number_input('Genetical Risk', step=1, min_value=0, max_value=5)

# ----------------------------------------------------------------------------
# LIVE VITALS STRIP
# ----------------------------------------------------------------------------
st.markdown(
    f'''
    <div class="vitals-strip">
        <div class="vital-chip"><span class="dot"></span>Plan&nbsp;<strong>{insurance_plan}</strong></div>
        <div class="vital-chip"><span class="dot"></span>BMI&nbsp;<strong>{bmi_category}</strong></div>
        <div class="vital-chip"><span class="dot"></span>Smoking&nbsp;<strong>{smoking_status}</strong></div>
        <div class="vital-chip"><span class="dot"></span>Region&nbsp;<strong>{region}</strong></div>
    </div>
    ''',
    unsafe_allow_html=True,
)

# ----------------------------------------------------------------------------
# INPUT DICT (unchanged keys — matches prediction_helper.predict)
# ----------------------------------------------------------------------------
input_dict = {
    'Age': age,
    'Number of Dependants': number_of_dependants,
    'Income in Lakhs': income_lakhs,
    'Genetical Risk': genetical_risk,
    'Insurance Plan': insurance_plan,
    'Employment Status': employment_status,
    'Gender': gender,
    'Marital Status': marital_status,
    'BMI Category': bmi_category,
    'Smoking Status': smoking_status,
    'Region': region,
    'Medical History': medical_history
}

# ----------------------------------------------------------------------------
# PREDICT
# ----------------------------------------------------------------------------
predict_clicked = st.button('Estimate My Premium')

if predict_clicked:
    with st.spinner('Reading vitals and running the model…'):
        prediction = predict(input_dict)

    plan_styles = {
        'Bronze': ('#CD7F32', 'rgba(205,127,50,0.16)'),
        'Silver': ('#C7CDD4', 'rgba(199,205,212,0.16)'),
        'Gold':   ('#FFD56B', 'rgba(255,213,107,0.16)'),
    }
    badge_color, badge_bg = plan_styles.get(insurance_plan, ('#FF6F59', 'rgba(255,111,89,0.16)'))

    try:
        numeric_prediction = float(prediction)
        is_numeric = True
    except (TypeError, ValueError):
        numeric_prediction = 0
        is_numeric = False

    if is_numeric:
        result_html = """
        <style>
            .result-card{
                font-family:'Inter', sans-serif;
                background: linear-gradient(160deg, #16283A 0%, #101E2A 100%);
                border: 1px solid #24405A;
                border-radius: 20px;
                padding: 2.1rem 1.5rem 1.8rem 1.5rem;
                text-align:center;
                animation: cardReveal .55s ease-out;
            }
            @keyframes cardReveal{
                from{ opacity:0; transform: translateY(14px) scale(.98); }
                to{ opacity:1; transform: translateY(0) scale(1); }
            }
            .result-eyebrow{
                font-family:'JetBrains Mono', monospace;
                text-transform:uppercase; letter-spacing:.14em;
                font-size:.74rem; color:#2DD4BF; margin-bottom:.5rem;
            }
            .premium-value{
                font-family:'JetBrains Mono', monospace;
                font-size: 3rem; font-weight:700; color:#FF6F59; letter-spacing:-0.01em;
            }
            .premium-sub{ font-size:.82rem; color:#8FA3B0; margin-top:.4rem; }
            .plan-badge{
                display:inline-block; margin-top:1rem;
                padding:.35rem 1.05rem; border-radius:999px;
                font-size:.74rem; font-weight:700; letter-spacing:.05em; text-transform:uppercase;
                color: BADGE_COLOR; background: BADGE_BG; border: 1px solid BADGE_COLOR;
            }
        </style>
        <div class="result-card">
            <div class="result-eyebrow">Estimated Annual Premium</div>
            <div class="premium-value" id="premium-value">₹0</div>
            <div class="premium-sub">Based on the profile entered above</div>
            <div class="plan-badge">PLAN_NAME Plan</div>
        </div>
        <script>
            (function(){
                const target = TARGET_VALUE;
                const el = document.getElementById('premium-value');
                const duration = 1100;
                const start = performance.now();
                function frame(now){
                    const t = Math.min((now - start) / duration, 1);
                    const eased = 1 - Math.pow(1 - t, 3);
                    const current = Math.round(target * eased);
                    el.innerText = '₹' + current.toLocaleString('en-IN');
                    if(t < 1){ requestAnimationFrame(frame); }
                }
                requestAnimationFrame(frame);
            })();
        </script>
        """
        result_html = (
            result_html
            .replace('BADGE_COLOR', badge_color)
            .replace('BADGE_BG', badge_bg)
            .replace('PLAN_NAME', insurance_plan)
            .replace('TARGET_VALUE', str(numeric_prediction))
        )
        components.html(result_html, height=300)
    else:
        st.markdown(
            f'''
            <div style="background:linear-gradient(160deg,#16283A,#101E2A);border:1px solid #24405A;
                        border-radius:20px;padding:2rem;text-align:center;">
                <div style="font-family:'JetBrains Mono',monospace;text-transform:uppercase;
                            letter-spacing:.14em;font-size:.74rem;color:#2DD4BF;margin-bottom:.6rem;">
                    Estimated Annual Premium
                </div>
                <div style="font-family:'JetBrains Mono',monospace;font-size:2.2rem;
                            font-weight:700;color:#FF6F59;">{prediction}</div>
            </div>
            ''',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="disclaimer">This is a model-based estimate, not a final quote — '
        'actual premiums may vary based on insurer underwriting.</div>',
        unsafe_allow_html=True,
    )