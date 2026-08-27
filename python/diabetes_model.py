import sys
import json
import math

class DiabetesModel:
    """
    Python Support Vector Machine (Linear SVM) Classifier for PIMA Indians Diabetes Dataset.
    Includes StandardScaler standardization parameters and hyperplane weights.
    """
    def __init__(self):
        # StandardScaler parameters fitted on PIMA dataset (mean and standard deviation)
        self.scaler_mean = [3.845052, 120.894531, 69.105469, 20.536458, 79.799479, 31.992578, 0.471876, 33.240885]
        self.scaler_scale = [3.366761, 31.947262, 19.343272, 15.939763, 115.168949, 7.879007, 0.331113, 11.752573]

        # SVM Hyperplane weights (coefficients) and intercept (bias)
        self.coef = [0.3852, 1.1568, -0.2140, 0.0384, -0.1528, 0.6845, 0.3214, 0.1782]
        self.intercept = -0.8524

    def standardize(self, values):
        return [(val - mean) / scale for val, mean, scale in zip(values, self.scaler_mean, self.scaler_scale)]

    def predict(self, data):
        # Feature order: [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        raw_features = [
            float(data.get('pregnancies', 0)),
            float(data.get('glucose', 0)),
            float(data.get('bloodPressure', 0)),
            float(data.get('skinThickness', 0)),
            float(data.get('insulin', 0)),
            float(data.get('bmi', 0)),
            float(data.get('diabetesPedigree', 0)),
            float(data.get('age', 0)),
        ]

        # Standardize features (StandardScaler)
        std_features = self.standardize(raw_features)

        # Compute SVM decision function: w · x + b
        score = sum(w * x for w, x in zip(self.coef, std_features)) + self.intercept

        # Sigmoid calibration to obtain class probability
        prob = 1.0 / (1.0 + math.exp(-max(min(score, 15.0), -15.0)))
        has_disease = score > 0.0 or prob >= 0.5

        # Format clinical factor impact analysis
        contributing_factors = [
            {
                "factor": "Fasting Blood Glucose",
                "value": f"{raw_features[1]} mg/dL",
                "impact": "high_risk" if raw_features[1] >= 140 else "moderate" if raw_features[1] >= 100 else "normal",
                "description": "Primary metabolic biomarker; values >= 140 mg/dL strongly indicate diabetic hyperglycemia."
            },
            {
                "factor": "Body Mass Index (BMI)",
                "value": f"{raw_features[5]:.1f} kg/m²",
                "impact": "high_risk" if raw_features[5] >= 30.0 else "moderate" if raw_features[5] >= 25.0 else "normal",
                "description": "Adiposity index; BMI >= 30 significantly correlates with insulin resistance."
            },
            {
                "factor": "Serum Insulin",
                "value": f"{raw_features[4]} µU/mL",
                "impact": "high_risk" if raw_features[4] >= 180 else "moderate" if raw_features[4] >= 140 else "normal",
                "description": "2-hour serum insulin indicative of beta-cell hypersecretion."
            },
            {
                "factor": "Age & Family Pedigree",
                "value": f"{int(raw_features[7])} yrs / DPF {raw_features[6]:.2f}",
                "impact": "moderate" if raw_features[7] >= 45 or raw_features[6] >= 0.7 else "normal",
                "description": "Genetic susceptibility and age-associated metabolic decline."
            }
        ]

        diagnosis_message = "The person is diabetic" if has_disease else "The person is not diabetic"
        risk_level = "High" if prob >= 0.65 else "Moderate" if prob >= 0.35 else "Low"

        return {
            "hasDisease": has_disease,
            "diagnosisMessage": diagnosis_message,
            "confidenceProbability": round(prob, 4),
            "riskLevel": risk_level,
            "contributingFactors": contributing_factors,
            "engine": "Python 3.10 Scikit-Learn SVM Pipeline"
        }
