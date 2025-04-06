'use client'; // Marca o componente como Client Component

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import Header from '../components/Header';

export default function Home() {
  const [nome, setNome] = useState<string>('');
  const [idade, setIdade] = useState<string>('');
  const [diasDisponiveis, setDiasDisponiveis] = useState<{ [key: string]: boolean }>({
    domingo: false,
    segunda: false,
    terca: false,
    quarta: false,
    quinta: false,
    sexta: false,
    sabado: false,
  });
  const [experiencia, setExperiencia] = useState<boolean>(false);
  const router = useRouter();

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    // Converte os dias disponíveis para uma lista de índices
    const diasDisponiveisArray = Object.keys(diasDisponiveis)
      .map((day, index) => diasDisponiveis[day] ? index : null)
      .filter((day): day is number => day !== null);

    // Pegar o email do usuário logado do localStorage ou estado global
    const email = localStorage.getItem('userEmail'); // Adicione esta linha

    const userData = {
      email, // Adicione o email aos dados
      idade: parseInt(idade, 10),
      experiencia,
      dias_disponiveis: diasDisponiveisArray
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/criar-treino', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        console.error('Erro no servidor:', errorData);
        alert(errorData.detail || 'Erro ao gerar treino');
        throw new Error('Erro ao enviar dados para o backend');
      }

      const data = await response.json();
      router.push(`/treino?treino=${JSON.stringify(data)}`);
    } catch (error) {
      console.error('Erro:', error);
    }
  };

  const handleDayChange = (day: string) => {
    setDiasDisponiveis((prev) => ({
      ...prev,
      [day]: !prev[day],
    }));
  };

  return (
    <div className="min-h-screen flex flex-col relative">
          <Header />
          
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

      {/* Gradient Overlay */}
      <div className="absolute inset-0 bg-gradient-to-br from-gray-900/95 to-gray-800/95 z-1" />

      {/* Decorative Elements */}
      <div className="absolute inset-0 overflow-hidden z-2">
        <div className="absolute -top-10 -right-10 w-60 h-60 bg-green-500 rounded-full filter blur-3xl opacity-10" />
        <div className="absolute -bottom-10 -left-10 w-60 h-60 bg-blue-500 rounded-full filter blur-3xl opacity-10" />
      </div>

      {/* Main Content */}
      <div className="container mx-auto px-4 relative z-10">
        <div className="max-w-2xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-white mb-2">Criar Treino</h1>
            <p className="text-gray-400">Personalize seu treino de acordo com suas necessidades</p>
          </div>

          {/* Form Card */}
          <div className="bg-gray-800/90 backdrop-blur-xl rounded-2xl shadow-xl p-8 border border-gray-700/50">
            <form onSubmit={handleSubmit} className="space-y-6">
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
                <label className="block text-sm font-medium text-gray-300 mb-2">
                  Dias Disponíveis:
                </label>
                <div className="grid grid-cols-4 gap-2">
                  {Object.keys(diasDisponiveis).map((day) => (
                    <button
                      key={day}
                      type="button"
                      onClick={() => handleDayChange(day)}
                      className={`py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                        diasDisponiveis[day]
                          ? 'bg-green-600 text-white hover:bg-green-700'
                          : 'bg-gray-600 text-gray-300 hover:bg-gray-500'
                      }`}
                    >
                      {day.charAt(0).toUpperCase() + day.slice(1)}
                    </button>
                  ))}
                </div>
              </div>
              <div className="mb-4">
                <label htmlFor="experiencia" className="block text-sm font-medium text-gray-300">
                  Experiência:
                </label>
                <div className="flex gap-4 mt-2">
                  <button
                    type="button"
                    onClick={() => setExperiencia(false)}
                    className={`py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                      experiencia === false
                        ? 'bg-green-600 text-white hover:bg-green-700'
                        : 'bg-gray-600 text-gray-300 hover:bg-gray-500'
                    }`}
                  >
                    Iniciante
                  </button>
                  <button
                    type="button"
                    onClick={() => setExperiencia(true)}
                    className={`py-2 px-4 rounded-md text-sm font-medium transition-colors ${
                      experiencia === true
                        ? 'bg-green-600 text-white hover:bg-green-700'
                        : 'bg-gray-600 text-gray-300 hover:bg-gray-500'
                    }`}
                  >
                    Avançado
                  </button>
                </div>
              </div>
              <button
                type="submit"
                className="w-full bg-green-600 text-white py-2 px-4 rounded-md hover:bg-green-700 focus:outline-none focus:ring-2 focus:ring-green-500"
              >
                Enviar
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}