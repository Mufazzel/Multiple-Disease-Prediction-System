"""
Sidebar component for Streamlit Disease Prediction System.
"""
import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/stethoscope.png", width=64)
        st.markdown("### Clinical Diagnostic Center")
        st.markdown("Machine Learning disease risk assessment.")
        st.markdown("---")
        
        selected_disease = st.radio(
            "Select Prediction Module:",
            [
                "🩸 Diabetes Prediction",
                "🫀 Heart Disease Prediction",
                "🧠 Parkinson's Disease Prediction"
            ]
        )
        st.markdown("---")
        st.markdown("#### ⚙️ System Engine")
        st.info("**100% Python Architecture**\n- Scikit-Learn Supervised ML\n- NumPy Vector Engine\n- Streamlit Interactive Web Interface")
        return selected_disease
