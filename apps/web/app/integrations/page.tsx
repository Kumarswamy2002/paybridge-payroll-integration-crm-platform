'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { Cpu, CheckCircle2, AlertTriangle, RefreshCw, Settings, ShieldCheck, ArrowUpRight } from 'lucide-react';

const adapters = [
  { id: 'gusto', name: 'Gusto Payroll', category: 'US Payroll Provider', status: 'ACTIVE', lastSync: '10 mins ago', recordsSynced: '420 Employees', apiVersion: 'v2.1' },
  { id: 'adp', name: 'ADP Workforce Now', category: 'Enterprise Payroll', status: 'ACTIVE', lastSync: '1 hour ago', recordsSynced: '810 Employees', apiVersion: 'v1.4' },
  { id: 'rippling', name: 'Rippling Global', category: 'Payroll & HRIS', status: 'DEGRADED', lastSync: '2 hours ago', recordsSynced: '150 Employees', apiVersion: 'v3.0' },
  { id: 'workday', name: 'Workday HCM', category: 'Enterprise HR & Payroll', status: 'ACTIVE', lastSync: '30 mins ago', recordsSynced: '650 Employees', apiVersion: 'v38.0' },
];

export default function IntegrationsPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Payroll Integration Hub & Adapters" />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          {/* Banner */}
          <div className="glass-card rounded-2xl p-6 border border-slate-800 flex items-center justify-between">
            <div>
              <h2 className="text-lg font-bold text-slate-100">Payroll Provider Adapter Marketplace</h2>
              <p className="text-xs text-slate-400 mt-1">Provider Adapter Framework decouples external API schemas from PayBridge CRM core</p>
            </div>
            <button className="px-4 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold shadow-md shadow-sky-950 transition-colors">
              + Connect New Payroll Provider
            </button>
          </div>

          {/* Adapter Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {adapters.map((adapter) => (
              <div key={adapter.id} className="glass-card rounded-2xl p-6 border border-slate-800 space-y-4">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-xl bg-slate-800 flex items-center justify-center font-bold text-sky-400 border border-slate-700">
                      <Cpu className="w-5 h-5" />
                    </div>
                    <div>
                      <h4 className="text-sm font-bold text-slate-100">{adapter.name}</h4>
                      <p className="text-xs text-slate-400">{adapter.category}</p>
                    </div>
                  </div>
                  <span className={`px-2.5 py-1 rounded-full text-[10px] font-bold border ${
                    adapter.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border-amber-500/30'
                  }`}>
                    {adapter.status}
                  </span>
                </div>

                <div className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 grid grid-cols-3 gap-2 text-xs">
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block font-semibold">Records Synced</span>
                    <span className="font-semibold text-slate-200">{adapter.recordsSynced}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block font-semibold">Last Sync</span>
                    <span className="font-semibold text-slate-200">{adapter.lastSync}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block font-semibold">API Contract</span>
                    <span className="font-mono text-sky-400">{adapter.apiVersion}</span>
                  </div>
                </div>

                <div className="flex items-center justify-between text-xs pt-2">
                  <button className="text-slate-400 hover:text-slate-200 flex items-center gap-1 font-semibold">
                    <Settings className="w-3.5 h-3.5" /> Configure Field Mappings
                  </button>
                  <button className="text-sky-400 hover:text-sky-300 flex items-center gap-1 font-semibold">
                    Test Connection <ArrowUpRight className="w-3.5 h-3.5" />
                  </button>
                </div>
              </div>
            ))}
          </div>
        </main>
      </div>
    </div>
  );
}
