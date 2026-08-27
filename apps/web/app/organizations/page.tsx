'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { Building2, Users, Network, Plus } from 'lucide-react';

export default function OrganizationsPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Organization Structure & Hierarchy" />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          <div className="glass-card rounded-2xl p-6 border border-slate-800 flex items-center justify-between">
            <div>
              <h2 className="text-lg font-bold text-slate-100">Departments & Business Units</h2>
              <p className="text-xs text-slate-400 mt-1">Hierarchical organization modeling linked to cost centers and job positions</p>
            </div>
            <button className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold shadow-md shadow-sky-950 transition-colors">
              + Add Department
            </button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {[
              { name: 'Engineering & Platform', head: 'Sarah Connor', count: 42, code: 'DEPT-ENG', budget: '$4,200,000' },
              { name: 'Operations & Security', head: 'John Reese', count: 18, code: 'DEPT-OPS', budget: '$2,100,000' },
              { name: 'Finance & Payroll', head: 'Elena Rostova', count: 12, code: 'DEPT-FIN', budget: '$1,400,000' },
            ].map(dept => (
              <div key={dept.code} className="glass-card rounded-xl p-6 border border-slate-800 space-y-4">
                <div className="flex items-center justify-between">
                  <h4 className="text-sm font-bold text-slate-100">{dept.name}</h4>
                  <span className="text-[10px] font-mono bg-sky-500/20 text-sky-400 px-2 py-0.5 rounded border border-sky-500/30">
                    {dept.code}
                  </span>
                </div>
                <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 space-y-2 text-xs">
                  <div className="flex justify-between text-slate-400">
                    <span>Department Head:</span>
                    <strong className="text-slate-200">{dept.head}</strong>
                  </div>
                  <div className="flex justify-between text-slate-400">
                    <span>Total Employees:</span>
                    <strong className="text-slate-200">{dept.count} Members</strong>
                  </div>
                  <div className="flex justify-between text-slate-400">
                    <span>Annual Budget:</span>
                    <strong className="text-emerald-400 font-mono">{dept.budget}</strong>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </main>
      </div>
    </div>
  );
}
