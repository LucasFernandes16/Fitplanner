'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useState, useEffect } from 'react';

export default function Navbar() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const pathname = usePathname();

  useEffect(() => {
    const email = localStorage.getItem('userEmail');
    setIsLoggedIn(!!email);
  }, []);

  const handleLogout = () => {
    localStorage.removeItem('userEmail');
    window.location.href = '/';
  };

  const isActive = (path: string) => pathname === path;

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-gray-800/90 backdrop-blur-md border-b border-gray-700/50">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <Link href="/" className="flex items-center space-x-2">
            <span className="text-2xl font-bold text-green-500">FitPlanner</span>
          </Link>

          {/* Navigation Links */}
          <div className="hidden md:flex items-center space-x-4">
            {isLoggedIn ? (
              <>
                <Link 
                  href="/formulario" 
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors
                    ${isActive('/formulario') 
                      ? 'bg-green-500 text-white' 
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
                >
                  Criar Treino
                </Link>
                <Link 
                  href="/treino" 
                  className={`px-3 py-2 rounded-md text-sm font-medium transition-colors
                    ${isActive('/treino') 
                      ? 'bg-green-500 text-white' 
                      : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
                >
                  Meu Treino
                </Link>
                <button
                  onClick={handleLogout}
                  className="px-3 py-2 rounded-md text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white transition-colors"
                >
                  Sair
                </button>
              </>
            ) : (
              <Link 
                href="/" 
                className={`px-3 py-2 rounded-md text-sm font-medium transition-colors
                  ${isActive('/') 
                    ? 'bg-green-500 text-white' 
                    : 'text-gray-300 hover:bg-gray-700 hover:text-white'}`}
              >
                Login
              </Link>
            )}
          </div>

          {/* Mobile menu button */}
          <div className="md:hidden">
            <button
              type="button"
              className="inline-flex items-center justify-center p-2 rounded-md text-gray-400 hover:text-white hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white"
              aria-controls="mobile-menu"
              aria-expanded="false"
            >
              <span className="sr-only">Abrir menu principal</span>
              {/* Icon */}
              <svg
                className="h-6 w-6"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M4 6h16M4 12h16M4 18h16"
                />
              </svg>
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
}