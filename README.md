# 🏥 Sistema de Predição de Doença Cardíaca

Este projeto é o trabalho final da disciplina de **Data Science**. Ele consiste em uma aplicação completa que utiliza Machine Learning para prever a probabilidade de um paciente possuir doença cardíaca com base em variáveis clínicas.

## 📋 Sobre o Projeto

O objetivo principal foi aplicar o ciclo completo de um projeto de ciência de dados: desde a análise exploratória e pré-processamento, passando pelo treinamento de múltiplos modelos, até a implantação (deploy) através de uma API com interface web.

### Funcionalidades
- **Relatório de Qualidade**: Inspeção automática de dados nulos e tipos de variáveis.
- **Análise Descritiva**: Visualizações estatísticas para entender o perfil dos pacientes.
- **Predição em Tempo Real**: Interface amigável para entrada de dados clínicos e recebimento imediato do diagnóstico preditivo.

---

## 🛠️ Tecnologias Utilizadas

### **Data Science & Machine Learning**
- **Python 3.x**: Linguagem base.
- **Pandas & Numpy**: Manipulação e tratamento de dados.
- **Scikit-Learn**: Treinamento dos modelos e métricas de avaliação.
- **Matplotlib & Seaborn**: Geração de gráficos e análise visual.
- **Joblib**: Persistência (exportação) do modelo treinado.

### **Backend**
- **Flask**: Framework web para criação da API e rotas do sistema.
- **Jinja2**: Motor de templates para renderização dinâmica do HTML.

### **Frontend**
- **HTML5 & CSS3**: Estrutura e estilização da interface, com design responsivo.

---

## 🚀 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação na sua máquina local:

### 1. Pré-requisitos
Certifique-se de ter o **Python** instalado. Você pode verificar digitando `python --version` no seu terminal.

### 2. Clonar o Repositório
```bash
git clone https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git
cd NOME_DO_REPOSITORIO
```

### 3. Instalar Depêndencias
```bash
pip install flask joblib numpy scikit-learn pandas
```

### 4. Executar a Aplicação
```bash
python app.py
```
### 5. Acessar a Interface
Após iniciar o servidor, abra o seu navegador e acesse: http://localhost:5000

---

## 📁 Estrutura de Pastas
```
├── app.py              # Servidor Flask (Rotas da API)
├── classifier.py       # Lógica de carregamento do modelo e predição
├── heart-disease.csv   # Base de dados original
├── requirements.txt    # Lista de bibliotecas necessárias
├── .gitignore          # Arquivos ignorados pelo Git (ex: __pycache__)
├── models/
│   └── modelo_cardiaco.pkl  # Modelo treinado exportado
├── templates/
│   └── index.html      # Interface web (HTML + Jinja2)
└── static/
    └── style.css       # Estilização da interface
```

---

## 👥 Integrantes da Equipe
- Arthur Filipe Rodrigues da Silva (arthur.filipe2402@gmail.com)
- Filipe Xavier dos Santos (xfilipe2006.santos@gmail.com)
- Maria Cecília de Lima e Silva (cecilmari33@gmail.com)
- Maria Clara Moutinho Albuquerque Silva (moutinhomaria2910@gmail.com)
- Maria Eduarda Pereira Vilarim (vilarim051@gmail.com)

---

## ⚠️ Aviso Legal
Este software foi desenvolvido para fins estritamente acadêmicos. As predições geradas não substituem a avaliação de um profissional de saúde qualificado.
