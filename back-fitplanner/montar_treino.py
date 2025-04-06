from criar_prompt import criar_prompt
from classes import *
import openai
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def receber_resposta(user: usuario) -> str:
    # Carrega a chave da API do OpenAI a partir das variáveis de ambiente
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    if not openai.api_key:
        raise ValueError("A chave da API do OpenAI não foi encontrada. Verifique o arquivo .env.")

    prompt: str = criar_prompt(user)
    resposta = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    
    return resposta["choices"][0]["message"]["content"]

def montar_treino(user: usuario) -> treino:
    cronograma = {
        "domingo": [],
        "segunda": [],
        "terca": [],
        "quarta": [],
        "quinta": [],
        "sexta": [],
        "sabado": []
    }
    
    # Mapeia os índices de dias disponíveis para os nomes dos dias
    dias_semana = ["domingo", "segunda", "terca", "quarta", "quinta", "sexta", "sabado"]
    dias_disponiveis = [dias_semana[i] for i in user.dias_disponiveis]
    
    lista_treinos: list[list[str]] = receber_resposta(user).split("#")
    
    for treino in lista_treinos:
        if not dias_disponiveis:
            break
        try:
            cronograma[dias_disponiveis[0]] = eval(treino)
        except:
            cronograma[dias_disponiveis[0]] = [treino.strip()]
        
        dias_disponiveis.pop(0)
        
    for dia in cronograma.keys():
        if not cronograma[dia]:
            cronograma[dia] = ["descanso"]

    return cronograma