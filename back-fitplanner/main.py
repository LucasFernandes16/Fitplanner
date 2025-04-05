from fastapi import FastAPI, HTTPException
from classes import *
from montar_treino import * 
from criar_prompt import *
from login import *
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

@app.post("/ler-usuario")
def ler(user: usuario):
    return user

@app.post("/intensidade")
def intens(user: usuario) -> str:
    return calcular_intensidade(user)

@app.post("/testar-prompt")
def prompt(user: usuario) -> str:
    return criar_prompt(user)

@app.post("/testarGPT")
def gpt(user: usuario) -> str:
    return receber_resposta(user)

@app.post("/criar-treino")
def treino_usuario(user: usuario) -> treino:
    return montar_treino(user)

@app.get("/registrar-login/")
def registrar_login(email: str, senha: str) -> None:
    if email_registrado(email):
        raise HTTPException(status_code= 410, detail= "Email já registrado")
    
    login_atual = login(email, senha)
    if not login_atual.email_valido():
        raise HTTPException(status_code= 411, detail= "Email inválido")
    if not login_atual.senha_valida():
        raise HTTPException(status_code= 412, detail= "Senha inválida, a senha precisa ter pelo menos um digito e um caractere especial")
    
    logins.update({login_atual: None})

@app.patch("/atualizar-senha")
def atualizar_senha(email: str, senha_nova: str) -> None:
    if not email_registrado(email):
        raise HTTPException(status_code= 413, detail= "Email não encontrado")
    
    login_atualizado = login(email, senha_nova)
    if not login_atualizado.senha_valida():
        raise HTTPException(status_code= 412, detail= "Senha inválida, a senha precisa ter pelo menos um digito e um caractere especial")
    
    login_antigo = encontrar_login(email)
    if login_antigo.mesma_senha(senha_nova):
        raise HTTPException(status_code= 414, detail= "A nova senha não pode ser igual a senha atual")
    login_antigo.atualizar_senha(senha_nova)

@app.post("/fazer-login")
def fazer_login(email: str, senha: str) -> None:
    if not email_registrado(email):
        raise HTTPException(status_code= 413, detail= "Email não encontrado")
    
    login_atual = encontrar_login(email)
    if not login_atual.mesma_senha(senha):
        raise HTTPException(status_code= 415, detail= "Senha incorreta")
    return True
            
@app.patch("/salvar-treino")
def salvar_treino(user: usuario, email: str) -> None:
    logins[encontrar_login(email)] = montar_treino(user)

@app.post("resgatar-treino")
def resgatar_treino(email: str) -> treino:
    return logins[encontrar_login(email)]