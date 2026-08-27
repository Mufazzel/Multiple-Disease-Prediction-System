"""
Streamlit and Python UI components for Multiple Disease Prediction System.
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

def render_result_card(res: dict, disease_name: str):
    prob_pct = res["confidenceProbability"] * 100
    if res["hasDisease"]:
        st.markdown(f"""
            <div class="result-card-positive">
                <h3 style="color:#b91c1c; margin:0 0 0.5rem 0;">⚠️ Diagnostic Outcome: Positive ({disease_name} Indicator)</h3>
                <p style="margin:0; font-size: 1.05rem; color:#450a0a;">
                    <strong>Calculated Probability:</strong> {prob_pct:.1f}% &nbsp;|&nbsp; 
                    <strong>Risk Tier:</strong> <span style="color:#dc2626; font-weight:bold;">{res['riskLevel']} Risk</span>
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="result-card-negative">
                <h3 style="color:#15803d; margin:0 0 0.5rem 0;">✅ Diagnostic Outcome: Negative (Healthy / Low Risk)</h3>
                <p style="margin:0; font-size: 1.05rem; color:#052e16;">
                    <strong>Calculated Probability:</strong> {prob_pct:.1f}% &nbsp;|&nbsp; 
                    <strong>Risk Tier:</strong> <span style="color:#16a34a; font-weight:bold;">{res['riskLevel']} Risk</span>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("#### 📊 Clinical Contributing Biomarkers")
    for factor in res.get("contributingFactors", []):
        badge_class = "factor-badge-high" if factor["impact"] == "high_risk" else "factor-badge-normal"
        st.markdown(f"- **{factor['factor']}** ({factor['value']}): <span class='{badge_class}'>{factor['impact'].replace('_', ' ').upper()}</span> — {factor['description']}", unsafe_allow_html=True)
