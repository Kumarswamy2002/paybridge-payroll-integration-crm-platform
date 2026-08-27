'use client';

import React, { useState } from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { mockEmployees, mockTimelineEvents, mockCases } from '@/lib/mockData';
import { ArrowLeft, DollarSign, Cpu, Ticket, History, Shield, Mail, Phone, MapPin, Building, Calendar, Edit3, CheckCircle2 } from 'lucide-react';
import Link from 'next/link';

export default function Employee360Page({ params }: { params: { id: string } }) {
  const [activeTab, setActiveTab] = useState<'OVERVIEW' | 'COMPENSATION' | 'PAYROLL' | 'TIMELINE' | 'CASES'>('OVERVIEW');

  const emp = mockEmployees.find(e => e.id === params.id) || mockEmployees[0];

  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title={`Employee 360 — ${emp.firstName} ${emp.lastName}`} />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          {/* Top Breadcrumb & Actions */}
          <div className="flex items-center justify-between">
            <Link href="/employees" className="flex items-center gap-2 text-xs font-semibold text-slate-400 hover:text-slate-200 transition-colors">
              <ArrowLeft className="w-4 h-4" /> Back to Employee CRM Directory
            </Link>
            <div className="flex gap-3">
              <button 
                onClick={() => alert("Open Case modal triggered!")}
                className="px-3.5 py-2 rounded-xl bg-amber-500/20 text-amber-300 border border-amber-500/30 text-xs font-bold hover:bg-amber-500/30 transition-colors"
              >
                + Open Payroll Case
              </button>
              <button 
                onClick={() => alert("Sync Employee profile with external payroll provider!")}
                className="px-3.5 py-2 rounded-xl bg-sky-600 hover:bg-sky-500 text-white text-xs font-bold transition-all shadow-md shadow-sky-950"
              >
                Trigger Provider Sync
              </button>
            </div>
          </div>

          {/* Profile Spotlight Banner */}
          <div className="glass-card rounded-2xl p-6 border border-slate-800 relative overflow-hidden">
            <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
              <div className="flex items-center gap-5">
                <div className="w-16 h-16 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center text-2xl font-bold text-white shadow-lg shadow-sky-950">
                  {emp.firstName[0]}{emp.lastName[0]}
                </div>
                <div>
                  <div className="flex items-center gap-3">
                    <h2 className="text-xl font-bold text-slate-100">{emp.firstName} {emp.lastName}</h2>
                    <span className="px-2.5 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                      {emp.status}
                    </span>
                  </div>
                  <p className="text-xs text-slate-400 mt-0.5">{emp.position} • <span className="text-sky-400">{emp.department}</span></p>
                  <p className="text-[11px] text-slate-500 font-mono mt-1">ID: {emp.code} | Manager: {emp.manager}</p>
                </div>
              </div>

              {/* Quick Payroll Snapshot */}
              <div className="flex items-center gap-6 bg-slate-900/80 p-4 rounded-xl border border-slate-800/80 text-xs">
                <div>
                  <span className="text-slate-500 text-[10px] uppercase font-semibold block">Payroll Provider</span>
                  <span className="font-bold text-slate-200">{emp.payrollProvider}</span>
                </div>
                <div className="border-l border-slate-800 pl-6">
                  <span className="text-slate-500 text-[10px] uppercase font-semibold block">Base Compensation</span>
                  <span className="font-mono font-bold text-emerald-400 text-sm">${emp.baseSalary.toLocaleString()}</span>
                </div>
                <div className="border-l border-slate-800 pl-6">
                  <span className="text-slate-500 text-[10px] uppercase font-semibold block">Sync Status</span>
                  <span className="font-semibold text-emerald-400 flex items-center gap-1">
                    <CheckCircle2 className="w-3.5 h-3.5" /> {emp.syncStatus}
                  </span>
                </div>
              </div>
            </div>

            {/* Tabs Bar */}
            <div className="flex items-center gap-2 mt-8 pt-4 border-t border-slate-800/80 overflow-x-auto">
              {[
                { id: 'OVERVIEW', label: 'Employee 360 Overview' },
                { id: 'COMPENSATION', label: 'Compensation & Benefits' },
                { id: 'PAYROLL', label: 'Payroll Provider Profile' },
                { id: 'TIMELINE', label: 'Unified CRM Timeline' },
                { id: 'CASES', label: `Payroll Cases (${emp.openCasesCount})` },
              ].map(tab => (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id as any)}
                  className={`px-4 py-2 rounded-lg text-xs font-semibold whitespace-nowrap transition-colors ${
                    activeTab === tab.id
                      ? 'bg-sky-600/30 text-sky-300 border border-sky-500/30'
                      : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
                  }`}
                >
                  {tab.label}
                </button>
              ))}
            </div>
          </div>

          {/* Tab Content Panels */}
          {activeTab === 'OVERVIEW' && (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              {/* Contact & Personal Details */}
              <div className="glass-card rounded-xl p-6 border border-slate-800 space-y-4">
                <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wider text-sky-400">Personal & Identity Info</h3>
                <div className="space-y-3 text-xs">
                  <div className="flex items-center gap-3 text-slate-300">
                    <Mail className="w-4 h-4 text-slate-500" />
                    <span>{emp.email}</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-300">
                    <Phone className="w-4 h-4 text-slate-500" />
                    <span>{emp.phone}</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-300">
                    <MapPin className="w-4 h-4 text-slate-500" />
                    <span>{emp.location}</span>
                  </div>
                  <div className="flex items-center gap-3 text-slate-300">
                    <Calendar className="w-4 h-4 text-slate-500" />
                    <span>Joined: {emp.joiningDate}</span>
                  </div>
                </div>
              </div>

              {/* Organization & Manager Relationship */}
              <div className="glass-card rounded-xl p-6 border border-slate-800 space-y-4">
                <h3 className="text-sm font-bold text-slate-100 uppercase tracking-wider text-sky-400">Organization Hierarchy</h3>
                <div className="space-y-3 text-xs">
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block">Department</span>
                    <span className="font-semibold text-slate-200 text-sm">{emp.department}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block">Manager (Reports To)</span>
                    <span className="font-semibold text-slate-200">{emp.manager}</span>
                  </div>
                  <div>
                    <span className="text-slate-500 text-[10px] uppercase block">Employment Type</span>
                    <span className="font-semibold text-slate-200">{emp.employmentType}</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {activeTab === 'TIMELINE' && (
            <div className="glass-card rounded-xl p-6 border border-slate-800 space-y-6">
              <h3 className="text-base font-bold text-slate-100">Relationship & Audit Timeline</h3>
              <div className="space-y-6">
                {mockTimelineEvents.map((evt) => (
                  <div key={evt.id} className="relative pl-6 border-l-2 border-slate-800">
                    <span className="absolute -left-[7px] top-0 w-3 h-3 rounded-full bg-sky-500 border-2 border-slate-900"></span>
                    <span className={`inline-block px-2 py-0.5 rounded text-[9px] font-bold tracking-wider uppercase border mb-1 ${evt.badgeColor}`}>
                      {evt.type}
                    </span>
                    <p className="text-xs font-semibold text-slate-200">{evt.summary}</p>
                    <div className="mt-1 flex items-center justify-between text-[10px] text-slate-500">
                      <span>{evt.actor}</span>
                      <span>{evt.date}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </main>
      </div>
    </div>
  );
}
