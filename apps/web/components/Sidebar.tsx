'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { 
  Users, 
  LayoutDashboard, 
  DollarSign, 
  Ticket, 
  Cpu, 
  Building2, 
  Settings, 
  ShieldCheck,
  Zap
} from 'lucide-react';

const navigation = [
  { name: 'Dashboard', href: '/dashboard', icon: LayoutDashboard },
  { name: 'Employee CRM (360°)', href: '/employees', icon: Users },
  { name: 'Payroll & Profiles', href: '/payroll', icon: DollarSign },
  { name: 'Cases & Exceptions', href: '/cases', icon: Ticket },
  { name: 'Integration Hub', href: '/integrations', icon: Cpu },
  { name: 'Organization', href: '/organizations', icon: Building2 },
  { name: 'Tenant Settings', href: '/settings', icon: Settings },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <aside className="w-64 glass-panel border-r border-slate-800/80 flex flex-col justify-between h-screen sticky top-0 z-40">
      <div>
        {/* Brand Header */}
        <div className="h-16 flex items-center px-6 border-b border-slate-800/80 gap-3">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center shadow-lg shadow-sky-500/20">
            <Zap className="w-5 h-5 text-white" />
          </div>
          <div>
            <h1 className="font-bold text-lg text-white tracking-wide leading-none">PayBridge</h1>
            <span className="text-[10px] text-sky-400 font-mono tracking-widest uppercase">Payroll CRM</span>
          </div>
        </div>

        {/* Tenant Selector Pill */}
        <div className="px-4 py-3 border-b border-slate-800/50">
          <div className="flex items-center gap-2 bg-slate-900/80 px-3 py-2 rounded-lg border border-slate-800">
            <ShieldCheck className="w-4 h-4 text-emerald-400" />
            <div className="flex-1 overflow-hidden">
              <p className="text-xs font-semibold text-slate-200 truncate">Nexus Global Inc.</p>
              <p className="text-[10px] text-slate-400">Enterprise Tenant</p>
            </div>
          </div>
        </div>

        {/* Navigation items */}
        <nav className="p-3 space-y-1">
          {navigation.map((item) => {
            const isActive = pathname === item.href || (pathname.startsWith(item.href) && item.href !== '/dashboard');
            return (
              <Link
                key={item.name}
                href={item.href}
                className={`flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 ${
                  isActive
                    ? 'bg-gradient-to-r from-sky-600/30 to-indigo-600/30 text-sky-300 border border-sky-500/30 shadow-md shadow-sky-950/50'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800/40'
                }`}
              >
                <item.icon className={`w-4 h-4 ${isActive ? 'text-sky-400' : 'text-slate-400'}`} />
                {item.name}
              </Link>
            );
          })}
        </nav>
      </div>

      {/* Footer Info */}
      <div className="p-4 border-t border-slate-800/80 text-xs text-slate-500">
        <div className="flex items-center justify-between">
          <span>Version 1.0.0</span>
          <span className="inline-block w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
        </div>
      </div>
    </aside>
  );
}
