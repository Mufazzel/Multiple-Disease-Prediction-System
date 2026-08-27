import { Activity, Heart, User, ShieldCheck, X } from 'lucide-react';
import { DiseaseType } from '../types';

interface SidebarProps {
  currentTab: DiseaseType;
  onSelectTab: (tab: DiseaseType) => void;
  isOpenMobile: boolean;
  onCloseMobile: () => void;
}

export function Sidebar({ currentTab, onSelectTab, isOpenMobile, onCloseMobile }: SidebarProps) {
  const menuItems = [
    {
      id: 'diabetes' as DiseaseType,
      label: 'Diabetes Prediction',
      icon: Activity,
      desc: 'PIMA Indians SVM Classifier (8 biomarkers)',
      tag: 'SVM',
    },
    {
      id: 'heart' as DiseaseType,
      label: 'Heart Disease',
      icon: Heart,
      desc: 'UCI Logistic Regression (13 clinical factors)',
      tag: 'Logistic Reg',
    },
    {
      id: 'parkinsons' as DiseaseType,
      label: "Parkinson's Prediction",
      icon: User,
      desc: 'Oxford Vocal Dysphonia Model (22 features)',
      tag: 'SVM RBF',
    },
  ];

  const handleSelect = (tab: DiseaseType) => {
    onSelectTab(tab);
    onCloseMobile();
  };

  return (
    <>
      {/* Mobile overlay */}
      {isOpenMobile && (
        <div
          className="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-xs md:hidden"
          onClick={onCloseMobile}
        />
      )}

      <aside
        className={`fixed top-0 bottom-0 left-0 z-50 flex w-72 flex-col border-r border-slate-200 bg-white shadow-sm transition-transform duration-200 ease-in-out md:static md:translate-x-0 shrink-0 ${
          isOpenMobile ? 'translate-x-0' : '-translate-x-full'
        }`}
      >
        {/* Sleek Brand Title */}
        <div className="border-b border-slate-100 p-5 flex items-center justify-between">
          <div>
            <div className="flex items-center gap-2.5 mb-1">
              <div className="flex h-8 w-8 items-center justify-center rounded-lg bg-blue-600 text-white shadow-xs shrink-0">
                <ShieldCheck className="h-4 w-4" />
              </div>
              <span className="font-bold text-base tracking-tight text-slate-900 leading-tight">
                Disease Models
              </span>
            </div>
            <p className="text-[10px] text-slate-400 uppercase tracking-widest font-bold">
              Diagnostics Suite
            </p>
          </div>

          <button
            type="button"
            onClick={onCloseMobile}
            className="rounded-lg p-1.5 text-slate-400 hover:bg-slate-100 hover:text-slate-700 md:hidden"
            title="Close Menu"
          >
            <X className="h-5 w-5" />
          </button>
        </div>

        {/* Option Menu Navigation */}
        <div className="flex-1 overflow-y-auto p-4 space-y-6">
          <div>
            <div className="px-3 pb-2 text-[10px] font-bold uppercase tracking-wider text-slate-400">
              Clinical Disease Models
            </div>
            <div className="space-y-1.5">
              {menuItems.map((item) => {
                const Icon = item.icon;
                const isActive = currentTab === item.id;
                return (
                  <button
                    key={item.id}
                    id={`nav-item-${item.id}`}
                    type="button"
                    onClick={() => handleSelect(item.id)}
                    className={`group flex w-full items-center justify-between rounded-xl p-3 text-left text-sm font-medium transition-all ${
                      isActive
                        ? 'bg-blue-50 text-blue-700 shadow-xs'
                        : 'text-slate-500 hover:bg-slate-50 hover:text-slate-800'
                    }`}
                  >
                    <div className="flex items-center gap-3">
                      <Icon
                        className={`h-4 w-4 shrink-0 transition-transform ${
                          isActive ? 'text-blue-600' : 'text-slate-400 group-hover:text-slate-600'
                        }`}
                      />
                      <div>
                        <div className="font-semibold leading-tight">{item.label}</div>
                        <div
                          className={`text-[11px] font-normal line-clamp-1 ${
                            isActive ? 'text-blue-600/80' : 'text-slate-400'
                          }`}
                        >
                          {item.desc}
                        </div>
                      </div>
                    </div>
                    <span
                      className={`ml-2 rounded-md px-1.5 py-0.5 text-[10px] font-bold ${
                        isActive
                          ? 'bg-blue-100 text-blue-800'
                          : 'bg-slate-100 text-slate-500'
                      }`}
                    >
                      {item.tag}
                    </span>
                  </button>
                );
              })}
            </div>
          </div>
        </div>

        {/* Footer */}
      </aside>
    </>
  );
}
