from criar_prompt import criar_prompt
from classes import *
import openai

def receber_resposta(user: usuario) -> str:
    openai.api_key = "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"

    prompt: str = criar_prompt(user)
    resposta = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = [{"role": "user", "content": prompt}])
    
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
    
    lista_treinos: list[list[str]] = receber_resposta(user).split("#")
    
    dias_treino: list[int] = user.dias_disponiveis.copy()
    chaves_cronograma = list(cronograma.keys())
    
    for treino in lista_treinos:
        try:
            cronograma[chaves_cronograma[dias_treino[0]]] = eval(treino)
        except:
            cronograma[chaves_cronograma[dias_treino[0]]] = [treino.strip()]

    
        
        dias_treino.pop(0)
        
    for dia in cronograma.keys():
        if not cronograma[dia]:
            cronograma[dia] = ["descanso"]

            
    return cronograma