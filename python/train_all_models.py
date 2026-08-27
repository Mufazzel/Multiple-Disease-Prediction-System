"""
Train and evaluate all 3 Machine Learning diagnostic models using Scikit-Learn.
Generates model evaluation reports and saves serialized models.
"""

import numpy as np
import pickle
import json
import os

try:
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.svm import SVC
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False


def train_diabetes_model():
    print("=" * 60)
    print("1. Training Diabetes Prediction Model (SVM Linear Classifier)")
    print("=" * 60)
    
    # Synthetic representative PIMA dataset distribution for standalone demonstration
    np.random.seed(42)
    n_samples = 768
    
    # Feature generation aligned with PIMA Indians distribution
    pregnancies = np.random.poisson(3.8, n_samples)
    glucose = np.random.normal(120.9, 31.9, n_samples).clip(44, 199)
    bp = np.random.normal(69.1, 19.3, n_samples).clip(24, 122)
    skin = np.random.normal(20.5, 15.9, n_samples).clip(0, 99)
    insulin = np.random.exponential(79.8, n_samples).clip(0, 846)
    bmi = np.random.normal(32.0, 7.8, n_samples).clip(18.2, 67.1)
    dpf = np.random.gamma(2.0, 0.23, n_samples).clip(0.078, 2.42)
    age = np.random.exponential(15, n_samples) + 21
    
    X = np.column_stack([pregnancies, glucose, bp, skin, insulin, bmi, dpf, age])
    
    # Ground truth logistic boundary
    z = -8.0 + 0.035 * glucose + 0.08 * bmi + 0.03 * age + 0.8 * dpf + 0.08 * pregnancies
    prob = 1 / (1 + np.exp(-z))
    y = (prob > 0.5).astype(int)
    
    if SKLEARN_AVAILABLE:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = SVC(kernel='linear', probability=True, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        preds = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, preds)
        print(f"-> Diabetes SVM Model Accuracy: {acc * 100:.2f}%")
        
        os.makedirs("models", exist_ok=True)
        with open("models/diabetes_model.sav", "wb") as f:
            pickle.dump({"model": model, "scaler": scaler}, f)
        print("-> Saved model to models/diabetes_model.sav\n")
    else:
        print("-> Scikit-Learn not installed in environment. Run 'pip install scikit-learn' to retrain.")


def train_heart_disease_model():
    print("=" * 60)
    print("2. Training Heart Disease Model (Logistic Regression)")
    print("=" * 60)
    
    np.random.seed(42)
    n_samples = 303
    
    age = np.random.normal(54.4, 9.0, n_samples).clip(29, 77)
    sex = np.random.binomial(1, 0.68, n_samples)
    cp = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.47, 0.17, 0.28, 0.08])
    trestbps = np.random.normal(131.6, 17.5, n_samples).clip(94, 200)
    chol = np.random.normal(246.3, 51.8, n_samples).clip(126, 564)
    fbs = np.random.binomial(1, 0.15, n_samples)
    restecg = np.random.choice([0, 1, 2], size=n_samples, p=[0.49, 0.49, 0.02])
    thalach = np.random.normal(149.6, 22.9, n_samples).clip(71, 202)
    exang = np.random.binomial(1, 0.33, n_samples)
    oldpeak = np.random.exponential(1.04, n_samples).clip(0, 6.2)
    slope = np.random.choice([0, 1, 2], size=n_samples, p=[0.46, 0.46, 0.08])
    ca = np.random.choice([0, 1, 2, 3], size=n_samples, p=[0.58, 0.22, 0.13, 0.07])
    thal = np.random.choice([0, 1, 2], size=n_samples, p=[0.55, 0.06, 0.39])
    
    X = np.column_stack([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])
    
    z = -1.5 + 0.8 * cp + 0.02 * (thalach - 150) - 0.7 * exang - 0.6 * oldpeak - 0.8 * ca - 0.9 * sex
    prob = 1 / (1 + np.exp(-z))
    y = (prob > 0.5).astype(int)
    
    if SKLEARN_AVAILABLE:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = LogisticRegression(max_iter=1000, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        preds = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, preds)
        print(f"-> Heart Disease Logistic Regression Accuracy: {acc * 100:.2f}%")
        
        os.makedirs("models", exist_ok=True)
        with open("models/heart_disease_model.sav", "wb") as f:
            pickle.dump({"model": model, "scaler": scaler}, f)
        print("-> Saved model to models/heart_disease_model.sav\n")
    else:
        print("-> Scikit-Learn not installed in environment. Run 'pip install scikit-learn' to retrain.")


def train_parkinsons_model():
    print("=" * 60)
    print("3. Training Parkinson's Disease Model (SVM RBF Classifier)")
    print("=" * 60)
    
    np.random.seed(42)
    n_samples = 195
    
    # 22 biomedical voice acoustic features
    X = np.random.randn(n_samples, 22)
    y = np.random.choice([0, 1], size=n_samples, p=[0.25, 0.75])
    
    if SKLEARN_AVAILABLE:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = SVC(kernel='rbf', probability=True, random_state=42)
        model.fit(X_train_scaled, y_train)
        
        preds = model.predict(X_test_scaled)
        acc = accuracy_score(y_test, preds)
        print(f"-> Parkinson's SVM (RBF) Model Accuracy: {acc * 100:.2f}%")
        
        os.makedirs("models", exist_ok=True)
        with open("models/parkinsons_model.sav", "wb") as f:
            pickle.dump({"model": model, "scaler": scaler}, f)
        print("-> Saved model to models/parkinsons_model.sav\n")
    else:
        print("-> Scikit-Learn not installed in environment. Run 'pip install scikit-learn' to retrain.")


if __name__ == '__main__':
    train_diabetes_model()
    train_heart_disease_model()
    train_parkinsons_model()
    print("All ML training routines completed.")
