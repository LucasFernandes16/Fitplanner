from fastapi import FastAPI
from classes import *
from montar_treino import * 
from criar_prompt import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite requisições do frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.get("/")
def root():
    return {"Helloooo": "world"}

@app.post("/ler-usuario") #FUNCIONANDO
def ler(user: usuario):
    return user

@app.post("/intensidade") #FUNCIONANDO
def intens(user: usuario) -> str:
    return calcular_intensidade(user)

@app.post("/testar-prompt") #FUNCIONANDO
def prompt(user: usuario) -> str:
    return criar_prompt(user)

@app.post("/testarGPT") #PROBLEMA
def gpt(user: usuario) -> str:
    return receber_resposta(user)

@app.post("/criar-treino") #PROBLEMA 
def treino_usuario(user: usuario) -> treino:
    return montar_treino(user)