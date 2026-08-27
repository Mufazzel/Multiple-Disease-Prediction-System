"""
Header UI component for Streamlit Disease Prediction System.
"""
import streamlit as st

def render_header():
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.75rem 1.25rem; background-color: #ffffff; border-bottom: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 1.5rem; box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);">
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <div style="display: flex; width: 36px; height: 36px; align-items: center; justify-content: center; border-radius: 8px; background-color: #0284c7; color: #ffffff; font-size: 1.2rem;">
                    🩺
                </div>
                <div>
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <span style="font-weight: 700; color: #0f172a; font-size: 1.1rem; letter-spacing: -0.025em;">
                            Multiple Disease Prediction System
                        </span>
                        <span style="display: inline-flex; align-items: center; gap: 0.35rem; border-radius: 9999px; background-color: #eff6ff; padding: 0.125rem 0.625rem; font-size: 0.75rem; font-weight: 600; color: #1d4ed8; border: 1px solid #dbeafe;">
                            ML Diagnostics Suite
                        </span>
                    </div>
                    <p style="margin: 0; font-size: 0.75rem; color: #94a3b8; font-weight: 500;">
                        Multiple Disease Prediction Engine • Python & Scikit-Learn Architecture
                    </p>
                </div>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem; background-color: #f1f5f9; padding: 0.35rem 0.75rem; border-radius: 8px; font-family: monospace; font-size: 0.75rem; color: #334155;">
                <span>🐍 Python 3.10 • Streamlit</span>
            </div>
        </div>
    """, unsafe_allow_html=True)
