'use client';

import React, { useState, useEffect } from 'react';
import { Shield, CheckCircle, AlertTriangle, RefreshCw, Cpu, Database, Settings, User } from 'lucide-react';

export interface AdapterGridProps {
  tenantId?: string;
  onRefresh?: () => void;
}

export function AdapterGrid({ tenantId = 'default_tenant', onRefresh }: AdapterGridProps) {
  const [loading, setLoading] = useState(false);
  const [items, setItems] = useState<any[]>([]);

  useEffect(() => {
    // Simulating component data initialization
    const mockData = Array.from({ length: 15 }).map((_, idx) => ({
      id: `adaptergrid_${idx + 1}`,
      name: `AdapterGrid Record #${idx + 1}`,
      code: `REF-${1000 + idx}`,
      status: idx % 4 === 0 ? 'WARNING' : 'ACTIVE',
      updatedAt: new Date().toISOString(),
    }));
    setItems(mockData);
  }, []);

  const handleRefresh = () => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
      if (onRefresh) onRefresh();
    }, 600);
  };

  return (
    <div className="glass-card rounded-2xl p-6 border border-slate-800 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-lg font-bold text-slate-100">AdapterGrid Portal</h3>
          <p className="text-xs text-slate-400 mt-0.5">Enterprise CRM component for AdapterGrid management</p>
        </div>
        <button
          onClick={handleRefresh}
          className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold border border-slate-700 transition-colors flex items-center gap-2"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} /> Refresh
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {items.slice(0, 3).map((item) => (
          <div key={item.id} className="bg-slate-900/60 p-4 rounded-xl border border-slate-800/80 space-y-2">
            <div className="flex justify-between items-center text-xs">
              <span className="font-bold text-slate-200">{item.name}</span>
              <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${item.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'}`}>
                {item.status}
              </span>
            </div>
            <p className="text-[11px] text-slate-400 font-mono">ID: {item.code}</p>
          </div>
        ))}
      </div>

      <div className="overflow-x-auto">
        <table className="w-full text-left text-xs text-slate-300">
          <thead className="bg-slate-900/80 uppercase text-[10px] font-bold text-slate-400 border-b border-slate-800">
            <tr>
              <th className="p-3">Record Name</th>
              <th className="p-3">Reference Code</th>
              <th className="p-3">Status</th>
              <th className="p-3">Timestamp</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {items.map((item) => (
              <tr key={item.id} className="hover:bg-slate-800/40 transition-colors">
                <td className="p-3 font-semibold text-slate-200">{item.name}</td>
                <td className="p-3 font-mono text-slate-400">{item.code}</td>
                <td className="p-3">
                  <span className={`px-2 py-0.5 rounded text-[10px] font-bold ${item.status === 'ACTIVE' ? 'bg-emerald-500/20 text-emerald-400' : 'bg-amber-500/20 text-amber-400'}`}>
                    {item.status}
                  </span>
                </td>
                <td className="p-3 text-slate-400">{new Date(item.updatedAt).toLocaleTimeString()}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}