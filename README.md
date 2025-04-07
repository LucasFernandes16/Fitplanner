
# 🏋️‍♂️ FitPlanner AI

FitPlanner AI é um aplicativo inteligente que monta treinos personalizados para os usuários. Desenvolvido com foco em usabilidade e personalização, o app visa facilitar a criação de treinos adequados ao perfil e objetivo de cada pessoa.

---

## 🚀 Funcionalidades

- Geração de treinos personalizados
- Armazenamento local dos treinos criados
- Interface moderna e responsiva com Next.js
- Backend em Python para lógica de geração de treinos

---

## 🛠️ Tecnologias Utilizadas

### Frontend
- [Next.js](https://nextjs.org/)

### Backend
- [Python 3.x](https://www.python.org/)

### Banco de Dados
- Ainda não implementado

---

## 📦 Instalação e Execução

### Pré-requisitos

- Node.js (versão mais recente recomendada)
- Python 3.x
- `npm` (gerenciador de pacotes do Node)

### Instalação

#### 1. Clone o repositório
```bash
git clone https://github.com/LucasFernandes16/Fitplanner.git
cd Fitplanner
```

#### 2. Instale as dependências do frontend
```bash
cd front-fitplanner
npm install
```

#### 3. Instale as dependências do backend
```bash
cd ../back-fitplanner
pip install -r requirements.txt
```

### Execução

#### Iniciar frontend
```bash
cd front-fitplanner
npm start
```

#### Iniciar backend
```bash
cd ../back-fitplanner
python app.py  # ou o nome do arquivo principal
```

---

## 📂 Estrutura do Projeto

```
Fitplanner/
├── front-fitplanner/     # Aplicação Frontend (Next.js)
├── back-fitplanner/      # Aplicação Backend (Python)
├── README.md              # Este arquivo
├── .gitignore             # Arquivos ignorados pelo Git
└── LICENSE                # Licença do projeto (MIT)
```

---

## 🧪 Testes

> No momento, o projeto ainda **não possui testes automatizados**. Testes manuais podem ser realizados interagindo com o frontend e verificando a geração dos treinos personalizados.

---

## 🤝 Contribuidores

Este projeto foi desenvolvido por alunos da disciplina de **Desenvolvimento de Software**:

- Lucas Fernandes ([@LucasFernandes16](https://github.com/LucasFernandes16))  
- Tiago Quaresma  
- Cesar Cavalcanti  
- Gabriel Campelo  
- Gabriel Carneiro

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [`LICENSE`](./LICENSE) para mais informações.

---

## 💡 Futuras Melhorias

- Implementação de banco de dados para persistência
- Testes automatizados
- Integração com mapas e localização para sugerir locais de treino
- Integração com profissionais da área para recomendações

---

Feito com 💪 por alunos apaixonados por tecnologia e saúde!
