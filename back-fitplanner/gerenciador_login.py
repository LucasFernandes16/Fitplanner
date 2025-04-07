from classes import login, treino
from gerenciador_dados import carregar_usuarios, salvar_usuarios

logins = carregar_usuarios()

def email_registrado(email: str) -> bool:
    return email in logins

def encontrar_login(email: str) -> login:
    return logins[email]["login"]