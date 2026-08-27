export type DiseaseType = 'diabetes' | 'heart' | 'parkinsons';

export interface DiabetesInput {
  pregnancies: number;
  glucose: number;
  bloodPressure: number;
  skinThickness: number;
  insulin: number;
  bmi: number;
  diabetesPedigree: number;
  age: number;
}

export interface HeartDiseaseInput {
  age: number;
  sex: number; // 1 = Male, 0 = Female
  cp: number; // Chest pain: 0 = Typical angina, 1 = Atypical, 2 = Non-anginal, 3 = Asymptomatic
  trestbps: number; // Resting BP (mm Hg)
  chol: number; // Serum cholesterol (mg/dl)
  fbs: number; // Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
  restecg: number; // Resting ECG (0 = Normal, 1 = ST-T wave abnormality, 2 = LV hypertrophy)
  thalach: number; // Max heart rate achieved
  exang: number; // Exercise induced angina (1 = Yes, 0 = No)
  oldpeak: number; // ST depression induced by exercise
  slope: number; // Slope of peak exercise ST (0 = Upsloping, 1 = Flat, 2 = Downsloping)
  ca: number; // Number of major vessels (0-4) colored by fluoroscopy
  thal: number; // 0 = Normal, 1 = Fixed defect, 2 = Reversible defect
}

export interface ParkinsonsInput {
  fo: number; // MDVP:Fo(Hz)
  fhi: number; // MDVP:Fhi(Hz)
  flo: number; // MDVP:Flo(Hz)
  jitterPercent: number; // MDVP:Jitter(%)
  jitterAbs: number; // MDVP:Jitter(Abs)
  rap: number; // MDVP:RAP
  ppq: number; // MDVP:PPQ
  ddp: number; // Jitter:DDP
  shimmer: number; // MDVP:Shimmer
  shimmerDb: number; // MDVP:Shimmer(dB)
  apq3: number; // Shimmer:APQ3
  apq5: number; // Shimmer:APQ5
  apq: number; // MDVP:APQ
  dda: number; // Shimmer:DDA
  nhr: number; // NHR
  hnr: number; // HNR
  rpde: number; // RPDE
  dfa: number; // DFA
  spread1: number; // spread1
  spread2: number; // spread2
  d2: number; // D2
  ppe: number; // PPE
}

export interface PredictionResult {
  hasDisease: boolean;
  diagnosisMessage: string;
  confidenceProbability: number; // 0 to 1
  riskLevel: 'Low' | 'Moderate' | 'High';
  engine?: string;
  contributingFactors: {
    factor: string;
    value: string | number;
    impact: 'normal' | 'moderate' | 'high_risk';
    description: string;
  }[];
}

export interface PatientPreset<T> {
  id: string;
  name: string;
  description: string;
  expectedOutcome: string;
  data: T;
}
