import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# 1. Configuração inicial da página web (layout largo)
st.set_page_config(page_title="Dashboard Cripto", layout="wide")

st.title("🚀 Terminal Financeiro - Visão Global")
st.markdown("Monitoramento de ativos em tempo real consumindo a API do Yahoo Finance.")
st.divider()

# ======== NOVA BASE DE CONTROLE (SIDEBAR) ========
st.sidebar.header("Painel de Controle")

# Menu suspenso para escolher a moeda
cripto_selecionada = st.sidebar.selectbox(
    "Selecione a Criptomoeda",
    ("BTC-USD", "ETH-USD", "SOL-USD", "BNB-USD")
)

# Menu suspenso para escolher o período de tempo
periodo_selecionado = st.sidebar.selectbox(
    "Período de Análise",
    ("1mo", "3mo", "6mo", "1y", "ytd")
)
# =================================================

# 2. Motor de busca atualizado para aceitar as escolhas do usuário
def carregar_dados(ticker, periodo):
    ativo = yf.Ticker(ticker)
    # ======== CORREÇÃO AQUI ========
    # Mudamos period=period para period=periodo
    historico = ativo.history(period=periodo) 
    # ===============================
    return historico

# 3. Processamento e Exibição Visual
st.subheader(f"Análise de Mercado: {cripto_selecionada}")

# Carrega os dados baseado no que o usuário escolheu na barra lateral
df = carregar_dados(cripto_selecionada, periodo_selecionado)

if not df.empty:
    # Matemática para descobrir se o preço subiu ou desceu desde ontem
    preco_atual = df['Close'].iloc[-1]
    preco_anterior = df['Close'].iloc[-2]
    variacao = preco_atual - preco_anterior
    porcentagem = (variacao / preco_anterior) * 100

    # Cria a métrica avançada (fica verde se subir, vermelho se cair)
    st.metric(label=f"Preço Atual ({cripto_selecionada})", 
              value=f"${preco_atual:,.2f}", 
              delta=f"${variacao:,.2f} ({porcentagem:.2f}%)")
    
    # ======== O GRÁFICO PROFISSIONAL (PLOTLY) ========
    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    # Melhorando o visual do gráfico
    fig.update_layout(title=f"Gráfico de Velas - {periodo_selecionado}",
                      xaxis_title="Data",
                      yaxis_title="Preço (USD)",
                      template="plotly_dark", # Tema escuro
                      xaxis_rangeslider_visible=False) # Remove a barra extra embaixo para ficar mais limpo

    # Manda o Streamlit desenhar o gráfico interativo na tela
    st.plotly_chart(fig, use_container_width=True)
    # =================================================

else:
    st.error("Falha na comunicação com a API. Tente outro ativo ou período.")