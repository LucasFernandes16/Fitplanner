'use client'; // Marca o componente como Client Component

import { useSearchParams } from 'next/navigation';
import Header from '../components/Header';

export default function Treino() {
  const searchParams = useSearchParams();
  const treino = searchParams ? searchParams.get('treino') : null;

  // Converte o treino de volta para um objeto
  const treinoGerado = treino ? JSON.parse(treino) : null;

  console.log(treinoGerado);

  return (
    <div className="min-h-screen bg-gray-800 text-white">
      <Header />
      <div className="pt-20 container mx-auto px-4">
        <div className="bg-gray-700 p-6 rounded-lg shadow-md">
          <h2 className="text-3xl font-bold mb-4">Seu Treino Personalizado</h2>
          {treinoGerado ? (
            <div>
              {Object.entries(treinoGerado).map(([dia, exercicios]) => (
                <div key={dia} className="mb-4">
                  <h3 className="text-xl font-semibold capitalize">{dia}</h3>
                  <ul>
                    {Array.isArray(exercicios) ? (
                      exercicios.map((exercicio, index) => (
                        <li key={index} className="bg-gray-800 p-2 rounded-md mb-2">
                          {exercicio}
                        </li>
                      ))
                    ) : exercicios ? (
                      <li className="bg-gray-800 p-2 rounded-md mb-2">{String(exercicios)}</li>
                    ) : (
                      <li className="text-gray-400">Nenhum exercício para esse dia</li>
                    )}
                  </ul>
                </div>
              ))}
            </div>
          ) : (
            <p>Nenhum treino gerado.</p>
          )}
        </div>
      </div>
    </div>
  );
}