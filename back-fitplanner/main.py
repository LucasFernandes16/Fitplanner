from fastapi import FastAPI, HTTPException
from classes import *
from montar_treino import * 
from criar_prompt import *
from login import *
from gerenciador_dados import salvar_usuarios
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Adicione outras origens, se necessário
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
    # Verifica se o email foi fornecido
    if not user.email:
        raise HTTPException(status_code=400, detail="Email não fornecido")
    
    # Verifica se o usuário existe
    if user.email not in logins:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    treino_gerado = montar_treino(user)
    
    # Converte o dicionário para um objeto treino
    treino_obj = treino(**treino_gerado)
    logins[user.email]["treino"] = treino_obj
    salvar_usuarios(logins)

    return treino_gerado

@app.post("/registrar-login")
def registrar_login(data: login) -> dict:
    email = data.email
    senha = data.senha
    if email_registrado(email):
        raise HTTPException(status_code=410, detail="Email já registrado")
    
    login_atual = login(email=email, senha=senha)
    if not login_atual.email_valido():
        raise HTTPException(status_code=411, detail="Email inválido")
    if not login_atual.senha_valida():
        raise HTTPException(status_code=412, detail="Senha inválida, a senha precisa ter pelo menos um digito e um caractere especial")
    
    logins[email] = {
        "login": login_atual, 
        "treino": treino(
            domingo=None, 
            segunda=None, 
            terca=None, 
            quarta=None, 
            quinta=None, 
            sexta=None, 
            sabado=None
        )
    }

    salvar_usuarios(logins)
    return {"message": "Registro realizado com sucesso"}

@app.patch("/atualizar-senha")
def atualizar_senha(email: str, senha_nova: str) -> None:
    if not email_registrado(email):
        raise HTTPException(status_code= 413, detail= "Email não encontrado")
    
    login_atualizado = login(email= email, senha= senha_nova)
    if not login_atualizado.senha_valida():
        raise HTTPException(status_code= 412, detail= "Senha inválida, a senha precisa ter pelo menos um digito e um caractere especial")
    
    login_antigo = encontrar_login(email)
    if login_antigo.mesma_senha(senha_nova):
        raise HTTPException(status_code= 414, detail= "A nova senha não pode ser igual a senha atual")
    login_antigo.atualizar_senha(senha_nova)

    salvar_usuarios(logins)

@app.post("/fazer-login")
def fazer_login(data: login) -> dict:
    email = data.email
    senha = data.senha
    if email not in logins:
        raise HTTPException(status_code= 410, detail= "Email não encontrado")
    
    login_atual = encontrar_login(email)
    if not login_atual.mesma_senha(senha):
        raise HTTPException(status_code= 415, detail= "Senha incorreta")
    
    return {"message": "Login realizado com sucesso"}
            
@app.patch("/salvar-treino")
def salvar_treino(user: usuario, email: str) -> None:
    logins[email]["treino"] = montar_treino(user)

    salvar_usuarios(logins)

@app.get("/resgatar-treino")
def resgatar_treino(email: str) -> treino:
    if email not in logins:
        raise HTTPException(status_code=404, detail="Treino não encontrado para o email fornecido")
    return logins[email]["treino"]