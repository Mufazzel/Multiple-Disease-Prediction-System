import { useState } from 'react';
import { DiseaseType } from './types';
import { StreamlitHeader } from './components/StreamlitHeader';
import { Sidebar } from './components/Sidebar';
import { DiabetesPredictor } from './components/DiabetesPredictor';
import { HeartDiseasePredictor } from './components/HeartDiseasePredictor';
import { ParkinsonsPredictor } from './components/ParkinsonsPredictor';

export default function App() {
  const [currentTab, setCurrentTab] = useState<DiseaseType>('diabetes');
  const [isSidebarOpenMobile, setIsSidebarOpenMobile] = useState<boolean>(false);

  return (
    <div className="flex h-screen w-screen flex-col overflow-hidden bg-slate-50 font-sans text-slate-800 antialiased selection:bg-blue-600 selection:text-white">
      {/* Fixed Navigation Header */}
      <StreamlitHeader
        onToggleSidebar={() => setIsSidebarOpenMobile((prev) => !prev)}
        isSidebarOpen={isSidebarOpenMobile}
      />

      <div className="flex flex-1 overflow-hidden relative">
        {/* Navigation Sidebar */}
        <Sidebar
          currentTab={currentTab}
          onSelectTab={(tab) => setCurrentTab(tab)}
          isOpenMobile={isSidebarOpenMobile}
          onCloseMobile={() => setIsSidebarOpenMobile(false)}
        />

        {/* Main Content Viewport */}
        <main className="flex-1 overflow-y-auto p-4 sm:p-6 lg:p-8">
          <div className="mx-auto max-w-6xl pb-16">
            {currentTab === 'diabetes' && <DiabetesPredictor />}
            {currentTab === 'heart' && <HeartDiseasePredictor />}
            {currentTab === 'parkinsons' && <ParkinsonsPredictor />}
          </div>
        </main>
      </div>
    </div>
  );
}
