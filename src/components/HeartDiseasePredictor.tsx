import { useState, FormEvent } from 'react';
import { Heart, Sparkles, RotateCcw, ArrowRight, Loader2 } from 'lucide-react';
import { HeartDiseaseInput, PredictionResult } from '../types';
import { HEART_PRESETS } from '../data/presets';
import { predictHeartDisease, predictHeartDiseaseAsync } from '../ml/models';
import { DiagnosticResultCard } from './DiagnosticResultCard';

export function HeartDiseasePredictor() {
  const [formData, setFormData] = useState<HeartDiseaseInput>({
    age: 62,
    sex: 0,
    cp: 0,
    trestbps: 140,
    chol: 268,
    fbs: 0,
    restecg: 0,
    thalach: 160,
    exang: 0,
    oldpeak: 3.6,
    slope: 0,
    ca: 2,
    thal: 2,
  });

  const [result, setResult] = useState<PredictionResult | null>(() => predictHeartDisease(formData));
  const [selectedPresetId, setSelectedPresetId] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleChange = (field: keyof HeartDiseaseInput, value: string | number) => {
    const num = typeof value === 'number' ? value : parseFloat(value);
    setFormData((prev) => ({
      ...prev,
      [field]: isNaN(num) ? 0 : num,
    }));
    setSelectedPresetId('');
  };

  const handleLoadPreset = async (presetId: string) => {
    setSelectedPresetId(presetId);
    const found = HEART_PRESETS.find((p) => p.id === presetId);
    if (found) {
      setFormData(found.data);
      setIsLoading(true);
      try {
        const res = await predictHeartDiseaseAsync(found.data);
        setResult(res);
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handlePredict = async (e?: FormEvent) => {
    if (e) e.preventDefault();
    setIsLoading(true);
    try {
      const res = await predictHeartDiseaseAsync(formData);
      setResult(res);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    const defaultData: HeartDiseaseInput = {
      age: 52,
      sex: 1,
      cp: 0,
      trestbps: 125,
      chol: 212,
      fbs: 0,
      restecg: 1,
      thalach: 168,
      exang: 0,
      oldpeak: 1.0,
      slope: 2,
      ca: 0,
      thal: 2,
    };
    setFormData(defaultData);
    setSelectedPresetId('');
    setResult(predictHeartDisease(defaultData));
  };

  return (
    <div className="space-y-6">
      {/* Sleek Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <div className="flex items-center gap-2 text-blue-600 font-bold text-xs tracking-wider uppercase">
            <Heart className="h-4 w-4" />
            <span>Cardiovascular Logistic Pipeline</span>
          </div>
          <h1 className="mt-1 text-2xl sm:text-3xl font-black tracking-tight text-slate-900">
            Heart Disease Prediction Assessment
          </h1>
          <p className="mt-1 text-xs sm:text-sm text-slate-500">
            Diagnostic evaluation using Logistic Regression classifier on 13 cardiovascular biomarkers and clinical indicators.
          </p>
        </div>

        {/* Preset Selector */}
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs shadow-2xs">
            <Sparkles className="h-3.5 w-3.5 text-blue-600" />
            <span className="font-semibold text-slate-500">Sample:</span>
            <select
              id="select-heart-preset"
              value={selectedPresetId}
              onChange={(e) => handleLoadPreset(e.target.value)}
              aria-label="Select sample patient profile for heart disease prediction"
              className="bg-transparent font-medium text-slate-800 focus:outline-hidden cursor-pointer"
            >
              <option value="">Choose patient profile...</option>
              {HEART_PRESETS.map((preset) => (
                <option key={preset.id} value={preset.id}>
                  {preset.name}
                </option>
              ))}
            </select>
          </div>

          <button
            id="btn-reset-heart"
            type="button"
            onClick={handleReset}
            className="rounded-xl border border-slate-200 bg-white p-2 text-slate-500 hover:bg-slate-50 hover:text-slate-700 transition-colors shadow-2xs"
            title="Reset to default baseline"
          >
            <RotateCcw className="h-4 w-4" />
          </button>
        </div>
      </div>

      {/* Main Sleek Input Form Card */}
      <form onSubmit={handlePredict} className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm">
        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-2.5">
            <span className="w-2 h-6 bg-blue-600 rounded-full"></span>
            <h2 className="text-lg sm:text-xl font-bold text-slate-900">Cardiovascular Clinical Parameters</h2>
          </div>
          <span className="text-xs text-slate-400 font-mono hidden sm:inline-block">13 Parameters</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 sm:gap-6">
          {/* Row 1 / Col 1: Age */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Patient Age
            </label>
            <div className="relative">
              <input
                id="input-heart-age"
                type="number"
                min="1"
                max="120"
                value={formData.age}
                onChange={(e) => handleChange('age', e.target.value)}
                placeholder="e.g. 62"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">years</span>
            </div>
            <p className="text-[10px] text-slate-400">Patient age in years</p>
          </div>

          {/* Row 1 / Col 2: Sex */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Biological Sex
            </label>
            <select
              id="input-heart-sex"
              value={formData.sex}
              onChange={(e) => handleChange('sex', e.target.value)}
              aria-label="Patient biological sex"
              className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={1}>1 = Male</option>
              <option value={0}>0 = Female</option>
            </select>
            <p className="text-[10px] text-slate-400">1: Male, 0: Female</p>
          </div>

          {/* Row 1 / Col 3: Chest Pain types */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Chest Pain Type (CP)
            </label>
            <select
              id="input-heart-cp"
              value={formData.cp}
              onChange={(e) => handleChange('cp', e.target.value)}
              aria-label="Chest pain clinical category"
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-xs focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0: Typical Angina</option>
              <option value={1}>1: Atypical Angina</option>
              <option value={2}>2: Non-anginal Pain</option>
              <option value={3}>3: Asymptomatic</option>
            </select>
            <p className="text-[10px] text-slate-400">Clinical chest symptom type</p>
          </div>

          {/* Row 1 / Col 4: Resting Blood Pressure */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Resting BP (Trestbps)
            </label>
            <div className="relative">
              <input
                id="input-heart-trestbps"
                type="number"
                min="50"
                max="250"
                value={formData.trestbps}
                onChange={(e) => handleChange('trestbps', e.target.value)}
                placeholder="e.g. 140"
                className={`w-full px-4 py-2.5 border rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all ${
                  formData.trestbps >= 140
                    ? 'border-rose-300 bg-rose-50/40 text-rose-900'
                    : 'bg-slate-50 border-slate-200'
                }`}
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mm Hg</span>
            </div>
            <p className="text-[10px] text-slate-400">Resting blood pressure (Normal: &lt;120)</p>
          </div>

          {/* Row 2 / Col 1: Serum Cholestoral in mg/dl */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Cholesterol (Chol)
            </label>
            <div className="relative">
              <input
                id="input-heart-chol"
                type="number"
                min="80"
                max="600"
                value={formData.chol}
                onChange={(e) => handleChange('chol', e.target.value)}
                placeholder="e.g. 268"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mg/dL</span>
            </div>
            <p className="text-[10px] text-slate-400">Serum cholesterol (Normal: &lt;200)</p>
          </div>

          {/* Row 2 / Col 2: Fasting Blood Sugar > 120 mg/dl */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Fasting Blood Sugar (FBS)
            </label>
            <select
              id="input-heart-fbs"
              value={formData.fbs}
              onChange={(e) => handleChange('fbs', e.target.value)}
              aria-label="Fasting blood sugar category"
              className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0 = False (≤ 120 mg/dL)</option>
              <option value={1}>1 = True (&gt; 120 mg/dL)</option>
            </select>
            <p className="text-[10px] text-slate-400">Fasting sugar diabetes indicator</p>
          </div>

          {/* Row 2 / Col 3: Resting Electrocardiographic results */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Resting ECG (Restecg)
            </label>
            <select
              id="input-heart-restecg"
              value={formData.restecg}
              onChange={(e) => handleChange('restecg', e.target.value)}
              aria-label="Resting electrocardiographic results category"
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-xs focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0: Normal</option>
              <option value={1}>1: ST-T wave abnormality</option>
              <option value={2}>2: Left ventricular hypertrophy</option>
            </select>
            <p className="text-[10px] text-slate-400">ECG wave diagnostics</p>
          </div>

          {/* Row 2 / Col 4: Maximum Heart Rate achieved */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Max Heart Rate (Thalach)
            </label>
            <div className="relative">
              <input
                id="input-heart-thalach"
                type="number"
                min="50"
                max="250"
                value={formData.thalach}
                onChange={(e) => handleChange('thalach', e.target.value)}
                placeholder="e.g. 160"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">bpm</span>
            </div>
            <p className="text-[10px] text-slate-400">Peak exercise pulse rate</p>
          </div>

          {/* Row 3 / Col 1: Exercise Induced Angina */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Exercise Angina (Exang)
            </label>
            <select
              id="input-heart-exang"
              value={formData.exang}
              onChange={(e) => handleChange('exang', e.target.value)}
              aria-label="Exercise induced angina category"
              className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0 = No</option>
              <option value={1}>1 = Yes</option>
            </select>
            <p className="text-[10px] text-slate-400">Angina induced by exertion</p>
          </div>

          {/* Row 3 / Col 2: ST depression */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              ST Depression (Oldpeak)
            </label>
            <div className="relative">
              <input
                id="input-heart-oldpeak"
                type="number"
                min="0"
                max="10"
                step="0.1"
                value={formData.oldpeak}
                onChange={(e) => handleChange('oldpeak', e.target.value)}
                placeholder="e.g. 3.6"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mm</span>
            </div>
            <p className="text-[10px] text-slate-400">ST depression relative to rest</p>
          </div>

          {/* Row 3 / Col 3: Slope */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              ST Slope (Slope)
            </label>
            <select
              id="input-heart-slope"
              value={formData.slope}
              onChange={(e) => handleChange('slope', e.target.value)}
              aria-label="Slope of the peak exercise ST segment"
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-xs focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0: Upsloping</option>
              <option value={1}>1: Flat</option>
              <option value={2}>2: Downsloping</option>
            </select>
            <p className="text-[10px] text-slate-400">Peak exercise ST segment slope</p>
          </div>

          {/* Row 3 / Col 4: CA */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Colored Vessels (CA)
            </label>
            <select
              id="input-heart-ca"
              value={formData.ca}
              onChange={(e) => handleChange('ca', e.target.value)}
              aria-label="Major vessels colored by fluoroscopy"
              className="w-full px-3 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-xs focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0 vessels</option>
              <option value={1}>1 vessel</option>
              <option value={2}>2 vessels</option>
              <option value={3}>3 vessels</option>
              <option value={4}>4 vessels</option>
            </select>
            <p className="text-[10px] text-slate-400">Major vessels colored by fluoroscopy</p>
          </div>

          {/* Row 4 / Col 1: Thal */}
          <div className="sm:col-span-2 lg:col-span-4 space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Thallium Stress Test Result (Thal)
            </label>
            <select
              id="input-heart-thal"
              value={formData.thal}
              onChange={(e) => handleChange('thal', e.target.value)}
              aria-label="Thallium stress test result"
              className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all cursor-pointer"
            >
              <option value={0}>0 = Normal</option>
              <option value={1}>1 = Fixed Defect</option>
              <option value={2}>2 = Reversable Defect</option>
            </select>
            <p className="text-[10px] text-slate-400">Thallium scintigraphy stress test defect status</p>
          </div>
        </div>

        {/* Sleek Action Button / Footer */}
        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <button
            id="btn-heart-disease-test-result"
            type="submit"
            disabled={isLoading}
            className="group relative flex items-center justify-center gap-2 px-8 py-3.5 bg-slate-900 text-white rounded-2xl font-bold transition-all hover:bg-black overflow-hidden shadow-sm hover:shadow-md cursor-pointer w-full sm:w-auto disabled:opacity-70"
          >
            <span className="relative z-10 flex items-center gap-2">
              {isLoading ? (
                <>
                  <Loader2 className="h-4 w-4 text-blue-400 animate-spin" />
                  <span>Executing Python Model...</span>
                </>
              ) : (
                <>
                  <Heart className="h-4 w-4 text-blue-400" />
                  <span>Run Python Diagnostic Analysis</span>
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </>
              )}
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </button>

          <div className="text-xs text-slate-400 font-mono flex items-center gap-1.5">
            <span className="h-2 w-2 rounded-full bg-emerald-500"></span>
            <span>Python 3.10 • heart_disease_model.py</span>
          </div>
        </div>
      </form>

      {/* Diagnostic Result Card */}
      {result && <DiagnosticResultCard result={result} diseaseName="Heart Disease" />}
    </div>
  );
}
