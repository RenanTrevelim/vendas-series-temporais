# 📊 Previsão de Vendas com Séries Temporais

Este projeto aplica técnicas de **análise de séries temporais** e **machine learning** para prever vendas mensais, identificar padrões e apoiar decisões de negócio.

A aplicação foi desenvolvida com **Streamlit**, transformando a análise em um dashboard interativo.

---

## 📸 Preview do Dashboard

> 📌 Adicione aqui um print ou GIF

![Dashboard](./assets/dashboard.png)

---

## 🚀 Objetivo

- Analisar o comportamento histórico das vendas  
- Identificar **tendência** e **sazonalidade**  
- Comparar diferentes modelos de previsão  
- Gerar previsões futuras  
- Traduzir resultados em **impacto financeiro**  

---

## 📊 Estrutura dos Dados

| data       | vendas |
|------------|--------|
| 2020-01-01 | 200    |
| 2020-02-01 | 210    |

- Frequência: Mensal  
- Variável alvo: `vendas`

---

## 🧠 Técnicas Utilizadas

- Análise exploratória de dados (EDA)
- Decomposição de séries temporais
- Média móvel

### Modelos Estatísticos
- Holt-Winters
- ARIMA
- SARIMA

### Machine Learning
- Regressão Linear
- Random Forest

### Métricas de Avaliação
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- MAPE (Mean Absolute Percentage Error)

---

## 🏆 Resultados

O modelo **SARIMA** apresentou o melhor desempenho, com menor erro entre os modelos testados.

Isso indica que a série possui:

- Sazonalidade forte  
- Dependência temporal relevante  

---

## 💡 Insights

> 📌 Complete com base na sua análise

- 📈 Meses com maior volume de vendas: **[ex: Maio e Junho]**
- 📉 Meses com menor desempenho: **[ex: Outubro]**
- 🔁 Padrão sazonal identificado ao longo dos anos
- 📊 Tendência geral: **[crescimento / estabilidade / queda]**

---

## 📊 Dashboard Interativo

O dashboard possui as seguintes seções:

- 📌 Visão geral dos dados  
- 📈 Análise exploratória  
- 📅 Sazonalidade por mês  
- 🤖 Comparação de modelos  
- 🔮 Previsão futura  
- 💰 Projeção de receita  

---

## ⚡ Otimização do Projeto

O modelo foi previamente treinado e salvo em formato `.pkl`.

Isso permite:

- Execução mais rápida  
- Separação entre treino e inferência  
- Estrutura mais próxima de ambiente de produção  

---

## 🛠️ Tecnologias Utilizadas

- Python  
- pandas  
- numpy  
- plotly  
- statsmodels  
- scikit-learn  
- streamlit  

---

## 📁 Estrutura do Projeto

```text
vendas-series-temporais/
│
├── data/
│ └── dados_vendas.csv 
│
├── models/
│ └── modelo_sarima.pkl 
│
├── notebooks/
│ └── Modelo_Regressão-Séries_Temporais
│
├── main.py 
├── requirements.txt 
├── README.md 
└── .gitignore 
```

## 🚀 Como rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/RenanTrevelim/vendas-series-temporais.git
cd payflow-inadimplencia
```

### 2. Crie um ambiente virtual

```bash
python -m venv .venv
#source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate    # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação

```bash
streamlit run main.py
```

