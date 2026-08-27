import { useState, FormEvent } from 'react';
import { User, Sparkles, RotateCcw, ArrowRight, Loader2 } from 'lucide-react';
import { ParkinsonsInput, PredictionResult } from '../types';
import { PARKINSONS_PRESETS } from '../data/presets';
import { predictParkinsons, predictParkinsonsAsync } from '../ml/models';
import { DiagnosticResultCard } from './DiagnosticResultCard';

export function ParkinsonsPredictor() {
  const [formData, setFormData] = useState<ParkinsonsInput>({
    fo: 119.992,
    fhi: 157.302,
    flo: 74.997,
    jitterPercent: 0.00784,
    jitterAbs: 0.00007,
    rap: 0.0037,
    ppq: 0.00554,
    ddp: 0.01109,
    shimmer: 0.04374,
    shimmerDb: 0.426,
    apq3: 0.02182,
    apq5: 0.0313,
    apq: 0.02971,
    dda: 0.06545,
    nhr: 0.02211,
    hnr: 21.033,
    rpde: 0.414783,
    dfa: 0.815285,
    spread1: -4.813031,
    spread2: 0.266482,
    d2: 2.301442,
    ppe: 0.284654,
  });

  const [result, setResult] = useState<PredictionResult | null>(() => predictParkinsons(formData));
  const [selectedPresetId, setSelectedPresetId] = useState<string>('');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleChange = (field: keyof ParkinsonsInput, value: string) => {
    const num = parseFloat(value);
    setFormData((prev) => ({
      ...prev,
      [field]: isNaN(num) ? 0 : num,
    }));
    setSelectedPresetId('');
  };

  const handleLoadPreset = async (presetId: string) => {
    setSelectedPresetId(presetId);
    const found = PARKINSONS_PRESETS.find((p) => p.id === presetId);
    if (found) {
      setFormData(found.data);
      setIsLoading(true);
      try {
        const res = await predictParkinsonsAsync(found.data);
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
      const res = await predictParkinsonsAsync(formData);
      setResult(res);
    } finally {
      setIsLoading(false);
    }
  };

  const handleReset = () => {
    const defaultData: ParkinsonsInput = {
      fo: 197.076,
      fhi: 206.896,
      flo: 192.055,
      jitterPercent: 0.00289,
      jitterAbs: 0.00001,
      rap: 0.00166,
      ppq: 0.00168,
      ddp: 0.00498,
      shimmer: 0.01098,
      shimmerDb: 0.097,
      apq3: 0.00563,
      apq5: 0.0068,
      apq: 0.00802,
      dda: 0.01689,
      nhr: 0.00339,
      hnr: 26.775,
      rpde: 0.422229,
      dfa: 0.741367,
      spread1: -7.348399,
      spread2: 0.177551,
      d2: 1.743867,
      ppe: 0.085569,
    };
    setFormData(defaultData);
    setSelectedPresetId('');
    setResult(predictParkinsons(defaultData));
  };

  const fields: { key: keyof ParkinsonsInput; label: string; desc: string }[] = [
    { key: 'fo', label: 'MDVP:Fo(Hz)', desc: 'Vocal fundamental freq' },
    { key: 'fhi', label: 'MDVP:Fhi(Hz)', desc: 'Max vocal fundamental freq' },
    { key: 'flo', label: 'MDVP:Flo(Hz)', desc: 'Min vocal fundamental freq' },
    { key: 'jitterPercent', label: 'MDVP:Jitter(%)', desc: 'Jitter percentage' },
    { key: 'jitterAbs', label: 'MDVP:Jitter(Abs)', desc: 'Absolute jitter (µs)' },
    { key: 'rap', label: 'MDVP:RAP', desc: 'Relative amplitude perturbation' },
    { key: 'ppq', label: 'MDVP:PPQ', desc: 'Period perturbation quotient' },
    { key: 'ddp', label: 'Jitter:DDP', desc: 'Degree difference in jitter' },
    { key: 'shimmer', label: 'MDVP:Shimmer', desc: 'Amplitude variation measure' },
    { key: 'shimmerDb', label: 'MDVP:Shimmer(dB)', desc: 'Amplitude variation in dB' },
    { key: 'apq3', label: 'Shimmer:APQ3', desc: '3-point amp perturbation' },
    { key: 'apq5', label: 'Shimmer:APQ5', desc: '5-point amp perturbation' },
    { key: 'apq', label: 'MDVP:APQ', desc: '11-point amp perturbation' },
    { key: 'dda', label: 'Shimmer:DDA', desc: 'Differential amplitude measure' },
    { key: 'nhr', label: 'NHR', desc: 'Noise-to-Harmonics ratio' },
    { key: 'hnr', label: 'HNR', desc: 'Harmonics-to-Noise ratio' },
    { key: 'rpde', label: 'RPDE', desc: 'Recurrence density entropy' },
    { key: 'dfa', label: 'DFA', desc: 'Detrended fluctuation analysis' },
    { key: 'spread1', label: 'spread1', desc: 'Frequency variation spread 1' },
    { key: 'spread2', label: 'spread2', desc: 'Nonlinear variation spread 2' },
    { key: 'd2', label: 'D2', desc: 'Correlation dimension' },
    { key: 'ppe', label: 'PPE', desc: 'Pitch period entropy' },
  ];

  return (
    <div className="space-y-6">
      {/* Sleek Page Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 pb-4">
        <div>
          <div className="flex items-center gap-2 text-blue-600 font-bold text-xs tracking-wider uppercase">
            <User className="h-4 w-4" />
            <span>Oxford Acoustic Dysphonia Model</span>
          </div>
          <h1 className="mt-1 text-2xl sm:text-3xl font-black tracking-tight text-slate-900">
            Parkinson's Disease Prediction Assessment
          </h1>
          <p className="mt-1 text-xs sm:text-sm text-slate-500">
            Support Vector Machine classification on 22 biomedical voice acoustic measurements for early neurological evaluation.
          </p>
        </div>

        {/* Preset Selector */}
        <div className="flex items-center gap-2">
          <div className="flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs shadow-2xs">
            <Sparkles className="h-3.5 w-3.5 text-blue-600" />
            <span className="font-semibold text-slate-500">Sample:</span>
            <select
              id="select-parkinsons-preset"
              value={selectedPresetId}
              onChange={(e) => handleLoadPreset(e.target.value)}
              aria-label="Select sample patient profile for Parkinson's disease prediction"
              className="bg-transparent font-medium text-slate-800 focus:outline-hidden cursor-pointer"
            >
              <option value="">Choose patient profile...</option>
              {PARKINSONS_PRESETS.map((preset) => (
                <option key={preset.id} value={preset.id}>
                  {preset.name}
                </option>
              ))}
            </select>
          </div>

          <button
            id="btn-reset-parkinsons"
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
            <h2 className="text-lg sm:text-xl font-bold text-slate-900">Acoustic Vocal Dysphonia Parameters</h2>
          </div>
          <span className="text-xs text-slate-400 font-mono hidden sm:inline-block">22 Parameters</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-4">
          {fields.map((field) => (
            <div key={field.key} className="space-y-1">
              <label
                className="text-[10px] uppercase font-bold text-slate-400 tracking-wider block truncate"
                title={field.label}
              >
                {field.label}
              </label>
              <input
                id={`input-parkinsons-${field.key}`}
                type="number"
                step="any"
                value={formData[field.key]}
                onChange={(e) => handleChange(field.key, e.target.value)}
                placeholder={field.label}
                className="w-full px-3 py-2 bg-slate-50 border border-slate-200 rounded-xl font-medium text-slate-800 text-xs focus:ring-2 focus:ring-blue-100 focus:border-blue-400 focus:bg-white outline-none transition-all"
              />
              <p className="text-[9px] text-slate-400 truncate" title={field.desc}>
                {field.desc}
              </p>
            </div>
          ))}
        </div>

        {/* Sleek Action Button / Footer */}
        <div className="mt-8 pt-6 border-t border-slate-100 flex flex-col sm:flex-row items-center justify-between gap-4">
          <button
            id="btn-parkinsons-test-result"
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
                  <User className="h-4 w-4 text-blue-400" />
                  <span>Run Python Diagnostic Analysis</span>
                  <ArrowRight className="h-4 w-4 transition-transform group-hover:translate-x-0.5" />
                </>
              )}
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-blue-600 to-indigo-600 opacity-0 group-hover:opacity-100 transition-opacity"></div>
          </button>

          <div className="text-xs text-slate-400 font-mono flex items-center gap-1.5">
            <span className="h-2 w-2 rounded-full bg-emerald-500"></span>
            <span>Python 3.10 • parkinsons_model.py</span>
          </div>
        </div>
      </form>

      {/* Diagnostic Result Card */}
      {result && <DiagnosticResultCard result={result} diseaseName="Parkinson's Disease" />}
    </div>
  );
}
