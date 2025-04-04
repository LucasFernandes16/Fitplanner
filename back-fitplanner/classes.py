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
