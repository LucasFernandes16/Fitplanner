import type { Metadata } from 'next';
import './../styles/globals.css';

export const metadata: Metadata = {
  title: 'FitPlanner AI',
  description: 'Um aplicativo que monta seus treinos de acordo com uma IA.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}