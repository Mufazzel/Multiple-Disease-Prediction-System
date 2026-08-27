"""
Preset clinical test patient cases for Diabetes, Heart Disease, and Parkinson's Disease.
"""

DIABETES_PRESETS = [
    {
        "id": "diab-healthy",
        "name": "Sample A: Healthy Control (Low Risk)",
        "description": "Normal blood glucose (85 mg/dL), healthy BMI (22.6), normal blood pressure",
        "expectedOutcome": "The person is not diabetic",
        "data": {
            "pregnancies": 1,
            "glucose": 85.0,
            "bloodPressure": 66.0,
            "skinThickness": 29.0,
            "insulin": 0.0,
            "bmi": 22.6,
            "diabetesPedigree": 0.351,
            "age": 28
        }
    },
    {
        "id": "diab-high-risk",
        "name": "Sample B: High Risk Diabetic Patient",
        "description": "Elevated glucose (168 mg/dL), BMI 35.3, high pedigree function",
        "expectedOutcome": "The person is diabetic",
        "data": {
            "pregnancies": 6,
            "glucose": 168.0,
            "bloodPressure": 74.0,
            "skinThickness": 32.0,
            "insulin": 175.0,
            "bmi": 35.3,
            "diabetesPedigree": 0.852,
            "age": 52
        }
    },
    {
        "id": "diab-borderline",
        "name": "Sample C: Borderline Prediabetic",
        "description": "Impaired fasting glucose (125 mg/dL), overweight BMI (28.4)",
        "expectedOutcome": "Borderline profile",
        "data": {
            "pregnancies": 2,
            "glucose": 125.0,
            "bloodPressure": 70.0,
            "skinThickness": 25.0,
            "insulin": 90.0,
            "bmi": 28.4,
            "diabetesPedigree": 0.467,
            "age": 38
        }
    }
]

HEART_PRESETS = [
    {
        "id": "heart-healthy",
        "name": "Sample A: Healthy Control (No Disease)",
        "description": "52-year-old active individual with normal BP, cholesterol 195 mg/dL, no angina",
        "expectedOutcome": "The person does not have any heart disease",
        "data": {
            "age": 52,
            "sex": 1,
            "cp": 0,
            "trestbps": 125,
            "chol": 195,
            "fbs": 0,
            "restecg": 1,
            "thalach": 168,
            "exang": 0,
            "oldpeak": 0.2,
            "slope": 2,
            "ca": 0,
            "thal": 2
        }
    },
    {
        "id": "heart-high-risk",
        "name": "Sample B: High Risk Coronary Heart Disease",
        "description": "64-year-old with exercise angina, ST depression 2.6, 2 major vessels colored",
        "expectedOutcome": "The person is having heart disease",
        "data": {
            "age": 64,
            "sex": 1,
            "cp": 2,
            "trestbps": 155,
            "chol": 288,
            "fbs": 1,
            "restecg": 0,
            "thalach": 122,
            "exang": 1,
            "oldpeak": 2.6,
            "slope": 1,
            "ca": 2,
            "thal": 1
        }
    }
]

PARKINSONS_PRESETS = [
    {
        "id": "park-healthy",
        "name": "Sample A: Healthy Vocal Control",
        "description": "Normal fundamental frequency (197 Hz), low jitter (0.0028), high HNR (26.2 dB)",
        "expectedOutcome": "The person does not have Parkinson's disease",
        "data": {
            "fo": 197.076,
            "fhi": 206.896,
            "flo": 192.055,
            "jitterPercent": 0.00289,
            "jitterAbs": 0.000015,
            "rap": 0.00166,
            "ppq": 0.00168,
            "ddp": 0.00498,
            "shimmer": 0.01098,
            "shimmerDb": 0.097,
            "apq3": 0.00563,
            "apq5": 0.00680,
            "apq": 0.00802,
            "dda": 0.01689,
            "nhr": 0.00339,
            "hnr": 26.775,
            "rpde": 0.422229,
            "dfa": 0.741367,
            "spread1": -7.348300,
            "spread2": 0.177551,
            "d2": 1.743867,
            "ppe": 0.085569
        }
    },
    {
        "id": "park-positive",
        "name": "Sample B: Parkinson's Dysphonia Patient",
        "description": "Severe vocal micro-tremor, elevated shimmer (0.04), reduced HNR (19.1 dB)",
        "expectedOutcome": "The person has Parkinson's disease",
        "data": {
            "fo": 119.992,
            "fhi": 157.302,
            "flo": 74.997,
            "jitterPercent": 0.00784,
            "jitterAbs": 0.000065,
            "rap": 0.00370,
            "ppq": 0.00554,
            "ddp": 0.01109,
            "shimmer": 0.04374,
            "shimmerDb": 0.426,
            "apq3": 0.02182,
            "apq5": 0.03130,
            "apq": 0.02971,
            "dda": 0.06545,
            "nhr": 0.02211,
            "hnr": 21.033,
            "rpde": 0.414783,
            "dfa": 0.815285,
            "spread1": -4.813031,
            "spread2": 0.266482,
            "d2": 2.301442,
            "ppe": 0.284654
        }
    }
]
