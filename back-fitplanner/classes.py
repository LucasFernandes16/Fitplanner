from pydantic import BaseModel

class usuario(BaseModel):
    idade: int
    experiencia: bool
    dias_disponiveis: list[int]  # Lista de índices dos dias disponíveis (0 = domingo, 1 = segunda, etc.)

class treino(BaseModel):
    domingo: list[str]
    segunda: list[str]
    terca: list[str]
    quarta: list[str]
    quinta: list[str]
    sexta: list[str]
    sabado: list[str]

class login:
    def __init__(self, email: str, senha: str) -> None:
        self.email = email
        self.__senha = senha 

    def email_valido(self) -> bool:
        if self.email.count("@") != 1:
            return False
        if self.email.split("@")[-1] == "gmail.com":
            return True
        return False
    
    def __eq__(self, outro: str) -> bool:
        if isinstance(outro, str) and outro == self.email:
            return True
        return False
    
    def __hash__(self) -> int:
        return hash(self.email)
    
    def senha_valida(self) -> bool:
        if self.__caractere_especial() and self.__caractere_numerico:
            return True
        return False

    def __caractere_numerico(self) -> bool:
        return any(caractere in "0123456789" for caractere in self.__senha)
    def __caractere_especial(self) -> bool:
        return any(caractere in "@#$%&*" for caractere in self.__senha)
    
    def mesma_senha(self, nova_senha: str) -> bool:
        if nova_senha == self.__senha:
            return True
        return False
    
    def atualizar_senha(self, nova_senha: str) -> None:
        self.__senha = nova_senha