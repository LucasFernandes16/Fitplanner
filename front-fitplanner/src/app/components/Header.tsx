import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-green-600 text-white py-4 shadow-lg fixed w-full top-0 z-50">
      <div className="container mx-auto flex justify-between items-center px-4">
        <div className="flex items-center">
          <h1 className="text-2xl font-bold">FitPlanner AI</h1>
        </div>
        <nav>
          <Link href="/treino" className="hover:text-green-200">
            Treino
          </Link>
        </nav>
      </div>
    </header>
  );
}