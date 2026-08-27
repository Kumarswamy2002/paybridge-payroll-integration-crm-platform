'use client';

import React from 'react';
import { Sidebar } from '@/components/Sidebar';
import { Header } from '@/components/Header';
import { Settings, ShieldCheck, Key, Lock, Database } from 'lucide-react';

export default function SettingsPage() {
  return (
    <div className="flex min-h-screen bg-[#0b0f19]">
      <Sidebar />
      <div className="flex-1 flex flex-col min-w-0">
        <Header title="Tenant Settings & Security" />

        <main className="p-8 space-y-8 flex-1 overflow-y-auto">
          <div className="glass-card rounded-2xl p-6 border border-slate-800 space-y-6">
            <div>
              <h2 className="text-lg font-bold text-slate-100">Multi-Tenant Governance & Security</h2>
              <p className="text-xs text-slate-400 mt-1">Tenant isolation policies, AES-256 PII encryption configurations, and RBAC roles</p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 pt-4 border-t border-slate-800">
              <div className="bg-slate-900/60 p-5 rounded-xl border border-slate-800 space-y-3">
                <div className="flex items-center gap-3">
                  <ShieldCheck className="w-5 h-5 text-emerald-400" />
                  <h4 className="text-sm font-bold text-slate-200">Tenant Context Isolation</h4>
                </div>
                <p className="text-xs text-slate-400">Strict database level isolation with enforced tenant_id query scoping on all models.</p>
                <span className="inline-block px-2.5 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">
                  ENFORCED & ACTIVE
                </span>
              </div>

              <div className="bg-slate-900/60 p-5 rounded-xl border border-slate-800 space-y-3">
                <div className="flex items-center gap-3">
                  <Lock className="w-5 h-5 text-sky-400" />
                  <h4 className="text-sm font-bold text-slate-200">PII AES-256 Encryption</h4>
                </div>
                <p className="text-xs text-slate-400">Tax identifiers (SSN/PAN) and direct deposit bank accounts encrypted at rest.</p>
                <span className="inline-block px-2.5 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-400 border border-sky-500/30">
                  AES-256 GCM ENABLED
                </span>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}
