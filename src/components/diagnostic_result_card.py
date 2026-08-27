"""
Diagnostic Result Card component displaying ML outcomes, confidence metrics, and clinical biomarkers.
"""
import streamlit as st
from typing import Dict, Any

def render_diagnostic_result_card(result: Dict[str, Any], disease_name: str):
    is_positive = result.get("hasDisease", False)
    prob_pct = result.get("confidenceProbability", 0.0) * 100
    risk_level = result.get("riskLevel", "Low")
    msg = result.get("diagnosisMessage", "")
    engine = result.get("engine", "Python 3.10 Scikit-Learn SVM Pipeline")
    factors = result.get("contributingFactors", [])

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if is_positive:
            st.markdown(f"""
                <div style="background-color: #fef2f2; border: 1px solid #fecaca; border-radius: 16px; padding: 1.5rem; height: 100%;">
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: #dc2626; letter-spacing: 0.05em;">Diagnostic Outcome</span>
                        <span style="background-color: #fee2e2; color: #991b1b; padding: 0.15rem 0.5rem; border-radius: 6px; font-size: 0.75rem; font-weight: 700;">
                            {risk_level} Risk
                        </span>
                    </div>
                    <h3 style="color: #450a0a; font-size: 1.35rem; font-weight: 700; margin: 0 0 0.5rem 0;">
                        ⚠️ {msg}
                    </h3>
                    <p style="color: #991b1b; font-size: 0.875rem; margin: 0; line-height: 1.5;">
                        Diagnostic markers indicate elevation above normal reference ranges. Clinical consultation and confirmatory testing recommended for {disease_name}.
                    </p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div style="background-color: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 16px; padding: 1.5rem; height: 100%;">
                    <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                        <span style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; color: #16a34a; letter-spacing: 0.05em;">Diagnostic Outcome</span>
                        <span style="background-color: #dcfce7; color: #166534; padding: 0.15rem 0.5rem; border-radius: 6px; font-size: 0.75rem; font-weight: 700;">
                            {risk_level} Risk
                        </span>
                    </div>
                    <h3 style="color: #052e16; font-size: 1.35rem; font-weight: 700; margin: 0 0 0.5rem 0;">
                        ✅ {msg}
                    </h3>
                    <p style="color: #166534; font-size: 0.875rem; margin: 0; line-height: 1.5;">
                        Biometric parameters align with healthy baseline reference criteria for {disease_name}.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div style="background-color: #0f172a; border-radius: 16px; padding: 1.5rem; color: #ffffff; height: 100%;">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                    <span style="color: #93c5fd; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em;">
                        Analytical Confidence
                    </span>
                    <span style="font-family: monospace; font-size: 0.75rem; color: #4ade80;">
                        ● ML Verified
                    </span>
                </div>
                <div style="display: flex; align-items: baseline; gap: 0.75rem;">
                    <span style="font-size: 2.25rem; font-weight: 900; font-family: monospace; color: #ffffff;">
                        {prob_pct:.1f}%
                    </span>
                    <span style="color: #60a5fa; font-size: 0.85rem; font-weight: 600;">
                        {'Disease Probability' if is_positive else 'Negative Likelihood Score'}
                    </span>
                </div>
                <div style="background-color: #1e293b; border-radius: 9999px; height: 10px; width: 100%; margin-top: 1rem; overflow: hidden;">
                    <div style="background-color: {'#ef4444' if is_positive else '#3b82f6'}; width: {max(prob_pct, 6)}%; height: 100%; border-radius: 9999px;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; font-size: 0.7rem; color: #94a3b8; font-family: monospace; margin-top: 0.5rem;">
                    <span>0% Low Risk</span>
                    <span>Decision Threshold: 50%</span>
                    <span>100% High Risk</span>
                </div>
                <div style="border-top: 1px solid #1e293b; margin-top: 1rem; padding-top: 0.75rem; font-size: 0.75rem; color: #64748b; display: flex; justify-content: space-between;">
                    <span>{engine}</span>
                    <span style="color: #4ade80;">Python Executed</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    if factors:
        st.markdown("#### 📊 Key Contributing Clinical Biomarkers")
        cols = st.columns(min(len(factors), 4))
        for idx, factor in enumerate(factors):
            col_idx = idx % min(len(factors), 4)
            with cols[col_idx]:
                impact = factor.get("impact", "normal")
                bg_col = "#fee2e2" if impact == "high_risk" else ("#fef3c7" if impact == "moderate" else "#dcfce7")
                txt_col = "#991b1b" if impact == "high_risk" else ("#92400e" if impact == "moderate" else "#166534")
                
                st.markdown(f"""
                    <div style="background-color: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 0.85rem; margin-bottom: 0.5rem; height: 100%;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 0.35rem;">
                            <span style="font-size: 0.8rem; font-weight: 700; color: #1e293b;">{factor['factor']}</span>
                            <span style="background-color: {bg_col}; color: {txt_col}; padding: 0.1rem 0.4rem; border-radius: 4px; font-size: 0.7rem; font-weight: 700; font-family: monospace;">
                                {factor['value']}
                            </span>
                        </div>
                        <p style="font-size: 0.75rem; color: #64748b; margin: 0; line-height: 1.4;">
                            {factor['description']}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
