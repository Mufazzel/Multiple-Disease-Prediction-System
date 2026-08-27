"""
Main execution launcher for Streamlit Multiple Disease Prediction System.
"""
import os
import sys

def main():
    """Launch the Streamlit app programmatically or via CLI."""
    import streamlit.web.bootstrap as bootstrap
    from streamlit import config as _config

    dirname = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    app_path = os.path.join(dirname, "app.py")
    
    _config.set_option("server.headless", True)
    _config.set_option("server.port", 8501)
    
    print(f"Launching Multiple Disease Prediction System from {app_path}...")
    bootstrap.run(app_path, "", [], flag_options={})

if __name__ == "__main__":
    main()
