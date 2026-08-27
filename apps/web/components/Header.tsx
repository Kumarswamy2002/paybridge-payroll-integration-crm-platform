'use client';

import React from 'react';
import { Bell, Search, UserCircle, RefreshCw } from 'lucide-react';

export function Header({ title = 'Dashboard' }: { title?: string }) {
  return (
    <header className="h-16 glass-panel border-b border-slate-800/80 px-8 flex items-center justify-between sticky top-0 z-30">
      <div className="flex items-center gap-4">
        <h2 className="text-xl font-bold text-slate-100 tracking-tight">{title}</h2>
        <span className="hidden md:inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
          <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
          System Live
        </span>
      </div>

      <div className="flex items-center gap-4">
        {/* Global Search Input */}
        <div className="relative w-64 hidden sm:block">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search employees, cases..."
            className="w-full bg-slate-900/80 border border-slate-700/60 rounded-lg pl-9 pr-4 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-sky-500 transition-colors"
          />
        </div>

        {/* Sync Status Action Button */}
        <button 
          onClick={() => alert("Sync triggered across all active payroll providers!")}
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-medium border border-slate-700 transition-all active:scale-95"
        >
          <RefreshCw className="w-3.5 h-3.5 text-sky-400" />
          Sync All Providers
        </button>

        {/* Notifications */}
        <button className="p-2 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 relative">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1 right-1 w-2 h-2 rounded-full bg-sky-500"></span>
        </button>

        {/* User Avatar */}
        <div className="flex items-center gap-3 border-l border-slate-800 pl-4">
          <div className="w-8 h-8 rounded-full bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center font-bold text-xs text-white">
            HR
          </div>
          <div className="hidden lg:block text-left">
            <p className="text-xs font-semibold text-slate-200">Alex Mercer</p>
            <p className="text-[10px] text-slate-400">HR Administrator</p>
          </div>
        </div>
      </div>
    </header>
  );
}
