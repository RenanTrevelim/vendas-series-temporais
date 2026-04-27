import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Previsão de Vendas - Séries Temporais",
    layout="wide"
)

st.title("📊 Análise e Previsão de Vendas com Séries Temporais")

st.markdown("""
Este projeto analisa uma série temporal mensal de vendas, identifica tendência,
sazonalidade e compara modelos de previsão para apoiar decisões de negócio.
""")

# =========================
# Carregar dados e modelo
# =========================

@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/dados_vendas.csv")
    df["data"] = pd.to_datetime(df["data"])
    df = df.set_index("data")
    return df


@st.cache_resource
def carregar_modelo():
    modelo = joblib.load("models/modelo_sarima.pkl")
    return modelo


df = carregar_dados()
modelo_sarima = carregar_modelo()

# =========================
# Sidebar
# =========================

st.sidebar.title("Navegação")

pagina = st.sidebar.radio(
    "Escolha uma seção:",
    [
        "Visão Geral",
        "Análise Exploratória",
        "Modelos",
        "Previsão Final",
        "Impacto Financeiro"
    ]
)

# =========================
# Visão Geral
# =========================

if pagina == "Visão Geral":
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Período inicial", df.index.min().strftime("%b/%Y"))
    col2.metric("Período final", df.index.max().strftime("%b/%Y"))
    col3.metric("Média de vendas", round(df["vendas"].mean(), 2))
    col4.metric("Total vendido", round(df["vendas"].sum(), 0))

    fig = px.line(
        df,
        x=df.index,
        y="vendas",
        title="Série Temporal de Vendas"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(df, use_container_width=True)

# =========================
# Análise Exploratória
# =========================

elif pagina == "Análise Exploratória":
    st.subheader("📈 Média móvel")

    df_eda = df.copy()
    df_eda["media_movel_3"] = df_eda["vendas"].rolling(3).mean()

    fig = px.line(
        df_eda,
        x=df_eda.index,
        y=["vendas", "media_movel_3"],
        title="Vendas x Média Móvel de 3 Meses"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("📅 Sazonalidade por mês")

    df_aux = df.copy()
    df_aux["mes_num"] = df_aux.index.month

    meses_pt = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    df_aux["mes"] = df_aux["mes_num"].map(meses_pt)

    media_mes = (
        df_aux
        .groupby(["mes_num", "mes"])["vendas"]
        .mean()
        .reset_index()
        .sort_values("mes_num")
    )

    fig_mes = px.bar(
        media_mes,
        x="mes",
        y="vendas",
        title="Média de Vendas por Mês"
    )

    fig_mes.update_layout(
        xaxis_title="Mês",
        yaxis_title="Vendas Médias"
    )

    st.plotly_chart(fig_mes, use_container_width=True)

    st.subheader("📊 Estatísticas descritivas")
    st.dataframe(df["vendas"].describe(), use_container_width=True)

# =========================
# Modelos
# =========================

elif pagina == "Modelos":
    st.subheader("🤖 Comparação dos Modelos")

    resultados = pd.DataFrame({
        "Modelo": [
            "Holt-Winters",
            "ARIMA(1,1,0)",
            "SARIMA(1,1,0)(1,1,0,12)",
            "Random Forest",
            "Regressão Linear"
        ],
        "MAE": [9.29, 36.63, 8.04, 21.29, 11.71],
        "RMSE": [11.13, 41.95, 11.68, 26.40, 14.25],
        "MAPE (%)": [3.42, 12.63, 2.93, 7.32, 4.15]
    })

    st.dataframe(resultados, use_container_width=True)

    metrica = st.selectbox(
        "Escolha a métrica para comparação:",
        ["MAE", "RMSE", "MAPE (%)"]
    )

    fig = px.bar(
        resultados,
        x="Modelo",
        y=metrica,
        title=f"Comparação dos Modelos por {metrica}"
    )

    st.plotly_chart(fig, use_container_width=True)

    melhor_modelo = resultados.sort_values(metrica).iloc[0]["Modelo"]
    menor_erro = resultados.sort_values(metrica).iloc[0][metrica]

    st.success(
        f"O modelo {melhor_modelo} apresentou o menor {metrica}: {menor_erro:.2f}."
    )

# =========================
# Previsão Final
# =========================

elif pagina == "Previsão Final":
    st.subheader("🔮 Previsão de Vendas")

    periodos = st.slider(
        "Quantidade de meses para prever:",
        min_value=1,
        max_value=24,
        value=12
    )

    previsao_futura = modelo_sarima.predict(
        start=len(df),
        end=len(df) + periodos - 1
    )

    datas_futuras = pd.date_range(
        start=df.index.max() + pd.DateOffset(months=1),
        periods=periodos,
        freq="MS"
    )

    previsao_df = pd.DataFrame({
        "data": datas_futuras,
        "previsao_vendas": previsao_futura.values
    })

    fig = px.line(
        df,
        x=df.index,
        y="vendas",
        title="Histórico de Vendas + Previsão"
    )

    fig.add_scatter(
        x=previsao_df["data"],
        y=previsao_df["previsao_vendas"],
        mode="lines+markers",
        name="Previsão"
    )

    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(previsao_df, use_container_width=True)

# =========================
# Impacto Financeiro
# =========================

elif pagina == "Impacto Financeiro":
    st.subheader("💰 Projeção de Receita")

    preco_medio = st.number_input(
        "Preço médio por venda",
        min_value=0.0,
        value=650.0,
        step=50.0
    )

    periodos = st.slider(
        "Quantidade de meses para projeção:",
        min_value=1,
        max_value=24,
        value=12
    )

    previsao_futura = modelo_sarima.predict(
        start=len(df),
        end=len(df) + periodos - 1
    )

    receita_prevista = previsao_futura.sum() * preco_medio
    receita_ultimo_ano = df["vendas"].tail(12).sum() * preco_medio

    diferenca = receita_prevista - receita_ultimo_ano

    if receita_ultimo_ano != 0:
        crescimento = (diferenca / receita_ultimo_ano) * 100
    else:
        crescimento = 0

    col1, col2, col3 = st.columns(3)

    col1.metric("Receita último ano", f"R$ {receita_ultimo_ano:,.2f}")
    col2.metric("Receita prevista", f"R$ {receita_prevista:,.2f}")
    col3.metric("Crescimento estimado", f"{crescimento:.2f}%")

    st.info(
        "Essa seção traduz a previsão de vendas em impacto financeiro, "
        "facilitando a tomada de decisão."
    )