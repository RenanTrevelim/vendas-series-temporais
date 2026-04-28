# 📊 Previsão de Vendas com Séries Temporais e Machine Learning

Projeto desenvolvido com foco na análise de comportamento de vendas ao longo do tempo e na construção de modelos capazes de **antecipar demanda futura**, apoiando decisões estratégicas e financeiras.

---

## 🎯 Objetivo do Projeto

O objetivo deste projeto é analisar padrões históricos de vendas e desenvolver modelos preditivos capazes de **gerar previsões confiáveis**, auxiliando o planejamento operacional e financeiro.

A partir disso, busca-se:

- Identificar tendência e sazonalidade  
- Entender padrões de comportamento ao longo do tempo  
- Comparar diferentes abordagens de modelagem  
- Gerar previsões futuras de vendas  
- Apoiar decisões com base em projeções financeiras  

---

## 📂 Descrição da Base de Dados

O dataset contém informações de vendas ao longo do tempo.

### 📊 Estrutura:

| data       | vendas |
|------------|--------|
| 2020-01-01 | 200    |
| 2020-02-01 | 210    |

- Frequência: Mensal  
- Variável alvo: `vendas`  

👉 Trata-se de uma **série temporal univariada**, onde o comportamento passado influencia diretamente o futuro.

---

## 🧠 Metodologia Utilizada

O projeto foi estruturado em etapas, seguindo um fluxo completo de análise de séries temporais.

---

### 1. Entendimento do problema  

Análise do contexto de negócio, considerando a necessidade de prever demanda futura para melhorar planejamento, estoque e projeções financeiras.

---

### 2. Análise Exploratória de Dados (EDA)

Foram investigados padrões temporais com foco em comportamento de vendas.

Principais análises realizadas:

- Evolução das vendas ao longo do tempo  
- Identificação de tendência  
- Análise de sazonalidade mensal  
- Avaliação de variações e picos  
- Uso de médias móveis para suavização  

👉 Principais insights identificados:

- Presença de padrão sazonal recorrente  
- Existência de tendência (crescimento ou estabilidade)  
- Períodos específicos com maior volume de vendas  
- Variações que impactam diretamente o planejamento  

---

### 3. Decomposição da Série Temporal

A série foi decomposta em componentes:

- Tendência  
- Sazonalidade  
- Resíduo  

👉 Essa etapa permitiu entender a estrutura do comportamento das vendas e orientar a escolha dos modelos.

---

### 4. Preparação dos Dados

Antes da modelagem, foram realizadas etapas de preparação:

- Garantia de ordenação temporal  
- Tratamento de valores ausentes  
- Criação de variáveis derivadas (lags e médias móveis, quando aplicável)  

---

### 5. Modelagem Preditiva

Foram testadas diferentes abordagens para previsão de séries temporais:

#### 📊 Modelos Estatísticos

- Holt-Winters  
- ARIMA  
- SARIMA  

#### 🤖 Modelos de Machine Learning

- Regressão Linear  
- Random Forest  

👉 Essa comparação permite avaliar diferentes formas de capturar padrões temporais.

---

### 6. Avaliação dos Modelos

Os modelos foram avaliados utilizando métricas adequadas para regressão:

- MAE (erro absoluto médio)  
- RMSE (erro quadrático médio)  
- MAPE (erro percentual médio)  

👉 O objetivo foi minimizar o erro e garantir previsões confiáveis.

---

### 7. Seleção do Modelo

O modelo **SARIMA** apresentou o melhor desempenho.

Motivos da escolha:

- Captura de sazonalidade  
- Modelagem da dependência temporal  
- Melhor desempenho nas métricas  

👉 Isso indica que a série possui forte estrutura temporal.

---

### 8. Geração de Previsões

O modelo final foi utilizado para:

- Projetar vendas futuras  
- Identificar tendências esperadas  
- Simular cenários de demanda  

---

### 9. Camada de Negócio

As previsões foram traduzidas em impacto prático:

- Estimativa de receita futura  
- Planejamento de estoque  
- Apoio a decisões comerciais  
- Antecipação de períodos de alta e baixa demanda  

👉 Transformando previsões em decisões estratégicas.

---

## 📊 Resultados do Modelo

O modelo selecionado demonstrou boa capacidade de previsão, capturando:

- Padrões sazonais recorrentes  
- Tendência da série  
- Variações ao longo do tempo  

---

### 🎯 Insights de Negócio

- Meses com maior volume de vendas apresentam padrão consistente  
- Períodos de baixa podem ser antecipados  
- A sazonalidade impacta diretamente o planejamento  
- A previsão permite decisões mais eficientes  

👉 O modelo permite reduzir incerteza e melhorar planejamento financeiro.

---

## 🖥️ Aplicação (Streamlit)

Foi desenvolvida uma aplicação interativa para exploração e previsão.

### Funcionalidades:

- Visualização da série histórica  
- Análise de tendência e sazonalidade  
- Comparação de modelos  
- Geração de previsões futuras  
- Projeção de receita  

👉 Interface voltada para análise e tomada de decisão.

---

## ⚡ Estrutura de Produção

O modelo foi treinado e salvo em formato `.pkl`, permitindo:

- Execução rápida  
- Separação entre treino e inferência  
- Uso em ambiente de produção  

---

## 🏁 Conclusão

O projeto evolui de uma análise temporal para uma ferramenta de previsão aplicada ao negócio.

Mais do que prever vendas, a solução permite:

- Antecipar demanda futura  
- Melhorar planejamento operacional  
- Apoiar decisões estratégicas  
- Reduzir incerteza financeira  

👉 Resultado: uso de séries temporais para transformar dados históricos em vantagem competitiva.

---

## ▶️ Como Reproduzir os Resultados

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

