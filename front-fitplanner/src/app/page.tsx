'use client'; // Marca o componente como Client Component

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Header from './components/Header';

export default function Home() {
  const [nome, setNome] = useState<string>('');
  const [idade, setIdade] = useState<string>('');
  const [diasDisponiveis, setDiasDisponiveis] = useState<string>('');
  const [intensidade, setIntensidade] = useState<string>('leve');
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Dados do formulário
    const userData = {
      nome,
      idade: parseInt(idade, 10),
      dias_disponiveis: diasDisponiveis.split(',').map(Number),
      experiencia: true, // Adicione a lógica para definir a experiência
    };

    try {
      // Envia os dados para o backend
      const response = await fetch('http://127.0.0.1:8000/criar-treino', { 
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });
      
      if (!response.ok) {
        throw new Error('Erro ao enviar dados para o backend');
      }

      const data = await response.json();
      console.log('Resposta do backend:', data);

      // Redireciona para a página de treino com os dados
      router.push(`/treino?treino=${JSON.stringify(data)}`);
    } catch (error) {
      console.error('Erro:', error);
    }
  };

  return (
    <div className="min-h-screen bg-gray-800 text-white">
      <Header />
      <div className="pt-20 container mx-auto px-4">
        <div className="text-center mb-8">
          <h2 className="text-3xl font-bold mb-4">FitPlanner AI</h2>
          <p className="text-gray-300">
            Sua melhor versão aqui.
          </p>
        </div>
        <form onSubmit={handleSubmit} className="max-w-md mx-auto bg-gray-700 p-6 rounded-lg shadow-md">
          <div className="mb-4">
            <label htmlFor="nome" className="block text-sm font-medium text-gray-300">
              Nome:
            </label>
            <input
              type="text"
              id="nome"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="idade" className="block text-sm font-medium text-gray-300">
              Idade:
            </label>
            <input
              type="number"
              id="idade"
              value={idade}
              onChange={(e) => setIdade(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>
          <div className="mb-4">
            <label htmlFor="diasDisponiveis" className="block text-sm font-medium text-gray-300">
              Dias Disponíveis (separados por vírgula):
            </label>
            <input
              type="text"
              id="diasDisponiveis"
              value={diasDisponiveis}
              onChange={(e) => setDiasDisponiveis(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>
          <div className="mb-6">
            <label htmlFor="intensidade" className="block text-sm font-medium text-gray-300">
              Nível de Intensidade:
            </label>
            <select
              id="intensidade"
              value={intensidade}
              onChange={(e) => setIntensidade(e.target.value)}
              className="mt-1 block w-full px-3 py-2 border border-gray-600 rounded-md bg-gray-800 text-white focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            >
              <option value="leve">Leve</option>
              <option value="moderado">Moderado</option>
              <option value="intenso">Intenso</option>
            </select>
          </div>
          <button
            type="submit"
            className="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500"
          >
            Começar
          </button>
        </form>
      </div>
      <div className=''>

      </div>
    </div>
  );
}