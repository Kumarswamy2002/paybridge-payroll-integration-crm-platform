import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'PayBridge — Payroll Integration CRM Platform',
  description: 'Enterprise relationship-driven payroll orchestration, reconciliation, and integration platform.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased selection:bg-sky-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
