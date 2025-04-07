'use client';

import { useEffect, useState } from 'react';
import Slider from 'react-slick';
import Header from '../components/Header';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

type TreinoType = {
  domingo: string[] | null;
  segunda: string[] | null;
  terca: string[] | null;
  quarta: string[] | null;
  quinta: string[] | null;
  sexta: string[] | null;
  sabado: string[] | null;
};

export default function Treino() {
  const [treinoGerado, setTreinoGerado] = useState<TreinoType | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const sliderSettings = {
    dots: true,
    infinite: false,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    className: "w-full max-w-2xl mx-auto"
  };

  useEffect(() => {
    const fetchTreino = async () => {
      try {
        const email = localStorage.getItem('userEmail');
        if (!email) {
          setError('Usuário não está logado');
          return;
        }

        const response = await fetch(`http://127.0.0.1:8000/resgatar-treino?email=${email}`);
        
        if (!response.ok) {
          throw new Error('Erro ao buscar treino');
        }

        const data = await response.json();
        setTreinoGerado(data);
      } catch (error) {
        setError('Erro ao carregar o treino');
        console.error('Erro:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchTreino();
  }, []);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-800 text-white">
        <Header />
        <div className="pt-20 container mx-auto px-4">
          <div className="bg-gray-700 p-6 rounded-lg shadow-md">
            <p>Carregando treino...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-800 text-white">
        <Header />
        <div className="pt-20 container mx-auto px-4">
          <div className="bg-gray-700 p-6 rounded-lg shadow-md">
            <p className="text-red-500">{error}</p>
          </div>
        </div>
      </div>
    );
  }

  return (

      <div className="min-h-screen flex flex-col relative">
      <Header />
      
      {/* Background Image */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'url("/backgrounds/gym-background2.jpg")',
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
        <div className="max-w-4xl mx-auto">
          {/* Header */}
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold text-white mb-2">Seu Treino</h1>
            <p className="text-gray-400">Acompanhe seu programa de treino personalizado</p>
          </div>

          {/* Treino Card */}
          <div className="bg-gray-800/90 backdrop-blur-xl rounded-2xl shadow-xl p-8 border border-gray-700/50">
            {treinoGerado ? (
              <Slider {...sliderSettings}>
                {Object.entries(treinoGerado).map(([dia, exercicios]) => (
                  <div key={dia} className="px-4">
                    <div className="bg-gray-700/50 p-6 rounded-xl">
                      <h3 className="text-2xl font-semibold capitalize mb-4 text-center text-green-400">
                        {dia}
                      </h3>
                      <ul className="space-y-3">
                        {Array.isArray(exercicios) ? (
                          exercicios.map((exercicio, index) => (
                            <li 
                              key={index} 
                              className="bg-gray-800/80 p-4 rounded-lg text-center text-white hover:bg-gray-700/80 transition-colors"
                            >
                              {exercicio}
                            </li>
                          ))
                        ) : exercicios ? (
                          <li className="bg-gray-800/80 p-4 rounded-lg text-center text-white">
                            {String(exercicios)}
                          </li>
                        ) : (
                          <li className="text-gray-400 text-center">
                            Descanso
                          </li>
                        )}
                      </ul>
                    </div>
                  </div>
                ))}
              </Slider>
            ) : (
              <p className="text-center text-gray-400">
                Nenhum treino gerado ainda. Vá para a página de formulário para gerar seu treino.
              </p>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}