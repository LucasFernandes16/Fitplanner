from fastapi.testclient import TestClient
from classes import *
from main import app

client = TestClient(app)

def test_1_dia():
    resposta = client.post("/criar-treino", json= {"idade": 18, "experiencia": True, "dias_disponiveis": [1]})

    assert resposta.status_code == 200
def test_todos_dias():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias_disponiveis":[0, 1, 2, 3, 4, 5, 6]})

    assert resposta.status_code == 200
def test_dias_consecutivos():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias_disponiveis":[1, 2, 3]})

    assert resposta.status_code == 200
def test_dias_espacados():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias_disponiveis":[1, 3, 5]})

    assert resposta.status_code == 200

def test_idoso_experiente():
    resposta = client.post("/intensidade", json= {"idade":70,"experiencia":True,"dias_disponiveis":[1]})

    assert resposta.status_code == 200
    assert resposta.text == '"Média"'
def test_idoso_inexperiente():
    resposta = client.post("/intensidade", json= {"idade":70,"experiencia":False,"dias_disponiveis":[1]})

    assert resposta.status_code == 200
    assert resposta.text == '"Baixa"'
def test_jovem_experiente():
    resposta = client.post("/intensidade", json= {"idade":18,"experiencia":True,"dias_disponiveis":[1]})

    assert resposta.status_code == 200
    assert resposta.text == '"Alta"'
def test_jovem_inexperiente():
    resposta = client.post("/intensidade", json= {"idade":18,"experiencia":False,"dias_disponiveis":[1]})

    assert resposta.status_code == 200
    assert resposta.text == '"Média"'

def test_prompt_1_dia():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0]})

    assert resposta.status_code == 200
def test_prompt_2_dias_disponiveis():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1]})

    assert resposta.status_code == 200
def test_prompt_3_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1, 2]})

    assert resposta.status_code == 200
def test_prompt_4_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1, 2, 3]})

    assert resposta.status_code == 200
def test_prompt_5_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1, 2, 3, 4]})

    assert resposta.status_code == 200
def test_prompt_6_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1, 2, 3, 4, 5]})

    assert resposta.status_code == 200
def test_prompt_7_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias_disponiveis":[0, 1, 2, 3, 4, 5, 6]})

    assert resposta.status_code == 200


#Testes de Login
def test_email_valido():
    repostas = client.get("/registrar-login", params= {"email": "teste@gmail.com", "senha": "aaa1@"})

    assert repostas.status_code == 200

def test_email_ja_existente():
    repostas = client.get("/registrar-login", params= {"email": "teste@gmail.com", "senha": "aaa1@"})

    assert repostas.status_code == 410

def test_senha_invalida():
    #Teste de senha sem caractere especial
    repostas_especial = client.get("/registrar-login", params= {"email": "teste2@gmail.com", "senha": "aaa1"})
    #Teste de senha senha sem digito
    repostas_digito = client.get("/registrar-login", params= {"email": "teste2@gmail.com", "senha": "aaa@"})
    #Teste de senha sem caractere esopecial ou digito
    repostas_geral = client.get("/registrar-login", params= {"email": "teste2@gmail.com", "senha": "aaa"})

    assert repostas_especial.status_code == 412
    assert repostas_digito.status_code == 412
    assert repostas_geral.status_code == 412

def test_email_invalido():
    repostas = client.get("/registrar-login", params= {"email": "teste@email.com", "senha": "aaa1@"})

    assert repostas.status_code == 411