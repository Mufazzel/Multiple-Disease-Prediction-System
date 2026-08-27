"""
Python Type Definitions and Data Structures for Multiple Disease Prediction System.
"""
from typing import TypedDict, List, Literal, Union, Dict, Any

DiseaseType = Literal['diabetes', 'heart', 'parkinsons']
RiskLevel = Literal['Low', 'Moderate', 'High']
ImpactType = Literal['normal', 'moderate', 'high_risk']

class ContributingFactor(TypedDict):
    factor: str
    value: Union[str, int, float]
    impact: ImpactType
    description: str

class PredictionResult(TypedDict, total=False):
    hasDisease: bool
    diagnosisMessage: str
    confidenceProbability: float  # 0.0 to 1.0
    riskLevel: RiskLevel
    engine: str
    contributingFactors: List[ContributingFactor]

class DiabetesInput(TypedDict):
    pregnancies: int
    glucose: float
    bloodPressure: float
    skinThickness: float
    insulin: float
    bmi: float
    diabetesPedigree: float
    age: int

class HeartDiseaseInput(TypedDict):
    age: int
    sex: int  # 1 = Male, 0 = Female
    cp: int  # Chest Pain: 0=Typical, 1=Atypical, 2=Non-anginal, 3=Asymptomatic
    trestbps: int  # Resting BP (mmHg)
    chol: int  # Serum cholesterol (mg/dL)
    fbs: int  # Fasting blood sugar > 120 mg/dL (1=True, 0=False)
    restecg: int  # Resting ECG (0, 1, 2)
    thalach: int  # Max HR
    exang: int  # Exercise induced angina (1=Yes, 0=No)
    oldpeak: float  # ST depression
    slope: int  # ST slope (0, 1, 2)
    ca: int  # Vessels colored (0-4)
    thal: int  # 0=Normal, 1=Fixed, 2=Reversible

class ParkinsonsInput(TypedDict):
    fo: float
    fhi: float
    flo: float
    jitterPercent: float
    jitterAbs: float
    rap: float
    ppq: float
    ddp: float
    shimmer: float
    shimmerDb: float
    apq3: float
    apq5: float
    apq: float
    dda: float
    nhr: float
    hnr: float
    rpde: float
    dfa: float
    spread1: float
    spread2: float
    d2: float
    ppe: float

class PatientPreset(TypedDict):
    id: str
    name: str
    description: str
    expectedOutcome: str
    data: Dict[str, Any]
