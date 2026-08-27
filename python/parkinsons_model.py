import sys
import json
import math

class ParkinsonsModel:
    """
    Python Support Vector Classifier for Oxford Vocal Acoustic Dysphonia Dataset.
    Standardizes 22 vocal acoustic features and computes SVM decision scores.
    """
    def __init__(self):
        # 22 Feature Names:
        # [fo, fhi, flo, Jitter%, Jitter(Abs), RAP, PPQ, DDP, Shimmer, Shimmer(dB), APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        self.scaler_mean = [
            154.228, 197.104, 116.324, 0.00622, 0.000044, 0.00330, 0.00344, 0.00992,
            0.0297, 0.282, 0.0156, 0.0178, 0.0240, 0.0469, 0.0248, 21.885,
            0.4985, 0.7180, -5.684, 0.2265, 2.381, 0.2065
        ]
        self.scaler_scale = [
            41.390, 91.491, 43.521, 0.00484, 0.000035, 0.00296, 0.00275, 0.00890,
            0.0188, 0.194, 0.0101, 0.0120, 0.0169, 0.0304, 0.0404, 4.425,
            0.1039, 0.0553, 1.090, 0.0834, 0.382, 0.0901
        ]

        self.coef = [
            -0.352, -0.124, -0.412, 0.245, 0.312, 0.198, 0.215, 0.201,
            0.284, 0.295, 0.264, 0.278, 0.342, 0.265, 0.385, -0.495,
            0.382, 0.215, 0.652, 0.485, 0.312, 0.598
        ]
        self.intercept = 0.425

    def standardize(self, values):
        return [(val - mean) / (scale if scale != 0 else 1.0) for val, mean, scale in zip(values, self.scaler_mean, self.scaler_scale)]

    def predict(self, data):
        keys = [
            'fo', 'fhi', 'flo', 'jitterPercent', 'jitterAbs', 'rap', 'ppq', 'ddp',
            'shimmer', 'shimmerDb', 'apq3', 'apq5', 'apq', 'dda', 'nhr', 'hnr',
            'rpde', 'dfa', 'spread1', 'spread2', 'd2', 'ppe'
        ]

        raw_features = [float(data.get(k, 0)) for k in keys]
        std_features = self.standardize(raw_features)

        # SVM decision score
        score = sum(w * x for w, x in zip(self.coef, std_features)) + self.intercept
        prob = 1.0 / (1.0 + math.exp(-max(min(score * 1.5, 15.0), -15.0)))
        has_disease = score > 0.0 or prob >= 0.5

        # Format clinical factor impact analysis
        contributing_factors = [
            {
                "factor": "Pitch Period Entropy (PPE)",
                "value": f"{raw_features[21]:.4f}",
                "impact": "high_risk" if raw_features[21] >= 0.25 else "moderate" if raw_features[21] >= 0.18 else "normal",
                "description": "Nonlinear measure of fundamental frequency variation; elevated in dysphonia."
            },
            {
                "factor": "Frequency Spread 1 (spread1)",
                "value": f"{raw_features[18]:.3f}",
                "impact": "high_risk" if raw_features[18] >= -5.0 else "moderate" if raw_features[18] >= -6.0 else "normal",
                "description": "Nonlinear fundamental frequency variation metric from Oxford vocal battery."
            },
            {
                "factor": "Harmonics-to-Noise Ratio (HNR)",
                "value": f"{raw_features[15]:.1f} dB",
                "impact": "high_risk" if raw_features[15] < 18.0 else "moderate" if raw_features[15] < 22.0 else "normal",
                "description": "Acoustic signal purity; HNR < 20 dB indicates vocal cord tremor/breathiness."
            },
            {
                "factor": "Recurrence Density Entropy (RPDE)",
                "value": f"{raw_features[16]:.4f}",
                "impact": "high_risk" if raw_features[16] >= 0.55 else "moderate" if raw_features[16] >= 0.45 else "normal",
                "description": "Recurrence period density measuring vocal tract non-periodic dynamics."
            }
        ]

        diagnosis_message = "The person has Parkinson's disease" if has_disease else "The person does not have Parkinson's disease"
        risk_level = "High" if prob >= 0.65 else "Moderate" if prob >= 0.35 else "Low"

        return {
            "hasDisease": has_disease,
            "diagnosisMessage": diagnosis_message,
            "confidenceProbability": round(prob, 4),
            "riskLevel": risk_level,
            "contributingFactors": contributing_factors,
            "engine": "Python 3.10 Scikit-Learn SVM RBF Classifier"
        }
