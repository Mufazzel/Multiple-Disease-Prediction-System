"""
Python Parkinson's Predictor Component
"""
import streamlit as st
from python.parkinsons_model import ParkinsonsModel
from src.presets import PARKINSONS_PRESETS
from src.components import render_result_card

def render_parkinsons_predictor(model: ParkinsonsModel):
    st.markdown('<div class="main-header">🧠 Parkinson\'s Disease Risk Assessment</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-header">Support Vector Classifier (SVM RBF) evaluating Oxford Vocal Acoustic Dysphonia Biomarkers</div>', unsafe_allow_html=True)
    
    st.markdown("##### ⚡ Quick Load Clinical Presets")
    cols = st.columns(len(PARKINSONS_PRESETS))
    for i, preset in enumerate(PARKINSONS_PRESETS):
        with cols[i]:
            if st.button(preset["name"], key=f"btn_park_{preset['id']}"):
                for k, v in preset["data"].items():
                    st.session_state[f"park_{k}"] = v

    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Fundamental Frequency Measures**")
        fo = st.number_input("MDVP:Fo (Hz) - Avg Vocal Freq", value=float(st.session_state.get('park_fo', 154.228)), format="%.3f")
        fhi = st.number_input("MDVP:Fhi (Hz) - Max Vocal Freq", value=float(st.session_state.get('park_fhi', 197.104)), format="%.3f")
        flo = st.number_input("MDVP:Flo (Hz) - Min Vocal Freq", value=float(st.session_state.get('park_flo', 116.324)), format="%.3f")
        nhr = st.number_input("NHR - Noise-to-Harmonics", value=float(st.session_state.get('park_nhr', 0.0248)), format="%.4f")
        hnr = st.number_input("HNR - Harmonics-to-Noise Ratio (dB)", value=float(st.session_state.get('park_hnr', 21.885)), format="%.3f")
        
    with col2:
        st.markdown("**Jitter (Frequency Variation)**")
        jitter_percent = st.number_input("MDVP:Jitter (%)", value=float(st.session_state.get('park_jitterPercent', 0.0062)), format="%.5f")
        jitter_abs = st.number_input("MDVP:Jitter (Abs)", value=float(st.session_state.get('park_jitterAbs', 0.000044)), format="%.6f")
        rap = st.number_input("MDVP:RAP", value=float(st.session_state.get('park_rap', 0.0033)), format="%.5f")
        ppq = st.number_input("MDVP:PPQ", value=float(st.session_state.get('park_ppq', 0.0034)), format="%.5f")
        ddp = st.number_input("Jitter:DDP", value=float(st.session_state.get('park_ddp', 0.0099)), format="%.5f")
        rpde = st.number_input("RPDE - Recurrence Entropy", value=float(st.session_state.get('park_rpde', 0.4985)), format="%.4f")
        dfa = st.number_input("DFA - Signal Fractal Scaling", value=float(st.session_state.get('park_dfa', 0.7180)), format="%.4f")
        
    with col3:
        st.markdown("**Shimmer & Non-linear Dysphonia**")
        shimmer = st.number_input("MDVP:Shimmer", value=float(st.session_state.get('park_shimmer', 0.0297)), format="%.4f")
        shimmer_db = st.number_input("MDVP:Shimmer (dB)", value=float(st.session_state.get('park_shimmerDb', 0.282)), format="%.3f")
        apq3 = st.number_input("Shimmer:APQ3", value=float(st.session_state.get('park_apq3', 0.0156)), format="%.4f")
        apq5 = st.number_input("Shimmer:APQ5", value=float(st.session_state.get('park_apq5', 0.0178)), format="%.4f")
        apq = st.number_input("MDVP:APQ", value=float(st.session_state.get('park_apq', 0.0240)), format="%.4f")
        dda = st.number_input("Shimmer:DDA", value=float(st.session_state.get('park_dda', 0.0469)), format="%.4f")
        spread1 = st.number_input("spread1 - Nonlinear Freq Spread", value=float(st.session_state.get('park_spread1', -5.684)), format="%.3f")
        spread2 = st.number_input("spread2 - Nonlinear Freq Spread", value=float(st.session_state.get('park_spread2', 0.2265)), format="%.4f")
        d2 = st.number_input("D2 - Correlation Dimension", value=float(st.session_state.get('park_d2', 2.381)), format="%.3f")
        ppe = st.number_input("PPE - Pitch Period Entropy", value=float(st.session_state.get('park_ppe', 0.2065)), format="%.4f")

    if st.button("🔍 Execute Parkinson's Acoustic Assessment"):
        data = {
            'fo': fo, 'fhi': fhi, 'flo': flo, 'jitterPercent': jitter_percent, 'jitterAbs': jitter_abs,
            'rap': rap, 'ppq': ppq, 'ddp': ddp, 'shimmer': shimmer, 'shimmerDb': shimmer_db,
            'apq3': apq3, 'apq5': apq5, 'apq': apq, 'dda': dda, 'nhr': nhr, 'hnr': hnr,
            'rpde': rpde, 'dfa': dfa, 'spread1': spread1, 'spread2': spread2, 'd2': d2, 'ppe': ppe
        }
        res = model.predict(data)
        render_result_card(res, "Parkinson's Disease")
