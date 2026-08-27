'use client';

import React, { useState } from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { mockEmployees, Employee360Data } from '@/lib/mockData';
import { Search, Plus, Filter, ExternalLink, ShieldAlert, CheckCircle2 } from 'lucide-react';
import Link from 'next/link';

export default function EmployeesDirectoryPage() {
  const [searchTerm, setSearchTerm] = useState('');

  const filteredEmployees = mockEmployees.filter(emp => 
    `${emp.firstName} ${emp.lastName}`.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.department.toLowerCase().includes(searchTerm.toLowerCase()) ||
    emp.code.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Employee CRM Directory" />

        <main className="p-8 space-y-6 flex-1 overflow-y-auto">
          {/* Controls header */}
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="relative w-full sm:w-80">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
              <input
                type="text"
                placeholder="Search by name, email, department..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="w-full bg-slate-900 border border-slate-700/80 rounded-xl pl-9 pr-4 py-2 text-xs text-slate-200 focus:outline-none focus:border-sky-500 transition-colors"
              />
            </div>

            <div className="flex items-center gap-3 w-full sm:w-auto justify-end">
              <button className="flex items-center gap-2 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors">
                <Filter className="w-3.5 h-3.5" /> Filter Status
              </button>
              <button 
                onClick={() => alert("Add Employee Modal — Integrated with FastAPI /api/v1/employees endpoint!")}
                className="flex items-center gap-2 px-4 py-2 rounded-xl bg-gradient-to-r from-sky-600 to-indigo-600 hover:from-sky-500 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-sky-950 transition-all active:scale-95"
              >
                <Plus className="w-4 h-4" /> Add Employee
              </button>
            </div>
          </div>

          {/* Cards Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-2 gap-6">
            {filteredEmployees.map((emp) => (
              <div key={emp.id} className="glass-card rounded-2xl p-6 border border-slate-800 hover:border-slate-700 transition-all duration-300 flex flex-col justify-between">
                <div>
                  <div className="flex items-start justify-between">
                    <div className="flex items-center gap-4">
                      <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center text-base font-bold text-white shadow-md shadow-sky-950">
                        {emp.firstName[0]}{emp.lastName[0]}
                      </div>
                      <div>
                        <h4 className="text-base font-bold text-slate-100">{emp.firstName} {emp.lastName}</h4>
                        <p className="text-xs text-slate-400">{emp.position}</p>
                        <p className="text-[11px] text-sky-400 font-mono mt-0.5">{emp.code} • {emp.department}</p>
                      </div>
                    </div>
                    <span className={`px-2.5 py-1 rounded-full text-[10px] font-bold border ${
                      emp.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400 border-emerald-500/30' : 'bg-amber-500/20 text-amber-400 border-amber-500/30'
                    }`}>
                      {emp.status}
                    </span>
                  </div>

                  <div className="mt-6 grid grid-cols-2 gap-4 bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 text-xs">
                    <div>
                      <span className="text-slate-500 text-[10px] uppercase font-semibold block">Payroll Provider</span>
                      <span className="font-semibold text-slate-200">{emp.payrollProvider}</span>
                    </div>
                    <div>
                      <span className="text-slate-500 text-[10px] uppercase font-semibold block">Base Salary</span>
                      <span className="font-mono font-bold text-emerald-400">${emp.baseSalary.toLocaleString()} / yr</span>
                    </div>
                    <div>
                      <span className="text-slate-500 text-[10px] uppercase font-semibold block">Sync Status</span>
                      <span className="font-semibold text-slate-300">{emp.syncStatus}</span>
                    </div>
                    <div>
                      <span className="text-slate-500 text-[10px] uppercase font-semibold block">Open CRM Tickets</span>
                      <span className={`font-semibold ${emp.openCasesCount > 0 ? 'text-amber-400' : 'text-slate-400'}`}>
                        {emp.openCasesCount} active ticket(s)
                      </span>
                    </div>
                  </div>
                </div>

                <div className="mt-6 pt-4 border-t border-slate-800/80 flex items-center justify-between">
                  <span className="text-[11px] text-slate-500">Joined: {emp.joiningDate}</span>
                  <Link 
                    href={`/employees/${emp.id}`}
                    className="flex items-center gap-1.5 text-xs font-bold text-sky-400 hover:text-sky-300 transition-colors"
                  >
                    Open Payroll 360 View <ExternalLink className="w-3.5 h-3.5" />
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </main>
      </div>
    </div>
  );
}
