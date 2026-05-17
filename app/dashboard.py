import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import os

# 1. Configuração da Página do Streamlit
st.set_page_config(
    page_title="Dashboard Olist - E-commerce Performance",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilização customizada em CSS para os KPIs
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        padding: 15px 20px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        border: 1px solid #e9ecef;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Carregamento Otimizado dos Dados (Cache)
@st.cache_data
def load_data():
    # Caminho configurado com base no script de ETL (pasta output)
    db_path = os.path.join('output', 'olist_analitico.db')
    
    if not os.path.exists(db_path):
        st.error(f"Banco de dados não localizado em: {db_path}. Execute o script de ETL primeiro.")
        return pd.DataFrame()
        
    conn = sqlite3.connect(db_path)
    
    # Consulta a tabela criada no seu processo de ETL
    query = "SELECT * FROM vendas_completas"
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Conversões e tratamentos adicionais de data necessários para os gráficos
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['ano'] = df['order_purchase_timestamp'].dt.year
    
    # Cálculo real do tempo de entrega efetivo (Dias)
    df['dias_entrega_real'] = (df['order_delivered_customer_date'] - df['order_purchase_timestamp']).dt.days
    
    return df

# Inicialização do dataframe
df = load_data()

if df.empty:
    st.warning("Aguardando carregamento correto da tabela 'vendas_completas'.")
else:
    # 3. Barra Lateral (Sidebar) para Filtros Dinâmicos
    st.sidebar.header("📌 Filtros do Dashboard")
    
    # Filtro de Ano baseado no timestamp de compra
    anos_disponiveis = sorted(df['ano'].dropna().unique())
    anos_selecionados = st.sidebar.multiselect("Selecione o Ano:", anos_disponiveis, default=anos_disponiveis)
    df_filtrado = df[df['ano'].isin(anos_selecionados)]

    # Filtro de Região por Estado do Cliente (customer_state)
    estados_disponiveis = sorted(df_filtrado['customer_state'].dropna().unique())
    estados_selecionados = st.sidebar.multiselect("Selecione os Estados (UF):", estados_disponiveis, default=estados_disponiveis)
    if estados_selecionados:
        df_filtrado = df_filtrado[df_filtrado['customer_state'].isin(estados_selecionados)]

    # Filtro por Categoria de Produto (tratada e padronizada pelo ETL)
    categorias_disponiveis = sorted(df_filtrado['product_category_name'].dropna().unique())
    categorias_selecionadas = st.sidebar.multiselect("Filtrar por Categoria:", categorias_disponiveis)
    if categorias_selecionadas:
        df_filtrado = df_filtrado[df_filtrado['product_category_name'].isin(categorias_selecionadas)]

    # 4. Cabeçalho Principal do Dashboard
    st.title("📊 Análise de Desempenho de Vendas (E-Commerce Olist)")
    st.markdown("### Ciência de Dados e Ferramentas Low Code para Geração de Insights")
    st.markdown("---")

    # 5. KPIs Principais do Negócio (Métricas)
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        # Faturamento Total baseado no preço do item
        venda_total = df_filtrado['price'].sum() if 'price' in df_filtrado.columns else 0
        st.metric(label="💰 Faturamento Total", value=f"R$ {venda_total:,.2f}")
        
    with col2:
        # Total de Pedidos únicos (removendo duplicadas criadas por múltiplos itens ou pagamentos)
        total_pedidos = df_filtrado['order_id'].nunique()
        st.metric(label="📦 Total de Pedidos", value=f"{total_pedidos:,}")
        
    with col3:
        # Ticket Médio real do E-commerce
        ticket_medio = venda_total / total_pedidos if total_pedidos > 0 else 0
        st.metric(label="🎯 Ticket Médio", value=f"R$ {ticket_medio:,.2f}")
        
    with col4:
        # Nota média de satisfação dos clientes
        nota_media = df_filtrado['review_score'].mean() if 'review_score' in df_filtrado.columns else 0
        st.metric(label="⭐ Avaliação Média", value=f"{nota_media:.2f} / 5.00")
        
    with col5:
        # Prazo Estimado Médio calculado pelo ETL
        prazo_medio = df_filtrado['prazo_entrega_estimado'].mean() if 'prazo_entrega_estimado' in df_filtrado.columns else 0
        st.metric(label="📅 Prazo Estimado Médio", value=f"{prazo_medio:.1f} Dias")

    st.markdown("---")

    # 6. Criação das Abas para Organização das Visões de Negócio
    tab_comercial, tab_logistica, tab_produtos = st.tabs([
        "📈 Performance Comercial", 
        "🚚 Logística e Entregas", 
        "🛍️ Análise de Produtos"
    ])

    # --- ABA 1: PERFORMANCE COMERCIAL ---
    with tab_comercial:
        st.subheader("Evolução Mensal do Faturamento e Pagamentos")
        c1, c2 = st.columns(2)
        
        with c1:
            # Gráfico de Linha com base na coluna 'ano_mes_compra' gerada no seu ETL
            faturamento_temporal = df_filtrado.groupby('ano_mes_compra')['price'].sum().reset_index()
            faturamento_temporal = faturamento_temporal.sort_values('ano_mes_compra')
            
            fig_linha = px.line(
                faturamento_temporal, x='ano_mes_compra', y='price',
                title="Evolução do Faturamento ao Longo do Tempo",
                labels={'ano_mes_compra': 'Mês da Compra', 'price': 'Faturamento (R$)'},
                markers=True, template="plotly_white", color_discrete_sequence=['#1f77b4']
            )
            st.plotly_chart(fig_linha, use_container_width=True)
                
        with c2:
            # Gráfico de Rosca mostrando os tipos de pagamento preferidos pelos clientes
            if 'payment_type' in df_filtrado.columns:
                pagamentos = df_filtrado['payment_type'].value_counts().reset_index()
                pagamentos.columns = ['Tipo de Pagamento', 'Quantidade']
                
                fig_pizza = px.pie(
                    pagamentos, names='Tipo de Pagamento', values='Quantidade',
                    title="Distribuição das Formas de Pagamento",
                    hole=0.4, template="plotly_white"
                )
                st.plotly_chart(fig_pizza, use_container_width=True)

    # --- ABA 2: LOGÍSTICA E ENTREGAS ---
    with tab_logistica:
        st.subheader("Análise de Distribuição Geográfica e Prazos")
        c3, c4 = st.columns(2)
        
        with c3:
            # Gráfico de Barras do volume de pedidos únicos agrupados por estado (customer_state)
            vendas_por_estado = df_filtrado.groupby('customer_state')['order_id'].nunique().reset_index()
            vendas_por_estado.columns = ['Estado (UF)', 'Volume de Pedidos']
            vendas_por_estado = vendas_por_estado.sort_values('Volume de Pedidos', ascending=False)
            
            fig_barra_uf = px.bar(
                vendas_por_estado, x='Estado (UF)', y='Volume de Pedidos',
                title="Concentração e Volume de Pedidos por Estado (UF)",
                color='Volume de Pedidos', color_continuous_scale='Blugrn',
                template="plotly_white"
            )
            st.plotly_chart(fig_barra_uf, use_container_width=True)
                
        with c4:
            # Cruzamento entre a nota de avaliação e o tempo real que a entrega levou
            if 'review_score' in df_filtrado.columns:
                satisfacao_entrega = df_filtrado.groupby('review_score')['dias_entrega_real'].mean().reset_index()
                
                fig_SLA = px.bar(
                    satisfacao_entrega, x='review_score', y='dias_entrega_real',
                    title="Tempo Médio Real de Entrega (Dias) vs. Nota de Satisfação",
                    labels={'review_score': 'Nota de Avaliação (Review)', 'dias_entrega_real': 'Média de Dias Conclusão'},
                    template="plotly_white", color='dias_entrega_real', color_continuous_scale='Reds'
                )
                st.plotly_chart(fig_SLA, use_container_width=True)

    # --- ABA 3: ANÁLISE DE PRODUTOS ---
    with tab_produtos:
        st.subheader("Desempenho de Categorias Mais Vendidas")
        c5, c6 = st.columns(2)
        
        # Agrupamento e identificação do Top 10 categorias com maior faturamento
        top_categorias = df_filtrado.groupby('product_category_name')['price'].agg(['sum', 'count']).reset_index()
        top_categorias.columns = ['Categoria', 'Faturamento Total', 'Quantidade de Itens']
        top_categorias = top_categorias.sort_values('Faturamento Total', ascending=False).head(10)
        
        with c5:
            # Gráfico de barras horizontal mostrando faturamento por categoria
            fig_cat_fat = px.bar(
                top_categorias, y='Categoria', x='Faturamento Total',
                title="Top 10 Categorias por Faturamento (R$)",
                orientation='h', color='Faturamento Total', color_continuous_scale='Viridis',
                template="plotly_white"
            )
            fig_cat_fat.update_layout(yaxis={'categoryorder':'total ascending'})
            st.plotly_chart(fig_cat_fat, use_container_width=True)
            
        with c6:
            # Gráfico de barras vertical mostrando volume de itens vendidos
            fig_cat_qtd = px.bar(
                top_categorias.sort_values('Quantidade de Itens', ascending=False), 
                x='Categoria', y='Quantidade de Itens',
                title="Volume de Itens Vendidos nas Maiores Categorias",
                labels={'Quantidade de Itens': 'Qtd de Itens Comercializados'},
                template="plotly_white", color_discrete_sequence=['#ff7f0e']
            )
            st.plotly_chart(fig_cat_qtd, use_container_width=True)

    # 7. Rodapé com os créditos do grupo conforme escopo do README
    st.markdown("---")
    st.caption("🚀 Projeto Integrador desenvolvido por: Juliana Alves, Luis Augusto, Guilherme Silva e Matheus de Oliveira.")