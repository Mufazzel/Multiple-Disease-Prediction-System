import { useState } from 'react';
import { CheckCircle2, AlertTriangle, ShieldCheck, Copy, Check, Info, Sparkles } from 'lucide-react';
import confetti from 'canvas-confetti';
import { PredictionResult } from '../types';

interface DiagnosticResultCardProps {
  result: PredictionResult;
  diseaseName: string;
}

export function DiagnosticResultCard({ result, diseaseName }: DiagnosticResultCardProps) {
  const [copied, setCopied] = useState(false);

  const handleCopy = () => {
    const text = `MedPredict AI - ${diseaseName} Diagnostic Assessment:
Result: ${result.diagnosisMessage}
Confidence Probability: ${(result.confidenceProbability * 100).toFixed(1)}%
Risk Classification: ${result.riskLevel}
Key Contributing Biomarkers:
${result.contributingFactors.map((f) => `- ${f.factor}: ${f.value} (${f.impact})`).join('\n')}`;

    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const triggerConfetti = () => {
    confetti({
      particleCount: 50,
      spread: 60,
      origin: { y: 0.8 },
      colors: ['#2563EB', '#10B981', '#60A5FA'],
    });
  };

  const isPositive = result.hasDisease;

  return (
    <div id="diagnostic-result-container" className="mt-8 space-y-6">
      {/* 2-Column Sleek Diagnostic & Analytical Cards Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Card 1: Diagnostic Outcome */}
        <div
          className={`rounded-3xl border p-6 sm:p-7 transition-all ${
            isPositive
              ? 'bg-rose-50/70 border-rose-200 shadow-xs'
              : 'bg-emerald-50/70 border-emerald-200 shadow-xs'
          }`}
        >
          <div className="flex items-start justify-between gap-4">
            <div className="flex items-center gap-3.5">
              <div
                className={`flex h-12 w-12 shrink-0 items-center justify-center rounded-2xl ${
                  isPositive
                    ? 'bg-rose-500/20 text-rose-600'
                    : 'bg-emerald-500/20 text-emerald-600'
                }`}
              >
                {isPositive ? (
                  <AlertTriangle className="h-6 w-6" />
                ) : (
                  <CheckCircle2 className="h-6 w-6" />
                )}
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span
                    className={`text-[10px] font-bold uppercase tracking-wider ${
                      isPositive ? 'text-rose-600' : 'text-emerald-700'
                    }`}
                  >
                    Diagnostic Outcome
                  </span>
                  <span
                    className={`rounded-md px-2 py-0.5 text-[10px] font-bold ${
                      isPositive
                        ? 'bg-rose-200 text-rose-900'
                        : 'bg-emerald-200 text-emerald-900'
                    }`}
                  >
                    {result.riskLevel} Risk
                  </span>
                </div>
                <h3
                  className={`mt-0.5 text-xl font-bold tracking-tight ${
                    isPositive ? 'text-rose-950' : 'text-emerald-950'
                  }`}
                >
                  {result.diagnosisMessage}
                </h3>
              </div>
            </div>

            <div className="flex items-center gap-1.5 shrink-0">
              {!isPositive && (
                <button
                  type="button"
                  onClick={triggerConfetti}
                  className="rounded-xl border border-emerald-200 bg-white px-2.5 py-1.5 text-xs font-semibold text-emerald-700 hover:bg-emerald-50 transition-colors shadow-2xs"
                  title="Celebrate non-pathological score"
                >
                  <Sparkles className="h-3.5 w-3.5" />
                </button>
              )}
              <button
                id="btn-copy-diagnosis"
                type="button"
                onClick={handleCopy}
                className="inline-flex items-center gap-1.5 rounded-xl border border-slate-200 bg-white px-3 py-1.5 text-xs font-semibold text-slate-700 hover:bg-slate-50 transition-colors shadow-2xs"
              >
                {copied ? (
                  <>
                    <Check className="h-3.5 w-3.5 text-emerald-600" />
                    <span>Copied</span>
                  </>
                ) : (
                  <>
                    <Copy className="h-3.5 w-3.5 text-slate-400" />
                    <span>Copy</span>
                  </>
                )}
              </button>
            </div>
          </div>

          <div
            className={`mt-4 text-xs sm:text-sm leading-relaxed ${
              isPositive ? 'text-rose-800/90' : 'text-emerald-800/90'
            }`}
          >
            {isPositive
              ? `Diagnostic markers indicate significant elevation above normal control baseline. Clinical consultation and confirmatory testing are recommended for ${diseaseName}.`
              : `Based on machine learning classification of the evaluated biometric parameters, the patient does not meet the clinical criteria for ${diseaseName} at this time.`}
          </div>
        </div>

        {/* Card 2: Sleek Dark Analytical Confidence Card */}
        <div className="bg-slate-900 rounded-3xl p-6 sm:p-7 text-white shadow-sm flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <h3 className="font-bold text-blue-300 text-xs uppercase tracking-widest">
                Analytical Confidence
              </h3>
              <span className="flex items-center gap-1 text-[11px] text-slate-400 font-mono">
                <ShieldCheck className="h-3.5 w-3.5 text-emerald-400" />
                ML Hyperplane Verified
              </span>
            </div>

            <div className="flex items-end gap-3">
              <div className="text-4xl font-black font-mono tracking-tight text-white">
                {(result.confidenceProbability * 100).toFixed(1)}%
              </div>
              <div className="text-blue-400 text-xs font-semibold pb-1">
                {isPositive ? 'Disease Probability Score' : 'Negative Likelihood Score'}
              </div>
            </div>

            {/* Sleek Progress Bar */}
            <div className="mt-4 h-2.5 w-full bg-slate-800 rounded-full overflow-hidden p-0.5">
              <div
                className={`h-full rounded-full transition-all duration-500 ${
                  isPositive ? 'bg-rose-500' : 'bg-blue-500'
                }`}
                style={{ width: `${Math.max(result.confidenceProbability * 100, 8)}%` }}
              />
            </div>
            <div className="mt-2 flex justify-between text-[10px] text-slate-400 font-mono">
              <span>0% Low Risk</span>
              <span>Decision Threshold: 50%</span>
              <span>100% High Risk</span>
            </div>
          </div>

          <div className="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs text-slate-400">
            <span>{result.engine || 'Python 3.10 Scikit-Learn Pipeline'}</span>
            <span className="font-mono text-[11px] text-emerald-400">● Python Executed</span>
          </div>
        </div>
      </div>

      {/* Contributing Factors & Biomarker Breakdown */}
      {result.contributingFactors && result.contributingFactors.length > 0 && (
        <div className="bg-white rounded-3xl border border-slate-200 p-6 sm:p-7 shadow-sm">
          <div className="flex items-center gap-2 mb-4">
            <span className="w-1.5 h-5 bg-blue-600 rounded-full"></span>
            <h4 className="text-base font-bold text-slate-900">Key Contributing Clinical Biomarkers</h4>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
            {result.contributingFactors.map((factor, idx) => (
              <div
                key={idx}
                className="flex flex-col justify-between rounded-2xl border border-slate-200 bg-slate-50 p-3.5 transition-all hover:bg-white hover:shadow-xs"
              >
                <div>
                  <div className="flex items-center justify-between gap-2">
                    <span className="text-xs font-bold text-slate-800 truncate">{factor.factor}</span>
                    <span
                      className={`rounded-md px-1.5 py-0.5 text-[10px] font-mono font-bold ${
                        factor.impact === 'high_risk'
                          ? 'bg-rose-100 text-rose-700'
                          : factor.impact === 'moderate'
                          ? 'bg-amber-100 text-amber-700'
                          : 'bg-emerald-100 text-emerald-700'
                      }`}
                    >
                      {factor.value}
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-500 mt-1 leading-snug">{factor.description}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
