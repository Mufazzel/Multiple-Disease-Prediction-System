# Multiple Disease Prediction System

A Machine Learning clinical prediction platform that performs real-time diagnostic risk assessments for **Diabetes**, **Heart Disease**, and **Parkinson's Disease**.

Repository: [https://github.com/Mufazzel/Multiple-Disease-Prediction-System](https://github.com/Mufazzel/Multiple-Disease-Prediction-System)

---

## 📌 Overview

This project provides an accessible diagnostic platform capable of evaluating patient parameters across three major diseases:

1. **Diabetes Prediction**: Uses an **SVM (Support Vector Machine) Linear Classifier** trained on the PIMA Indians Diabetes Dataset.
2. **Heart Disease Prediction**: Uses a **Logistic Regression Classifier** trained on the UCI Cleveland Cardiovascular Disease Dataset.
3. **Parkinson's Disease Prediction**: Uses an **SVM with Radial Basis Function (RBF) Kernel** trained on Oxford Vocal Dysphonia Biomedical Measurements.

---

## 🚀 Key Features

- **Streamlit Option Menu Navigation**: Integrated sidebar navigation (`streamlit_option_menu`) with distinct medical icons (`activity`, `heart`, `person`).
- **Saved Serialized Models**: Machine learning models serialized into `.sav` format using Python's `pickle` library in the `saved_models/` directory.
- **3-Column & 5-Column Responsive Input Grids**: Intuitive medical parameter input layout.
- **Real-time Diagnostic Feedback**: Instant test evaluation with positive/negative diagnosis notifications and probability scores.

---

## 🧠 Machine Learning Models & Datasets

| Condition | Algorithm | Dataset | Key Input Features | 
| :--- | :--- | :--- | :--- | :--- |
| **Diabetes** | Support Vector Machine (Linear Kernel) | PIMA Indians Diabetes Dataset | Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, DPF, Age | 
| **Heart Disease** | Logistic Regression | UCI Cleveland Heart Disease Dataset | Age, Sex, Chest Pain (CP), Resting BP, Cholesterol, FBS, Resting ECG, Max HR, Exercise Angina, ST Depression, Slope, Major Vessels (CA), Thalassemia |
| **Parkinson's Disease** | Support Vector Machine (RBF Kernel) | Oxford Parkinson's Vocal Dysphonia Dataset | MDVP (Fo, Fhi, Flo, Jitter, Shimmer), NHR, HNR, RPDE, DFA, Spread1/2, D2, PPE (22 features) |

---

## 🐍 Setup & Installation

### 1. Clone the repository:
```bash
git clone https://github.com/Mufazzel/Multiple-Disease-Prediction-System.git
cd Multiple-Disease-Prediction-System
```

### 2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Web Application:
```bash
streamlit run app.py
```
*(or `streamlit run multiple_disease_prediction.py`)*

### 4. Open in browser:
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 📂 Project Structure

```text
├── saved_models/
│   ├── diabetes_model.sav           # Serialized Diabetes SVM Model
│   ├── heart_disease_model.sav      # Serialized Heart Disease Logistic Regression Model
│   └── parkinsons_model.sav         # Serialized Parkinson's SVM Model
├── python/
│   ├── diabetes_model.py            # Diabetes model logic & weights
│   ├── heart_disease_model.py       # Heart disease model logic & weights
│   ├── parkinsons_model.py          # Parkinson's model logic & weights
│   ├── train_all_models.py          # Scikit-Learn training script
│   └── predict.py                   # Python CLI prediction dispatcher
├── app.py                           # Main Streamlit Web Application
├── multiple_disease_prediction.py   # Streamlit Application Script
├── requirements.txt                 # Python dependencies
├── .gitattributes                   # GitHub language stats (100% Python)
└── README.md                        # Documentation
```

---

## ⚠️ Disclaimer

This application is developed for **educational and research purposes only**. It is not intended to be a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of a qualified healthcare provider with any questions you may have regarding a medical condition.
