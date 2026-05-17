import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Portal de Vendas Olist", layout="wide", page_icon="🛍️")

st.title("🛍️ Dashboard de Performance de Vendas (Olist)")
st.markdown("Análise de faturamento, volumetria de pedidos e logística por estado.")

def carregar_dados():    
    caminho_db = "dados_processados/olist_estruturado.db"
    
    if not os.path.exists(caminho_db):
        st.error(f"ERRO: O banco de dados não foi encontrado em {caminho_db}")
        return pd.DataFrame()
        
    conn = sqlite3.connect(caminho_db)
    df = pd.read_sql("SELECT * FROM vendas_tratadas", conn)
    conn.close()
    return df

df = carregar_dados()

if not df.empty:    
    st.sidebar.header("Filtros de Análise")
    estados = st.sidebar.multiselect("Selecione os Estados:", 
                                    options=df["customer_state"].unique(),
                                    default=df["customer_state"].unique()[:5])
    
    df_filtrado = df[df["customer_state"].isin(estados)]
    
    col1, col2, col3 = st.columns(3)
    
    faturamento = df_filtrado["payment_value"].sum()
    pedidos = df_filtrado["order_id"].nunique()
    ticket_medio = faturamento / pedidos if pedidos > 0 else 0

    col1.metric("💰 Faturamento Total", f"R$ {faturamento:,.2f}")
    col2.metric("📦 Total de Pedidos", f"{pedidos:,}")
    col3.metric("🎟️ Ticket Médio", f"R$ {ticket_medio:,.2f}")

    st.markdown("---")
    
    col_dir, col_esq = st.columns(2)

    with col_dir:
        st.subheader("💳 Faturamento por Meio de Pagamento")
        faturamento_pagamento = df_filtrado.groupby("payment_type")["payment_value"].sum().sort_values(ascending=False)
        st.bar_chart(faturamento_pagamento)

    with col_esq:
        st.subheader("🚚 Pedidos por Estado (Top 10)")
        pedidos_estado = df_filtrado.groupby("customer_state")["order_id"].count().sort_values(ascending=False).head(10)
        st.bar_chart(pedidos_estado)

    st.success("Dados atualizados com sucesso via SQLite!")