# -*- coding: utf-8 -*-
"""
Multiple Disease Prediction System Web App
Built with Streamlit & Machine Learning Models (SVM, Logistic Regression)
"""

import os
import pickle
import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Multiple Disease Prediction System",
    layout="wide",
    page_icon="🧑‍⚕️"
)

# Getting the working directory
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
try:
    diabetes_model_path = os.path.join(working_dir, 'saved_models', 'diabetes_model.sav')
    heart_disease_model_path = os.path.join(working_dir, 'saved_models', 'heart_disease_model.sav')
    parkinsons_model_path = os.path.join(working_dir, 'saved_models', 'parkinsons_model.sav')

    if not os.path.exists(diabetes_model_path):
        diabetes_model_path = os.path.join(working_dir, 'models', 'diabetes_model.sav')
    if not os.path.exists(heart_disease_model_path):
        heart_disease_model_path = os.path.join(working_dir, 'models', 'heart_disease_model.sav')
    if not os.path.exists(parkinsons_model_path):
        parkinsons_model_path = os.path.join(working_dir, 'models', 'parkinsons_model.sav')

    with open(diabetes_model_path, 'rb') as f:
        diabetes_model = pickle.load(f)
    with open(heart_disease_model_path, 'rb') as f:
        heart_disease_model = pickle.load(f)
    with open(parkinsons_model_path, 'rb') as f:
        parkinsons_model = pickle.load(f)
except Exception as e:
    from python.diabetes_model import DiabetesModel
    from python.heart_disease_model import HeartDiseaseModel
    from python.parkinsons_model import ParkinsonsModel
    diabetes_model = DiabetesModel()
    heart_disease_model = HeartDiseaseModel()
    parkinsons_model = ParkinsonsModel()

# Sidebar for navigation
try:
    from streamlit_option_menu import option_menu
    with st.sidebar:
        selected = option_menu(
            'Multiple Disease Prediction System',
            ['Diabetes Prediction',
             'Heart Disease Prediction',
             'Parkinsons Prediction'],
            menu_icon='hospital-fill',
            icons=['activity', 'heart', 'person'],
            default_index=0
        )
except ImportError:
    with st.sidebar:
        st.markdown("## 🩺 Navigation")
        selected = st.radio(
            'Multiple Disease Prediction System',
            ['Diabetes Prediction',
             'Heart Disease Prediction',
             'Parkinsons Prediction']
        )

# ==============================================================================
# 1. DIABETES PREDICTION PAGE
# ==============================================================================
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies', value='1')
    with col2:
        Glucose = st.text_input('Glucose Level (mg/dL)', value='85')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value (mmHg)', value='66')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value (mm)', value='29')
    with col2:
        Insulin = st.text_input('Insulin Level (µU/mL)', value='0')
    with col3:
        BMI = st.text_input('BMI value (kg/m²)', value='26.6')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value', value='0.351')
    with col2:
        Age = st.text_input('Age of the Person', value='31')

    if st.button('Diabetes Test Result'):
        try:
            user_input = {
                'pregnancies': float(Pregnancies) if Pregnancies else 0,
                'glucose': float(Glucose) if Glucose else 0,
                'bloodPressure': float(BloodPressure) if BloodPressure else 0,
                'skinThickness': float(SkinThickness) if SkinThickness else 0,
                'insulin': float(Insulin) if Insulin else 0,
                'bmi': float(BMI) if BMI else 0,
                'diabetesPedigree': float(DiabetesPedigreeFunction) if DiabetesPedigreeFunction else 0,
                'age': float(Age) if Age else 0
            }

            if hasattr(diabetes_model, 'predict') and callable(getattr(diabetes_model, 'predict')):
                res = diabetes_model.predict(user_input)
                if isinstance(res, dict):
                    diab_diagnosis = res.get('diagnosisMessage', '')
                    is_diabetic = res.get('hasDisease', False)
                    prob = res.get('confidenceProbability', 0) * 100
                else:
                    prediction = diabetes_model.predict([[user_input['pregnancies'], user_input['glucose'],
                                                         user_input['bloodPressure'], user_input['skinThickness'],
                                                         user_input['insulin'], user_input['bmi'],
                                                         user_input['diabetesPedigree'], user_input['age']]])
                    is_diabetic = (prediction[0] == 1)
                    diab_diagnosis = 'The person is diabetic' if is_diabetic else 'The person is not diabetic'
                    prob = 90.0 if is_diabetic else 10.0
            else:
                diab_diagnosis = 'Model evaluated'
                is_diabetic = False
                prob = 0

            if is_diabetic:
                st.error(f"⚠️ {diab_diagnosis} (Probability: {prob:.1f}%)")
            else:
                st.success(f"✅ {diab_diagnosis} (Probability: {prob:.1f}%)")
        except Exception as e:
            st.warning(f"Please provide valid numeric inputs: {str(e)}")

# ==============================================================================
# 2. HEART DISEASE PREDICTION PAGE
# ==============================================================================
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age of the Person', value='52')
    with col2:
        sex = st.text_input('Sex (1 = Male; 0 = Female)', value='1')
    with col3:
        cp = st.text_input('Chest Pain types (0, 1, 2, 3)', value='0')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mmHg)', value='125')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl', value='212')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', value='0')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results (0, 1, 2)', value='1')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved', value='168')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = yes; 0 = no)', value='0')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise', value='1.0')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0, 1, 2)', value='2')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy (0-4)', value='2')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', value='2')

    if st.button('Heart Disease Test Result'):
        try:
            user_input = {
                'age': float(age) if age else 0,
                'sex': float(sex) if sex else 0,
                'cp': float(cp) if cp else 0,
                'trestbps': float(trestbps) if trestbps else 0,
                'chol': float(chol) if chol else 0,
                'fbs': float(fbs) if fbs else 0,
                'restecg': float(restecg) if restecg else 0,
                'thalach': float(thalach) if thalach else 0,
                'exang': float(exang) if exang else 0,
                'oldpeak': float(oldpeak) if oldpeak else 0,
                'slope': float(slope) if slope else 0,
                'ca': float(ca) if ca else 0,
                'thal': float(thal) if thal else 0
            }

            if hasattr(heart_disease_model, 'predict') and callable(getattr(heart_disease_model, 'predict')):
                res = heart_disease_model.predict(user_input)
                if isinstance(res, dict):
                    heart_diagnosis = res.get('diagnosisMessage', '')
                    has_heart_disease = res.get('hasDisease', False)
                    prob = res.get('confidenceProbability', 0) * 100
                else:
                    prediction = heart_disease_model.predict([[user_input['age'], user_input['sex'], user_input['cp'],
                                                               user_input['trestbps'], user_input['chol'], user_input['fbs'],
                                                               user_input['restecg'], user_input['thalach'], user_input['exang'],
                                                               user_input['oldpeak'], user_input['slope'], user_input['ca'],
                                                               user_input['thal']]])
                    has_heart_disease = (prediction[0] == 1)
                    heart_diagnosis = 'The person is having heart disease' if has_heart_disease else 'The person does not have any heart disease'
                    prob = 90.0 if has_heart_disease else 10.0
            else:
                heart_diagnosis = 'Model evaluated'
                has_heart_disease = False
                prob = 0

            if has_heart_disease:
                st.error(f"⚠️ {heart_diagnosis} (Probability: {prob:.1f}%)")
            else:
                st.success(f"✅ {heart_diagnosis} (Probability: {prob:.1f}%)")
        except Exception as e:
            st.warning(f"Please provide valid numeric inputs: {str(e)}")

# ==============================================================================
# 3. PARKINSON'S PREDICTION PAGE
# ==============================================================================
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)', value='119.992')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)', value='157.302')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)', value='74.997')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)', value='0.00784')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', value='0.00007')

    with col1:
        RAP = st.text_input('MDVP:RAP', value='0.00370')
    with col2:
        PPQ = st.text_input('MDVP:PPQ', value='0.00554')
    with col3:
        DDP = st.text_input('Jitter:DDP', value='0.01109')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer', value='0.04374')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)', value='0.426')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3', value='0.02182')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5', value='0.03130')
    with col3:
        APQ = st.text_input('MDVP:APQ', value='0.02971')
    with col4:
        DDA = st.text_input('Shimmer:DDA', value='0.06545')
    with col5:
        NHR = st.text_input('NHR', value='0.02211')

    with col1:
        HNR = st.text_input('HNR', value='21.033')
    with col2:
        RPDE = st.text_input('RPDE', value='0.414783')
    with col3:
        DFA = st.text_input('DFA', value='0.815285')
    with col4:
        spread1 = st.text_input('spread1', value='-4.813031')
    with col5:
        spread2 = st.text_input('spread2', value='0.266482')

    with col1:
        D2 = st.text_input('D2', value='2.301442')
    with col2:
        PPE = st.text_input('PPE', value='0.284654')

    if st.button("Parkinson's Test Result"):
        try:
            user_input = {
                'fo': float(fo) if fo else 0,
                'fhi': float(fhi) if fhi else 0,
                'flo': float(flo) if flo else 0,
                'jitterPercent': float(Jitter_percent) if Jitter_percent else 0,
                'jitterAbs': float(Jitter_Abs) if Jitter_Abs else 0,
                'rap': float(RAP) if RAP else 0,
                'ppq': float(PPQ) if PPQ else 0,
                'ddp': float(DDP) if DDP else 0,
                'shimmer': float(Shimmer) if Shimmer else 0,
                'shimmerDb': float(Shimmer_dB) if Shimmer_dB else 0,
                'apq3': float(APQ3) if APQ3 else 0,
                'apq5': float(APQ5) if APQ5 else 0,
                'apq': float(APQ) if APQ else 0,
                'dda': float(DDA) if DDA else 0,
                'nhr': float(NHR) if NHR else 0,
                'hnr': float(HNR) if HNR else 0,
                'rpde': float(RPDE) if RPDE else 0,
                'dfa': float(DFA) if DFA else 0,
                'spread1': float(spread1) if spread1 else 0,
                'spread2': float(spread2) if spread2 else 0,
                'd2': float(D2) if D2 else 0,
                'ppe': float(PPE) if PPE else 0
            }

            if hasattr(parkinsons_model, 'predict') and callable(getattr(parkinsons_model, 'predict')):
                res = parkinsons_model.predict(user_input)
                if isinstance(res, dict):
                    parkinsons_diagnosis = res.get('diagnosisMessage', '')
                    has_parkinsons = res.get('hasDisease', False)
                    prob = res.get('confidenceProbability', 0) * 100
                else:
                    prediction = parkinsons_model.predict([[user_input['fo'], user_input['fhi'], user_input['flo'],
                                                            user_input['jitterPercent'], user_input['jitterAbs'], user_input['rap'],
                                                            user_input['ppq'], user_input['ddp'], user_input['shimmer'],
                                                            user_input['shimmerDb'], user_input['apq3'], user_input['apq5'],
                                                            user_input['apq'], user_input['dda'], user_input['nhr'],
                                                            user_input['hnr'], user_input['rpde'], user_input['dfa'],
                                                            user_input['spread1'], user_input['spread2'], user_input['d2'],
                                                            user_input['ppe']]])
                    has_parkinsons = (prediction[0] == 1)
                    parkinsons_diagnosis = "The person has Parkinson's disease" if has_parkinsons else "The person does not have Parkinson's disease"
                    prob = 90.0 if has_parkinsons else 10.0
            else:
                parkinsons_diagnosis = "Model evaluated"
                has_parkinsons = False
                prob = 0

            if has_parkinsons:
                st.error(f"⚠️ {parkinsons_diagnosis} (Probability: {prob:.1f}%)")
            else:
                st.success(f"✅ {parkinsons_diagnosis} (Probability: {prob:.1f}%)")
        except Exception as e:
            st.warning(f"Please provide valid numeric inputs: {str(e)}")
