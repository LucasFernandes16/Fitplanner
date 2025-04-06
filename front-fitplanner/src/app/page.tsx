'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Image from 'next/image';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    try {
      const endpoint = isRegistering
        ? `http://127.0.0.1:8000/registrar-login`
        : `http://127.0.0.1:8000/fazer-login`;

      const data = {
        email,
        senha
      };

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error('Erro no servidor:', errorData);

        if (response.status === 410 && isRegistering) {
          alert('O email já está registrado. Tente fazer login.');
        } else if (response.status === 410 && !isRegistering) {
          alert('Email não encontrado. Tente se registrar.');
        } else if (response.status === 415) {
          alert('Senha incorreta.');
        } else {
          alert('Erro ao processar a solicitação.');
        }

        throw new Error(`Erro: ${response.status} - ${response.statusText}`);
      }

      // Salva o email do usuário após login bem-sucedido
      localStorage.setItem('userEmail', email);

      console.log(isRegistering ? 'Registro bem-sucedido' : 'Login bem-sucedido');
      alert(isRegistering ? 'Registro realizado com sucesso!' : 'Login realizado com sucesso!');

      router.push('/formulario');
    } catch (error) {
      console.error('Erro ao conectar ao backend:', error);
      alert('Erro ao conectar ao servidor. Tente novamente mais tarde.');
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center relative">
      {/* Background Image */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'url("/backgrounds/gym-background.jpg")',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          backgroundRepeat: 'no-repeat',
        }}
      />

      {/* Dark Overlay */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-900/95 to-gray-800/95 z-1" />
      
      {/* Decorative Elements with adjusted opacity */}
      <div className="absolute inset-0 overflow-hidden z-2">
        <div className="absolute -top-10 -right-10 w-60 h-60 bg-green-500 rounded-full filter blur-3xl opacity-10" />
        <div className="absolute -bottom-10 -left-10 w-60 h-60 bg-blue-500 rounded-full filter blur-3xl opacity-10" />
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-md mx-auto">
          {/* Logo Section */}
          <div className="text-center mb-8">
            <div className="w-20 h-20 mx-auto mb-4 relative">
              <Image
                src="/dumbbell-icon.png"
                alt="FitPlanner Logo"
                layout="fill"
                className="object-contain"
              />
            </div>
            <h1 className="text-3xl font-bold text-white mb-2">FitPlanner</h1>
            <p className="text-gray-400">Seu parceiro de treino personalizado</p>
          </div>

          {/* Form Card with increased transparency */}
          <div className="bg-gray-800/90 backdrop-blur-xl rounded-2xl shadow-xl p-8 border border-gray-700/50">
            <h2 className="text-2xl font-bold text-white mb-6 text-center">
              {isRegistering ? 'Criar Conta' : 'Bem-vindo de volta!'}
            </h2>

            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label htmlFor="email" className="block text-sm font-medium text-gray-300 mb-2">
                  Email
                </label>
                <input
                  type="email"
                  id="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-all"
                  required
                />
              </div>

              <div>
                <label htmlFor="senha" className="block text-sm font-medium text-gray-300 mb-2">
                  Senha
                </label>
                <input
                  type="password"
                  id="senha"
                  value={senha}
                  onChange={(e) => setSenha(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg bg-gray-700 border border-gray-600 text-white focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition-all"
                  required
                />
              </div>

              <button
                type="submit"
                className="w-full bg-gradient-to-r from-green-500 to-green-600 text-white py-3 px-4 rounded-lg font-medium hover:from-green-600 hover:to-green-700 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-offset-2 focus:ring-offset-gray-800 transition-all transform hover:scale-[1.02]"
              >
                {isRegistering ? 'Criar Conta' : 'Entrar'}
              </button>
            </form>

            <div className="mt-6 text-center">
              <button
                onClick={() => setIsRegistering(!isRegistering)}
                className="text-gray-400 hover:text-green-400 transition-colors"
              >
                {isRegistering ? 'Já tem uma conta? Entre' : 'Não tem uma conta? Registre-se'}
              </button>
            </div>

            {/* Feature Highlights */}
            <div className="mt-8 pt-6 border-t border-gray-700">
              <div className="grid grid-cols-2 gap-4">
                <div className="text-center">
                  <div className="w-10 h-10 mx-auto mb-2 bg-gray-700 rounded-full flex items-center justify-center">
                    <svg className="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                  </div>
                  <p className="text-sm text-gray-400">Treinos Personalizados</p>
                </div>
                <div className="text-center">
                  <div className="w-10 h-10 mx-auto mb-2 bg-gray-700 rounded-full flex items-center justify-center">
                    <svg className="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                  </div>
                  <p className="text-sm text-gray-400">Acompanhamento Eficiente</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
