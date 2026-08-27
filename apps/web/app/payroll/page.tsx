'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { mockEmployees } from '@/lib/mockData';
import { DollarSign, RefreshCw, CheckCircle2, AlertOctagon, Cpu, ShieldCheck } from 'lucide-react';

export default function PayrollProfilesPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Payroll Profiles & Reconciliation" />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          {/* Top Banner */}
          <div className="glass-card rounded-2xl p-6 border border-slate-800 flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
            <div>
              <h2 className="text-lg font-bold text-slate-100">Payroll Integration & Reconciliation Engine</h2>
              <p className="text-xs text-slate-400 mt-1">Converts external provider schemas (Gusto, ADP, Rippling, Workday) into the PayBridge Canonical Model</p>
            </div>
            <button className="flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-500 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-sky-950 transition-all">
              <RefreshCw className="w-3.5 h-3.5" /> Trigger Full Reconciliation Run
            </button>
          </div>

          {/* Reconciliation Stats */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="glass-card rounded-xl p-5 border border-slate-800">
              <span className="text-xs font-semibold text-slate-400 uppercase">Synchronized Profiles</span>
              <div className="text-2xl font-bold text-emerald-400 mt-2">1,240 / 1,244</div>
              <p className="text-[11px] text-slate-500 mt-1">99.7% synchronization success rate</p>
            </div>

            <div className="glass-card rounded-xl p-5 border border-slate-800">
              <span className="text-xs font-semibold text-slate-400 uppercase">Detected Discrepancies</span>
              <div className="text-2xl font-bold text-amber-400 mt-2">4 Mismatches</div>
              <p className="text-[11px] text-slate-500 mt-1">Auto-converted into CRM Exception Tickets</p>
            </div>

            <div className="glass-card rounded-xl p-5 border border-slate-800">
              <span className="text-xs font-semibold text-slate-400 uppercase">Active Canonical Mappings</span>
              <div className="text-2xl font-bold text-sky-400 mt-2">12 Rule Sets</div>
              <p className="text-[11px] text-slate-500 mt-1">Gusto v2, ADP US, Rippling Core, Workday API</p>
            </div>
          </div>

          {/* Payroll Profiles Table */}
          <div className="glass-card rounded-xl p-6 border border-slate-800">
            <h3 className="text-base font-bold text-slate-100 mb-4">Active Payroll Profiles</h3>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-xs text-slate-300">
                <thead className="bg-slate-900/80 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
                  <tr>
                    <th className="py-3 px-4">Employee</th>
                    <th className="py-3 px-4">Payroll Provider</th>
                    <th className="py-3 px-4">External Provider ID</th>
                    <th className="py-3 px-4">Payment Method</th>
                    <th className="py-3 px-4">Base Salary</th>
                    <th className="py-3 px-4">Sync Status</th>
                    <th className="py-3 px-4">Last Synced</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-800/60">
                  {mockEmployees.map((emp) => (
                    <tr key={emp.id} className="hover:bg-slate-800/40 transition-colors">
                      <td className="py-3 px-4 font-semibold text-slate-100">{emp.firstName} {emp.lastName}</td>
                      <td className="py-3 px-4 font-medium text-slate-200">{emp.payrollProvider}</td>
                      <td className="py-3 px-4 font-mono text-slate-400">{emp.code}-PROV</td>
                      <td className="py-3 px-4 text-slate-300">Direct Deposit</td>
                      <td className="py-3 px-4 font-mono font-bold text-emerald-400">${emp.baseSalary.toLocaleString()}</td>
                      <td className="py-3 px-4">
                        <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[10px] font-bold ${
                          emp.syncStatus === 'IN_SYNC' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                        }`}>
                          {emp.syncStatus}
                        </span>
                      </td>
                      <td className="py-3 px-4 text-slate-400">{emp.lastSynced}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
