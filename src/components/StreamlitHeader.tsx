import { Cpu, Menu, Shield } from 'lucide-react';

interface StreamlitHeaderProps {
  onToggleSidebar?: () => void;
  isSidebarOpen?: boolean;
}

export function StreamlitHeader({ onToggleSidebar }: StreamlitHeaderProps) {
  return (
    <header className="shrink-0 z-30 flex h-16 items-center justify-between border-b border-slate-200 bg-white px-4 sm:px-8 shadow-xs">
      <div className="flex items-center gap-3">
        <button
          id="btn-toggle-sidebar"
          type="button"
          onClick={onToggleSidebar}
          className="rounded-xl p-2 text-slate-600 hover:bg-slate-100 md:hidden focus:outline-hidden"
          title="Toggle Navigation Menu"
        >
          <Menu className="h-5 w-5" />
        </button>

        <div className="flex items-center gap-3">
          <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-blue-600 text-white shadow-xs">
            <Shield className="h-5 w-5" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="font-bold text-slate-900 text-base sm:text-lg tracking-tight">
                Multiple Disease Prediction System
              </span>
              <span className="hidden sm:inline-flex items-center gap-1.5 rounded-full bg-blue-50 px-2.5 py-0.5 text-xs font-semibold text-blue-700 border border-blue-100">
                <span className="h-1.5 w-1.5 rounded-full bg-blue-600 animate-pulse"></span>
                ML Diagnostics Suite
              </span>
            </div>
            <p className="text-xs text-slate-400 hidden sm:block font-medium">
              Multiple Disease Prediction Engine • Python & Scikit-Learn Architecture
            </p>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-2 sm:gap-3">
        <div className="flex items-center gap-1.5 rounded-xl bg-slate-100 px-3 py-1.5 text-xs text-slate-700 font-mono font-medium">
          <Cpu className="h-3.5 w-3.5 text-blue-600" />
          <span className="text-[11px]">Streamlit v1.22</span>
        </div>
      </div>
    </header>
  );
}
