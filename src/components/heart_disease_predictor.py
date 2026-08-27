"""
Python Heart Disease Predictor Component
"""
import streamlit as st
from python.heart_disease_model import HeartDiseaseModel
from src.presets import HEART_PRESETS
from src.components import render_result_card

def render_heart_predictor(model: HeartDiseaseModel):
    st.markdown('<div class="main-header">🫀 Heart Disease Risk Assessment</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Logistic Regression Classifier trained on the UCI Cleveland Cardiovascular Dataset</div>', unsafe_allow_html=True)
    
    st.markdown("##### ⚡ Quick Load Clinical Presets")
    cols = st.columns(len(HEART_PRESETS))
    for i, preset in enumerate(HEART_PRESETS):
        with cols[i]:
            if st.button(preset["name"], key=f"btn_hd_{preset['id']}"):
                for k, v in preset["data"].items():
                    st.session_state[f"hd_{k}"] = v

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Patient Age", min_value=1, max_value=120, value=int(st.session_state.get('hd_age', 55)))
        sex = st.selectbox("Sex", options=[("Male (1)", 1), ("Female (0)", 0)], format_func=lambda x: x[0])[1]
        cp = st.selectbox("Chest Pain Type (CP)", options=[
            ("0 - Typical Angina", 0),
            ("1 - Atypical Angina", 1),
            ("2 - Non-anginal Pain", 2),
            ("3 - Asymptomatic", 3)
        ], format_func=lambda x: x[0])[1]
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=250, value=int(st.session_state.get('hd_trestbps', 130)))
        chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=100, max_value=600, value=int(st.session_state.get('hd_chol', 240)))

    with col2:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[("No (0)", 0), ("Yes (1)", 1)], format_func=lambda x: x[0])[1]
        restecg = st.selectbox("Resting ECG Results", options=[
            ("0 - Normal", 0),
            ("1 - ST-T Wave Abnormality", 1),
            ("2 - Left Ventricular Hypertrophy", 2)
        ], format_func=lambda x: x[0])[1]
        thalach = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250, value=int(st.session_state.get('hd_thalach', 150)))
        exang = st.selectbox("Exercise Induced Angina", options=[("No (0)", 0), ("Yes (1)", 1)], format_func=lambda x: x[0])[1]

    with col3:
        oldpeak = st.number_input("ST Depression Induced by Exercise (Oldpeak)", min_value=0.0, max_value=10.0, value=float(st.session_state.get('hd_oldpeak', 1.0)), step=0.1)
        slope = st.selectbox("Peak Exercise ST Segment Slope", options=[
            ("0 - Upsloping", 0),
            ("1 - Flat", 1),
            ("2 - Downsloping", 2)
        ], format_func=lambda x: x[0])[1]
        ca = st.selectbox("Major Vessels Colored by Fluoroscopy (0-4)", options=[0, 1, 2, 3, 4], index=int(st.session_state.get('hd_ca', 0)))
        thal = st.selectbox("Thalassemia Status", options=[
            ("0 - Normal", 0),
            ("1 - Fixed Defect", 1),
            ("2 - Reversible Defect", 2)
        ], format_func=lambda x: x[0])[1]

    if st.button("🔍 Execute Cardiovascular Diagnostic Test"):
        data = {
            'age': age, 'sex': sex, 'cp': cp, 'trestbps': trestbps, 'chol': chol,
            'fbs': fbs, 'restecg': restecg, 'thalach': thalach, 'exang': exang,
            'oldpeak': oldpeak, 'slope': slope, 'ca': ca, 'thal': thal
        }
        res = model.predict(data)
        render_result_card(res, "Heart Disease")
