from classes import login, treino

logins = {
    login("cesar@gmail.com", "senhacesar1@"): None,
    login("guilherme@gmail.com", "senhaguilherme1@"): None,
    login("gabriel@gmail.com", "senhagabriel1@"): None,
    login("tiago@gmail.com", "senhatiago1@"): None,
    login("lucas@gmail.com", "senhalucas1@"): None
}

def email_registrado(email: str) -> bool:
    return email in logins

def encontrar_login(email: str) -> login:
    for i in logins:
        if i == email:
            return i