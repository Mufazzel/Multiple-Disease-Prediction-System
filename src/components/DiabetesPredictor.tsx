import { useState, FormEvent } from 'react';
import { Activity, Sparkles, RotateCcw, Info, ArrowRight, Loader2 } from 'lucide-react';
import { DiabetesInput, PredictionResult } from '../types';
import { DIABETES_PRESETS } from '../data/presets';
import { predictDiabetes, predictDiabetesAsync } from '../ml/models';
import { DiagnosticResultCard } from './DiagnosticResultCard';

export function DiabetesPredictor() {
  const [formData, setFormData] = useState<DiabetesInput>({
    pregnancies: 6,
    glucose: 148,
    bloodPressure: 72,
    skinThickness: 35,
    insulin: 0,
    bmi: 33.6,
    diabetesPedigree: 0.627,
    age: 50,
  });

  const [result, setResult] = useState<PredictionResult | null>(() => predictDiabetes(formData));
  const [selectedPresetId, setSelectedPresetId] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleChange = (field: keyof DiabetesInput, value: string) => {
    const num = parseFloat(value);
    setFormData((prev) => ({
      ...prev,
      [field]: isNaN(num) ? 0 : num,
    }));
    setSelectedPresetId('');
  };

  const handleLoadPreset = async (presetId: string) => {
    setSelectedPresetId(presetId);
    const found = DIABETES_PRESETS.find((p) => p.id === presetId);
    if (found) {
      setFormData(found.data);
      setIsLoading(true);
      try {
        const res = await predictDiabetesAsync(found.data);
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
      const res = await predictDiabetesAsync(formData);
      setResult(res);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    const defaultData: DiabetesInput = {
      pregnancies: 1,
      glucose: 95,
      bloodPressure: 70,
      skinThickness: 20,
      insulin: 79,
      bmi: 24.5,
      diabetesPedigree: 0.35,
      age: 29,
    };
    setFormData(defaultData);
    setSelectedPresetId('');
    setResult(predictDiabetes(defaultData));
  };

  return (
    <div className="space-y-6">
      {/* Sleek Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <div className="flex items-center gap-2 text-blue-600 font-bold text-xs tracking-wider uppercase">
            <Activity className="h-4 w-4" />
            <span>Pima Indians Clinical Model</span>
          </div>
          <h1 className="mt-1 text-2xl sm:text-3xl font-black tracking-tight text-slate-900">
            Diabetes Prediction Assessment
          </h1>
          <p className="mt-1 text-xs sm:text-sm text-slate-500">
            Diagnostic classification utilizing Support Vector Machine (SVM) algorithm on 8 standardized metabolic parameters.
          </p>
        </div>

        {/* Preset Selector */}
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs shadow-2xs">
            <Sparkles className="h-3.5 w-3.5 text-blue-600" />
            <span className="font-semibold text-slate-500">Sample:</span>
            <select
              id="select-diabetes-preset"
              value={selectedPresetId}
              onChange={(e) => handleLoadPreset(e.target.value)}
              aria-label="Select sample patient profile for diabetes prediction"
              className="bg-transparent font-medium text-slate-800 focus:outline-hidden cursor-pointer"
            >
              <option value="">Choose patient profile...</option>
              {DIABETES_PRESETS.map((preset) => (
                <option key={preset.id} value={preset.id}>
                  {preset.name}
                </option>
              ))}
            </select>
          </div>

          <button
            id="btn-reset-diabetes"
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
            <h2 className="text-lg sm:text-xl font-bold text-slate-900">Diabetes Clinical Parameters</h2>
          </div>
          <span className="text-xs text-slate-400 font-mono hidden sm:inline-block">8 Parameters</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5 sm:gap-6">
          {/* Row 1 / Col 1: Pregnancies */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Pregnancies
            </label>
            <div className="relative">
              <input
                id="input-pregnancies"
                type="number"
                min="0"
                max="20"
                step="1"
                value={formData.pregnancies}
                onChange={(e) => handleChange('pregnancies', e.target.value)}
                placeholder="e.g. 6"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">count</span>
            </div>
            <p className="text-[10px] text-slate-400">Total pregnancy count (0 - 17)</p>
          </div>

          {/* Row 1 / Col 2: Glucose Level */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Glucose Level
            </label>
            <div className="relative">
              <input
                id="input-glucose"
                type="number"
                min="0"
                max="300"
                step="1"
                value={formData.glucose}
                onChange={(e) => handleChange('glucose', e.target.value)}
                placeholder="e.g. 148"
                className={`w-full px-4 py-2.5 border rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all ${
                  formData.glucose >= 140
                    ? 'border-rose-300 bg-rose-50/40 text-rose-900'
                    : 'bg-slate-50 border-slate-200'
                }`}
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mg/dL</span>
            </div>
            <p className="text-[10px] text-slate-400">Plasma glucose (Normal: 70-99)</p>
          </div>

          {/* Row 1 / Col 3: Blood Pressure */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Blood Pressure
            </label>
            <div className="relative">
              <input
                id="input-blood-pressure"
                type="number"
                min="0"
                max="200"
                step="1"
                value={formData.bloodPressure}
                onChange={(e) => handleChange('bloodPressure', e.target.value)}
                placeholder="e.g. 72"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mm Hg</span>
            </div>
            <p className="text-[10px] text-slate-400">Diastolic blood pressure</p>
          </div>

          {/* Row 1 / Col 4: Skin Thickness */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Skin Thickness
            </label>
            <div className="relative">
              <input
                id="input-skin-thickness"
                type="number"
                min="0"
                max="99"
                step="1"
                value={formData.skinThickness}
                onChange={(e) => handleChange('skinThickness', e.target.value)}
                placeholder="e.g. 35"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mm</span>
            </div>
            <p className="text-[10px] text-slate-400">Triceps skin fold thickness</p>
          </div>

          {/* Row 2 / Col 1: Insulin Level */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Insulin Level
            </label>
            <div className="relative">
              <input
                id="input-insulin"
                type="number"
                min="0"
                max="900"
                step="1"
                value={formData.insulin}
                onChange={(e) => handleChange('insulin', e.target.value)}
                placeholder="e.g. 0"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">mu U/ml</span>
            </div>
            <p className="text-[10px] text-slate-400">2-Hour serum insulin</p>
          </div>

          {/* Row 2 / Col 2: BMI value */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              BMI Value
            </label>
            <div className="relative">
              <input
                id="input-bmi"
                type="number"
                min="0"
                max="70"
                step="0.1"
                value={formData.bmi}
                onChange={(e) => handleChange('bmi', e.target.value)}
                placeholder="e.g. 33.6"
                className={`w-full px-4 py-2.5 border rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all ${
                  formData.bmi >= 30
                    ? 'border-rose-300 bg-rose-50/40 text-rose-900'
                    : 'bg-slate-50 border-slate-200'
                }`}
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">kg/m²</span>
            </div>
            <p className="text-[10px] text-slate-400">Body mass index (Normal: 18.5-24.9)</p>
          </div>

          {/* Row 2 / Col 3: Diabetes Pedigree Function */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Pedigree Function
            </label>
            <div className="relative">
              <input
                id="input-pedigree"
                type="number"
                min="0"
                max="3"
                step="0.001"
                value={formData.diabetesPedigree}
                onChange={(e) => handleChange('diabetesPedigree', e.target.value)}
                placeholder="e.g. 0.627"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">score</span>
            </div>
            <p className="text-[10px] text-slate-400">Genetic lineage risk calculation</p>
          </div>

          {/* Row 2 / Col 4: Age */}
          <div className="space-y-1.5">
            <label className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block">
              Patient Age
            </label>
            <div className="relative">
              <input
                id="input-age"
                type="number"
                min="1"
                max="120"
                step="1"
                value={formData.age}
                onChange={(e) => handleChange('age', e.target.value)}
                placeholder="e.g. 50"
                className="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-sm focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <span className="absolute right-3 top-2.5 text-xs text-slate-400 font-medium">years</span>
            </div>
            <p className="text-[10px] text-slate-400">Patient age in years</p>
          </div>
        </div>

        {/* Sleek Action Button / Footer */}
        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <button
            id="btn-diabetes-test-result"
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
                  <Activity className="h-4 w-4 text-blue-400" />
                  <span>Run Python Diagnostic Analysis</span>
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </>
              )}
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </button>

          <div className="text-xs text-slate-400 font-mono flex items-center gap-1.5">
            <span className="h-2 w-2 rounded-full bg-emerald-500"></span>
            <span>Python 3.10 • diabetes_model.py</span>
          </div>
        </div>
      </form>

      {/* Diagnostic Result Card */}
      {result && <DiagnosticResultCard result={result} diseaseName="Diabetes" />}
    </div>
  );
}
