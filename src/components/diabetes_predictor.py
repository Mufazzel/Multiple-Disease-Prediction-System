"""
Python Diabetes Predictor Component
"""
import streamlit as st
from python.diabetes_model import DiabetesModel
from src.presets import DIABETES_PRESETS
from src.components import render_result_card

def render_diabetes_predictor(model: DiabetesModel):
    st.markdown('<div class="main-header">🩸 Diabetes Risk Assessment</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Linear Support Vector Machine (SVM) trained on the PIMA Indians Diabetes Database</div>', unsafe_allow_html=True)
    
    st.markdown("##### ⚡ Quick Load Clinical Presets")
    cols = st.columns(len(DIABETES_PRESETS))
    for i, preset in enumerate(DIABETES_PRESETS):
        with cols[i]:
            if st.button(preset["name"], key=f"btn_dia_{preset['id']}"):
                for k, v in preset["data"].items():
                    st.session_state[f"dia_{k}"] = v

    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=int(st.session_state.get('dia_pregnancies', 1)), step=1)
        skin_thickness = st.number_input("Skin Fold Thickness (mm)", min_value=0.0, max_value=99.0, value=float(st.session_state.get('dia_skinThickness', 20.0)), step=1.0)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=float(st.session_state.get('dia_diabetesPedigree', 0.47)), step=0.01)
        
    with col2:
        glucose = st.number_input("Fasting Glucose Level (mg/dL)", min_value=0.0, max_value=300.0, value=float(st.session_state.get('dia_glucose', 120.0)), step=1.0)
        insulin = st.number_input("Serum Insulin (µU/mL)", min_value=0.0, max_value=850.0, value=float(st.session_state.get('dia_insulin', 79.0)), step=1.0)
        age = st.number_input("Patient Age (Years)", min_value=1, max_value=120, value=int(st.session_state.get('dia_age', 33)), step=1)
        
    with col3:
        blood_pressure = st.number_input("Diastolic Blood Pressure (mmHg)", min_value=0.0, max_value=200.0, value=float(st.session_state.get('dia_bloodPressure', 70.0)), step=1.0)
        bmi = st.number_input("Body Mass Index (BMI kg/m²)", min_value=0.0, max_value=70.0, value=float(st.session_state.get('dia_bmi', 32.0)), step=0.1)

    if st.button("🔍 Execute Diabetes Diagnostic Test"):
        data = {
            'pregnancies': pregnancies,
            'glucose': glucose,
            'bloodPressure': blood_pressure,
            'skinThickness': skin_thickness,
            'insulin': insulin,
            'bmi': bmi,
            'diabetesPedigree': dpf,
            'age': age
        }
        res = model.predict(data)
        render_result_card(res, "Diabetic")
