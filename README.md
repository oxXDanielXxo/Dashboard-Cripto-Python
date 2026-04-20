# 📈 Dashboard Financeiro: Mercado de Criptomoedas

Um terminal financeiro interativo desenvolvido em Python para monitoramento de ativos em tempo real, com foco no mercado de criptomoedas. 

🔴 **[CLIQUE AQUI PARA ACESSAR O DASHBOARD AO VIVO](https://daniel-dashboard-cripto.streamlit.app/)**

## ⚙️ Tecnologias Utilizadas (Arsenal)
* **Linguagem:** Python
* **Interface Web:** Streamlit (Deploy em Nuvem via Streamlit Community Cloud)
* **Processamento de Dados:** Pandas
* **Visualização:** Plotly (Gráficos interativos de Velas/Candlestick)
* **Integração de API:** yFinance (Consumo de dados em tempo real do Yahoo Finance)

## 🚀 Funcionalidades (Features)
* Busca automatizada de dados históricos e em tempo real.
* Seleção dinâmica de ativos (BTC, ETH, SOL, BNB).
* Filtros de período temporal personalizados (1 mês, 6 meses, 1 ano, etc).
* Cálculo automático de variação percentual e valor bruto.
* Renderização de gráficos financeiros padrão "Wall Street" (Candlestick) com suporte a zoom e *hover* interativo.

## 🧠 Arquitetura do Sistema
O sistema opera através de requisições HTTP para a API do Yahoo Finance, armazenando o retorno JSON em DataFrames do Pandas. Os dados são limpos e estruturados para alimentar o motor de renderização do Plotly, enquanto o Streamlit gerencia os estados (State Management) da interface do usuário sem a necessidade de recarregamento da página (Single Page Application concept).
