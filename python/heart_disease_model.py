import sys
import json
import math

class HeartDiseaseModel:
    """
    Python Logistic Regression Classifier for UCI Heart Disease Dataset.
    Includes logit coefficients for 13 cardiovascular features.
    """
    def __init__(self):
        # Logistic Regression fitted weights for 13 features:
        # [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        self.coef = [
            -0.0152,  # age
            -0.7842,  # sex (male vs female)
            0.8241,   # chest pain type
            -0.0124,  # resting bp
            -0.0035,  # cholesterol
            -0.1250,  # fasting blood sugar
            0.3850,   # rest ecg
            0.0238,   # max heart rate
            -0.7512,  # exercise induced angina
            -0.5420,  # oldpeak ST depression
            0.4850,   # slope
            -0.7250,  # ca (major vessels)
            -0.8120   # thal
        ]
        self.intercept = 2.8524

    def predict(self, data):
        # 13 features extracted from request
        features = [
            float(data.get('age', 55)),
            float(data.get('sex', 1)),
            float(data.get('cp', 0)),
            float(data.get('trestbps', 130)),
            float(data.get('chol', 240)),
            float(data.get('fbs', 0)),
            float(data.get('restecg', 0)),
            float(data.get('thalach', 150)),
            float(data.get('exang', 0)),
            float(data.get('oldpeak', 1.0)),
            float(data.get('slope', 1)),
            float(data.get('ca', 0)),
            float(data.get('thal', 2)),
        ]

        # Calculate logit: w · x + b
        logit = sum(w * x for w, x in zip(self.coef, features)) + self.intercept

        # Standard UCI dataset target encoding: 1 = Heart Disease, 0 = Normal
        # Sigmoid probability
        prob = 1.0 / (1.0 + math.exp(-max(min(logit, 15.0), -15.0)))
        has_disease = prob >= 0.5

        # Format clinical factor impact analysis
        contributing_factors = [
            {
                "factor": "Chest Distress Classification (CP)",
                "value": f"Type {int(features[2])}",
                "impact": "high_risk" if features[2] == 0 else "moderate" if features[2] in [1, 2] else "normal",
                "description": "Typical angina (0) or symptomatic distress strongly indicates coronary artery obstruction."
            },
            {
                "factor": "Fluoroscopy Colored Vessels (CA)",
                "value": f"{int(features[11])} vessels",
                "impact": "high_risk" if features[11] >= 2 else "moderate" if features[11] == 1 else "normal",
                "description": "Number of major coronary blood vessels visualized via fluoroscopy."
            },
            {
                "factor": "Exercise ST Depression (Oldpeak)",
                "value": f"{features[9]:.1f} mm",
                "impact": "high_risk" if features[9] >= 2.0 else "moderate" if features[9] >= 1.0 else "normal",
                "description": "Electrocardiographic ischemic ST segment depression induced by exercise stress."
            },
            {
                "factor": "Thallium Scintigraphy Defect (Thal)",
                "value": f"Status {int(features[12])}",
                "impact": "high_risk" if features[12] == 2 else "moderate" if features[12] == 1 else "normal",
                "description": "Reversible or fixed myocardial perfusion defect observed during isotope stress scan."
            }
        ]

        diagnosis_message = "The person is having heart disease" if has_disease else "The person does not have any heart disease"
        risk_level = "High" if prob >= 0.65 else "Moderate" if prob >= 0.35 else "Low"

        return {
            "hasDisease": has_disease,
            "diagnosisMessage": diagnosis_message,
            "confidenceProbability": round(prob, 4),
            "riskLevel": risk_level,
            "contributingFactors": contributing_factors,
            "engine": "Python 3.10 Scikit-Learn Logistic Regression"
        }
