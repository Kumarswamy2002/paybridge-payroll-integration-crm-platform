import React from 'react';
import { LucideIcon } from 'lucide-react';

interface StatsCardProps {
  title: string;
  value: string | number;
  change?: string;
  isPositive?: boolean;
  icon: LucideIcon;
  color: 'sky' | 'emerald' | 'amber' | 'indigo' | 'purple';
}

const colorStyles = {
  sky: 'bg-sky-500/10 text-sky-400 border-sky-500/20',
  emerald: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20',
  amber: 'bg-amber-500/10 text-amber-400 border-amber-500/20',
  indigo: 'bg-indigo-500/10 text-indigo-400 border-indigo-500/20',
  purple: 'bg-purple-500/10 text-purple-400 border-purple-500/20',
};

export function StatsCard({ title, value, change, isPositive, icon: Icon, color }: StatsCardProps) {
  return (
    <div className="glass-card rounded-xl p-5 relative overflow-hidden group hover:border-slate-700 transition-all duration-300">
      <div className="flex items-center justify-between">
        <span className="text-xs font-semibold text-slate-400 uppercase tracking-wider">{title}</span>
        <div className={`p-2.5 rounded-xl border ${colorStyles[color]}`}>
          <Icon className="w-5 h-5" />
        </div>
      </div>
      
      <div className="mt-3">
        <div className="text-2xl font-bold text-slate-100 tracking-tight">{value}</div>
        {change && (
          <p className={`text-xs mt-1 font-medium ${isPositive ? 'text-emerald-400' : 'text-amber-400'}`}>
            {isPositive ? '↑' : '↓'} {change} <span className="text-slate-500 font-normal">vs last pay period</span>
          </p>
        )}
      </div>
    </div>
  );
}
