'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { mockCases } from '@/lib/mockData';
import { Ticket, Plus, Filter, AlertCircle, Clock, CheckCircle, ArrowUpRight } from 'lucide-react';

export default function CasesPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Payroll Case & Exception Management" />

        <main className="p-8 space-y-6 flex-1 overflow-y-auto">
          {/* Header Controls */}
          <div className="flex items-center justify-between">
            <div>
              <h2 className="text-lg font-bold text-slate-100">Payroll CRM Exception Tickets</h2>
              <p className="text-xs text-slate-400">Structured resolution pipeline for payroll mismatches, tax queries, and sync errors</p>
            </div>
            <button className="flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-sky-600 to-indigo-600 text-white text-xs font-bold shadow-lg shadow-sky-950 transition-all">
              <Plus className="w-4 h-4" /> Create New Case
            </button>
          </div>

          {/* Case Lifecycle Columns */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {['OPEN / TRIAGED', 'INVESTIGATING', 'RESOLVED / CLOSED'].map((stage, idx) => {
              const stageCases = mockCases.filter(c => {
                if (idx === 0) return c.status === 'OPEN';
                if (idx === 1) return c.status === 'INVESTIGATING';
                return c.status === 'RESOLVED';
              });

              return (
                <div key={stage} className="glass-card rounded-xl p-5 border border-slate-800 flex flex-col justify-between">
                  <div>
                    <div className="flex items-center justify-between mb-4 border-b border-slate-800 pb-3">
                      <span className="text-xs font-bold text-slate-300 tracking-wider">{stage}</span>
                      <span className="px-2 py-0.5 rounded-full text-[10px] font-bold bg-slate-800 text-slate-300">
                        {stageCases.length}
                      </span>
                    </div>

                    <div className="space-y-4">
                      {stageCases.map((c) => (
                        <div key={c.id} className="bg-slate-900/80 p-4 rounded-xl border border-slate-800 hover:border-slate-700 transition-all space-y-2">
                          <div className="flex items-center justify-between">
                            <span className="text-[10px] font-mono font-bold text-sky-400">{c.ticketNumber}</span>
                            <span className={`text-[9px] font-bold px-2 py-0.5 rounded ${
                              c.priority === 'URGENT' ? 'bg-red-500/20 text-red-400 border border-red-500/30' :
                              c.priority === 'HIGH' ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30' : 'bg-slate-800 text-slate-400'
                            }`}>
                              {c.priority}
                            </span>
                          </div>
                          <h4 className="text-xs font-bold text-slate-100">{c.title}</h4>
                          <p className="text-[11px] text-slate-400">Employee: <strong className="text-slate-300">{c.employeeName}</strong></p>
                          <div className="pt-2 border-t border-slate-800/80 flex items-center justify-between text-[10px] text-slate-500">
                            <span>Assignee: {c.assignedTo}</span>
                            <span>{c.createdAt}</span>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </main>
      </div>
    </div>
  );
}
