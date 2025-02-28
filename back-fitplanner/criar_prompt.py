from exercicios import exercicios
from classes import usuario

def calcular_intensidade(user: usuario) -> str:
    if user.idade >= 50:
        if user.experiencia:
            return "Média"
        return "Baixa"
    if user.experiencia:
        return "Alta"
    return "Média"

def criar_prompt(user: usuario) -> str:
    intensidade: str = calcular_intensidade(user)
    
    opcoes_peito: list[str] = exercicios["Peito"][intensidade]
    opcoes_triceps: list[str] = exercicios["Tríceps"][intensidade]
    opcoes_ombros: list[str] = exercicios["Ombros"][intensidade]
    opcoes_costas: list[str] = exercicios["Costas"][intensidade]
    opcoes_biceps: list[str] = exercicios["Bíceps"][intensidade]
    opcoes_coxa: list[str] = exercicios["Coxa"][intensidade]
    opcoes_gluteos: list[str] = exercicios["Glúteos"][intensidade]
    opcoes_abdomen: list[str] = exercicios["Abdomên"][intensidade]
    opcoes_panturrilha: list[str] = exercicios["Panturrilha"][intensidade]
    
    disponibilidade: int = len(user.dias_disponiveis)
    
    if disponibilidade == 1:
            prompt = f"""Imagine que você é um personal trainer que precisa selecionar exercícios para um cliente. Escolha a quantidade indicada de exercícios entre os listados a seguir para cada grupo muscular:
            Escolha 2 exercícios de peito entre esses: {", ".join(opcoes_peito)}
            Escolha 1 exercício de ombro entre esses: {", ".join(opcoes_ombros)}
            Escolha 2 exercícios de costas entre esses: {", ".join(opcoes_costas)}
            Escolha 1 exercício de bíceps entre esses: {", ".join(opcoes_biceps)}
            Escolha 1 exercício de tríceps entre esses: {", ".join(opcoes_triceps)}
            Escolha 2 exercícios de coxas entre esses: {", ".join(opcoes_coxa)}
            
            Escreve sua resposta seguindo essa formatação, seguindo a mesma ordem citada anteriormente e com as escolhas entre aspas(por exemplo, "Supino", "fly"):
            
            [escolha1, escolha2..., escolhaN]
            """
    elif disponibilidade == 2:
        prompt = f"""Imagine que você é um personal trainer que precisa selecionar exercícios para um cliente. Escolha a quantidade indicada de exercícios entre os listados a seguir para cada grupo muscular, os exercícios serão separados entre dois dias de treino, A e B, que serão indicados no inicio de cada linha:
        (A)Escolha 2 exercícios de peito entre esses: {", ".join(opcoes_peito)}
        (A)Escolha 1 exercício de ombro entre esses: {", ".join(opcoes_ombros)}
        (A)Escolha 2 exercícios de costas entre esses: {", ".join(opcoes_costas)}
        (A)Escolha 1 exercício de bíceps entre esses: {", ".join(opcoes_biceps)}
        (A)Escolha 1 exercício de tríceps entre esses: {", ".join(opcoes_triceps)}
        (B)Escolha 3 exercícios de coxas entre esses: {", ".join(opcoes_coxa)}
        (B)Escolha 2 exercícios de panturrilha entre esses: {", ".join(opcoes_panturrilha)}
        (B)Escolha 1 exercício de abdomên entre esses: {", ".join(opcoes_abdomen)}
        (B)Escolha 1 exercício de glúteos entre esses: {", ".join(opcoes_gluteos)}
        
        Escreve sua resposta seguindo essa formatação(as escolhas do treino A entre colchetes, seguido de um hashtag, então as escolhas do treino B entre colchetes), seguindo a mesma ordem citada anteriormente e com as escolhas entre aspas(por exemplo, "Supino", "fly"):
        
        [escolha1A, escolha2A..., escolhaNA]#[escolha1B, escolha2B..., escolhaNB]
        """
    elif disponibilidade == 3 or disponibilidade == 6 or disponibilidade == 7:
        prompt = f"""Imagine que você é um personal trainer que precisa selecionar exercícios para um cliente. Escolha a quantidade indicada de exercícios entre os listados a seguir para cada grupo muscular, os exercícios serão separados entre três dias de treino, A, B e C, que serão indicados no inicio de cada linha:
        (A)Escolha 3 exercícios de peito entre esses: {", ".join(opcoes_peito)}
        (A)Escolha 3 exercícios de costas entre esses: {", ".join(opcoes_costas)}
        (A)Escolha 1 exercício de tríceps entre esses: {", ".join(opcoes_triceps)}
        (A)Escolha 1 exercício de bíceps entre esses: {", ".join(opcoes_biceps)}
        (B)Escolha 4 exercícios de ombro entre esses: {", ".join(opcoes_ombros)}
        (B)Escolha 2 exercícios de panturrilha entre esses: {", ".join(opcoes_panturrilha)}
        (C)Escolha 3 exercícios de tríceps entre esses: {", ".join(opcoes_triceps)}
        (C)Escolha 3 exercícios de bíceps entre esses: {", ".join(opcoes_biceps)}
        (D)Escolha 3 exercícios de coxas entre esses: {", ".join(opcoes_coxa)}
        (D)Escolha 1 exercício de panturrilha entre esses: {", ".join(opcoes_panturrilha)}
        (C)Escolha 1 exercício de glúteos entre esses: {", ".join(opcoes_gluteos)}
        
        Escreve sua resposta seguindo essa formatação(as escolhas do treino A entre colchetes, seguido de um hashtag, então as escolhas do treino B entre colchetes, etc), seguindo a mesma ordem citada anteriormente e com as escolhas entre aspas(por exemplo, "Supino", "fly"):
        
        [escolha1A, escolha2A..., escolhaNA]#[escolha1B, escolha2B..., escolhaNB]#[escolha1C, escolha2C..., escolhaNC]
        """
    elif disponibilidade == 4:
        prompt = f"""Imagine que você é um personal trainer que precisa selecionar exercícios para um cliente. Escolha a quantidade indicada de exercícios entre os listados a seguir para cada grupo muscular, os exercícios serão separados entre quatro dias de treino, A, B, C e D, que serão indicados no inicio de cada linha:
        (A)Escolha 5 exercícios de peito entre esses: {", ".join(opcoes_peito)}
        (A)Escolha 2 exercícios de ombro entre esses: {", ".join(opcoes_ombros)}
        (B)Escolha 5 exercícios de costas entre esses: {", ".join(opcoes_costas)}
        (B)Escolha 1 exercício de abdomên entre esses: {", ".join(opcoes_abdomen)}
        (C)Escolha 4 exercícios de coxas entre esses: {", ".join(opcoes_coxa)}
        (C)Escolha 2 exercício de panturrilha entre esses: {", ".join(opcoes_panturrilha)}
        (C)Escolha 1 exercício de glúteos entre esses: {", ".join(opcoes_gluteos)}
        (D)Escolha 4 exercícios de bíceps entre esses: {", ".join(opcoes_biceps)}
        (D)Escolha 4 exercícios de tríceps entre esses: {", ".join(opcoes_triceps)}
        
        Escreve sua resposta seguindo essa formatação(as escolhas do treino A entre colchetes, seguido de um hashtag, então as escolhas do treino B entre colchetes, etc), seguindo a mesma ordem citada anteriormente e com as escolhas entre aspas(por exemplo, "Supino", "fly"):
        
        [escolha1A, escolha2A..., escolhaNA]#[escolha1B, escolha2B..., escolhaNB]#[escolha1C, escolha2C..., escolhaNC]#[escolha1D, escolha2D..., escolhaND]
        """
    elif disponibilidade == 5:
        prompt = f"""Imagine que você é um personal trainer que precisa selecionar exercícios para um cliente. Escolha a quantidade indicada de exercícios entre os listados a seguir para cada grupo muscular, os exercícios serão separados entre quatro dias de treino, A, B, C e D, que serão indicados no inicio de cada linha:
        (A)Escolha 3 exercícios de peito entre esses: {", ".join(opcoes_peito)}
        (B)Escolha 3 exercícios de costas entre esses: {", ".join(opcoes_costas)}
        (C)Escolha 3 exercícios de coxas entre esses: {", ".join(opcoes_coxa)}
        (C)Escolha 1 exercício de panturrilha entre esses: {", ".join(opcoes_panturrilha)}
        (C)Escolha 1 exercício de glúteos entre esses: {", ".join(opcoes_gluteos)}
        (D)Escolha 3 exercícios de bíceps entre esses: {", ".join(opcoes_biceps)}
        (D)Escolha 2 exercícios de tríceps entre esses: {", ".join(opcoes_triceps)}
        (E)Escolha 3 exercícios de ombro entre esses: {", ".join(opcoes_ombros)}
        (E)Escolha 1 exercício de abdomên entre esses: {", ".join(opcoes_abdomen)}
        
        Escreve sua resposta seguindo essa formatação(as escolhas do treino A entre colchetes, seguido de um hashtag, então as escolhas do treino B entre colchetes, etc), seguindo a mesma ordem citada anteriormente e com as escolhas entre aspas(por exemplo, "Supino", "fly"):
        
        [escolha1A, escolha2A..., escolhaNA]#[escolha1B, escolha2B..., escolhaNB]#[escolha1C, escolha2C..., escolhaNC]#[escolha1D, escolha2D..., escolhaND]#[escolha1E, escolha2E..., escolhaNE]
        """

    return prompt