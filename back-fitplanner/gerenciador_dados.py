import json
from classes import login, treino

def carregar_usuarios() -> dict[str, dict[str, object]]:
    with open("banco_dados.json", "r") as f:
        dados = json.load(f)
    
    usuarios = {}
    for i in dados:
        usuarios[i] = {
            "login": login(
                email=dados[i]["login"]["email"],
                senha=dados[i]["login"]["senha"]
            ),
            "treino": treino(
                domingo=dados[i]["treino"]["domingo"],
                segunda=dados[i]["treino"]["segunda"],
                terca=dados[i]["treino"]["terca"],
                quarta=dados[i]["treino"]["quarta"],
                quinta=dados[i]["treino"]["quinta"],
                sexta=dados[i]["treino"]["sexta"],
                sabado=dados[i]["treino"]["sabado"]
            )
        }
    return usuarios

def salvar_usuarios(usuarios: dict[str, dict[str, object]]) -> None:
    dados = {
        i: {
            "login": {
                "email": usuarios[i]["login"].email,
                "senha": usuarios[i]["login"].senha,
            },
            "treino": {
                "domingo": usuarios[i]["treino"].domingo if isinstance(usuarios[i]["treino"], treino) else None,
                "segunda": usuarios[i]["treino"].segunda if isinstance(usuarios[i]["treino"], treino) else None,
                "terca": usuarios[i]["treino"].terca if isinstance(usuarios[i]["treino"], treino) else None,
                "quarta": usuarios[i]["treino"].quarta if isinstance(usuarios[i]["treino"], treino) else None,
                "quinta": usuarios[i]["treino"].quinta if isinstance(usuarios[i]["treino"], treino) else None,
                "sexta": usuarios[i]["treino"].sexta if isinstance(usuarios[i]["treino"], treino) else None,
                "sabado": usuarios[i]["treino"].sabado if isinstance(usuarios[i]["treino"], treino) else None,
            }
        }
        for i in usuarios
    }

    with open("banco_dados.json", "w") as f:
        json.dump(dados, f, indent=4)