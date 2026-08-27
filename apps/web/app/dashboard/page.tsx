'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { StatsCard } from '@/components/StatsCard';
import { mockEmployees, mockCases, mockTimelineEvents } from '@/lib/mockData';
import { Users, DollarSign, Ticket, Cpu, ArrowUpRight, CheckCircle2, AlertTriangle, ShieldCheck } from 'lucide-react';
import Link from 'next/link';

export default function DashboardPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Payroll CRM Dashboard" />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          {/* Executive Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <StatsCard
              title="Total Active Employees"
              value={mockEmployees.length}
              change="12%"
              isPositive={true}
              icon={Users}
              color="sky"
            />
            <StatsCard
              title="Monthly Payroll Commitment"
              value="$588,000"
              change="4.2%"
              isPositive={true}
              icon={DollarSign}
              color="emerald"
            />
            <StatsCard
              title="Open Payroll Cases"
              value={mockCases.length}
              change="1 case resolved today"
              isPositive={true}
              icon={Ticket}
              color="amber"
            />
            <StatsCard
              title="Connected Providers"
              value="4 / 4 Active"
              change="100% Sync Health"
              isPositive={true}
              icon={Cpu}
              color="indigo"
            />
          </div>

          {/* Provider Integration Health Strip */}
          <div className="glass-card rounded-xl p-6 border border-slate-800">
            <div className="flex items-center justify-between mb-4">
              <div>
                <h3 className="text-base font-bold text-slate-100">Payroll Provider Integrations</h3>
                <p className="text-xs text-slate-400">Real-time status of connected payroll adapters and synchronization pipelines</p>
              </div>
              <Link href="/integrations" className="text-xs font-semibold text-sky-400 hover:underline flex items-center gap-1">
                View All Adapters <ArrowUpRight className="w-3.5 h-3.5" />
              </Link>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {[
                { name: 'Gusto Adapter', status: 'CONNECTED', syncRate: '100%', latency: '240ms', color: 'emerald' },
                { name: 'ADP Workforce', status: 'CONNECTED', syncRate: '99.8%', latency: '310ms', color: 'emerald' },
                { name: 'Rippling Adapter', status: 'DEGRADED', syncRate: '94.2%', latency: '850ms', color: 'amber' },
                { name: 'Workday Sync', status: 'CONNECTED', syncRate: '100%', latency: '410ms', color: 'emerald' },
              ].map((provider) => (
                <div key={provider.name} className="bg-slate-900/60 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">
                  <div className="flex items-center justify-between">
                    <span className="text-sm font-semibold text-slate-200">{provider.name}</span>
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                      provider.color === 'emerald' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                    }`}>
                      {provider.status}
                    </span>
                  </div>
                  <div className="mt-3 flex items-center justify-between text-xs text-slate-400">
                    <span>Sync Rate: <strong className="text-slate-200">{provider.syncRate}</strong></span>
                    <span>Latency: <strong className="text-slate-200">{provider.latency}</strong></span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Two-Column Grid: Employee Directory & Recent CRM Cases */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            {/* Left 2 Cols: Employee 360 Spotlight */}
            <div className="lg:col-span-2 glass-card rounded-xl p-6 border border-slate-800">
              <div className="flex items-center justify-between mb-6">
                <div>
                  <h3 className="text-base font-bold text-slate-100">Employee Payroll CRM Directory</h3>
                  <p className="text-xs text-slate-400">Centralized view linking identity, compensation, provider profiles, and cases</p>
                </div>
                <Link href="/employees" className="px-3 py-1.5 rounded-lg bg-sky-600 hover:bg-sky-500 text-white text-xs font-semibold shadow-md shadow-sky-950 transition-colors">
                  View Employee 360 →
                </Link>
              </div>

              <div className="overflow-x-auto">
                <table className="w-full text-left text-xs text-slate-300">
                  <thead className="bg-slate-900/80 text-slate-400 uppercase font-semibold text-[10px] tracking-wider border-b border-slate-800">
                    <tr>
                      <th className="py-3 px-4">Employee</th>
                      <th className="py-3 px-4">Department</th>
                      <th className="py-3 px-4">Provider</th>
                      <th className="py-3 px-4">Base Salary</th>
                      <th className="py-3 px-4">Sync Status</th>
                      <th className="py-3 px-4 text-right">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60">
                    {mockEmployees.map((emp) => (
                      <tr key={emp.id} className="hover:bg-slate-800/40 transition-colors">
                        <td className="py-3 px-4">
                          <div className="font-semibold text-slate-100">{emp.firstName} {emp.lastName}</div>
                          <div className="text-[10px] text-slate-400">{emp.email}</div>
                        </td>
                        <td className="py-3 px-4 text-slate-300">{emp.department}</td>
                        <td className="py-3 px-4 text-slate-300">{emp.payrollProvider}</td>
                        <td className="py-3 px-4 font-mono font-semibold text-slate-200">${emp.baseSalary.toLocaleString()}</td>
                        <td className="py-3 px-4">
                          <span className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold ${
                            emp.syncStatus === 'IN_SYNC' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                          }`}>
                            <span className={`w-1.5 h-1.5 rounded-full ${emp.syncStatus === 'IN_SYNC' ? 'bg-emerald-400' : 'bg-amber-400'}`}></span>
                            {emp.syncStatus}
                          </span>
                        </td>
                        <td className="py-3 px-4 text-right">
                          <Link href={`/employees/${emp.id}`} className="text-sky-400 hover:text-sky-300 font-semibold text-xs">
                            360 Profile →
                          </Link>
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>

            {/* Right Column: Unified Activity Timeline */}
            <div className="glass-card rounded-xl p-6 border border-slate-800 flex flex-col">
              <h3 className="text-base font-bold text-slate-100 mb-1">Unified CRM Timeline</h3>
              <p className="text-xs text-slate-400 mb-6">Real-time audit log of payroll activities, updates, and cases</p>

              <div className="space-y-6 flex-1 overflow-y-auto pr-2">
                {mockTimelineEvents.map((evt) => (
                  <div key={evt.id} className="relative pl-6 border-l-2 border-slate-800">
                    <span className="absolute -left-[7px] top-0 w-3 h-3 rounded-full bg-sky-500 border-2 border-slate-900"></span>
                    <span className={`inline-block px-2 py-0.5 rounded text-[9px] font-bold tracking-wider uppercase border mb-1 ${evt.badgeColor}`}>
                      {evt.type}
                    </span>
                    <p className="text-xs font-medium text-slate-200 leading-snug">{evt.summary}</p>
                    <div className="mt-1 flex items-center justify-between text-[10px] text-slate-500">
                      <span>{evt.actor}</span>
                      <span>{evt.date}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
