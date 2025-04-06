from classes import login
from gerenciador_dados import *

logins = carregar_usuarios()

def email_registrado(email: str) -> bool:
    return email in logins

def encontrar_login(email: str) -> login:
    return logins[email]["login"]