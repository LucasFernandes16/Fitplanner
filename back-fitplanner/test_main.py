from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_1_dia():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias":[1]})

    assert resposta.status_code == 200
def test_todos_dias():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias":[0, 1, 2, 3, 4, 5, 6]})

    assert resposta.status_code == 200
def test_dias_consecutivos():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias":[1, 2, 3]})

    assert resposta.status_code == 200
def test_dias_espacados():
    resposta = client.post("/criar-treino", json= {"idade":18,"experiencia":True,"dias":[1, 3, 5]})

    assert resposta.status_code == 200

def test_idoso_experiente():
    resposta = client.post("/intensidade", json= {"idade":70,"experiencia":True,"dias":[1]})

    assert resposta.status_code == 200
    assert resposta.text == "Média"
def test_idoso_inexperiente():
    resposta = client.post("/intensidade", json= {"idade":70,"experiencia":False,"dias":[1]})

    assert resposta.status_code == 200
    assert resposta.text == "Baixa"
def test_jovem_experiente():
    resposta = client.post("/intensidade", json= {"idade":18,"experiencia":True,"dias":[1]})

    assert resposta.status_code == 200
    assert resposta.text == "Alta"
def test_jovem_inexperiente():
    resposta = client.post("/", json= {"idade":18,"experiencia":False,"dias":[1]})

    assert resposta.status_code == 200
    assert resposta.text == "Média"

def test_prompt_1_dia():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0]})

    assert resposta.status_code == 200
def test_prompt_2_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1]})

    assert resposta.status_code == 200
def test_prompt_3_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1, 2]})

    assert resposta.status_code == 200
def test_prompt_4_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1, 2, 3]})

    assert resposta.status_code == 200
def test_prompt_5_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1, 2, 3, 4]})

    assert resposta.status_code == 200
def test_prompt_6_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1, 2, 3, 4, 5]})

    assert resposta.status_code == 200
def test_prompt_7_dias():
    resposta = client.post("/testar-prompt", json={"idade":18,"experiencia":False,"dias":[0, 1, 2, 3, 4, 5, 6]})

    assert resposta.status_code == 200