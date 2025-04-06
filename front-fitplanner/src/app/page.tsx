'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';

export default function LoginPage() {
  const [email, setEmail] = useState('');
  const [senha, setSenha] = useState('');
  const [isRegistering, setIsRegistering] = useState(false); // Estado para alternar entre login e registro
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
    <div className="min-h-screen bg-gray-800 text-white flex items-center justify-center">
      <form onSubmit={handleSubmit} className="max-w-md bg-gray-700 p-6 rounded-lg shadow-md">
        <h2 className="text-xl font-bold mb-4">
          {isRegistering ? 'Registrar-se' : 'Login'}
        </h2>
        <div className="mb-4">
          <label htmlFor="email" className="block text-sm font-medium text-gray-300">
            Email:
          </label>
          <input
            type="email"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
        </div>
        <div className="mb-4">
          <label htmlFor="senha" className="block text-sm font-medium text-gray-300">
            Senha:
          </label>
          <input
            type="password"
            id="senha"
            value={senha}
            onChange={(e) => setSenha(e.target.value)}
            className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500"
        >
          {isRegistering ? 'Registrar' : 'Login'}
        </button>
        <p className="mt-4 text-sm text-gray-400 text-center">
          {isRegistering ? 'Já tem uma conta?' : 'Não tem uma conta?'}{' '}
          <button
            type="button"
            onClick={() => setIsRegistering(!isRegistering)}
            className="text-green-500 hover:underline"
          >
            {isRegistering ? 'Faça login' : 'Registre-se'}
          </button>
        </p>
      </form>
    </div>
  );
}
