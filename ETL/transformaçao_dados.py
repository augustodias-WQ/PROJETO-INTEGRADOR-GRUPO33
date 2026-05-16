import pandas as pd
import os

pasta_origem = "dados_brutos"
print("Iniciando a transformação dos dados...")

print("Carregando as tabelas no Pandas...")
df_pedidos = pd.read_csv(os.path.join(pasta_origem, 'olist_orders_dataset.csv'))
df_clientes = pd.read_csv(os.path.join(pasta_origem, 'olist_customers_dataset.csv'))
df_pagamentos = pd.read_csv(os.path.join(pasta_origem, 'olist_order_payments_dataset.csv'))

print("Cruzando dados de pedidos, clientes e pagamentos...")

df_vendas = pd.merge(df_pedidos, df_clientes, on='customer_id')

df_consolidado = pd.merge(df_vendas, df_pagamentos, on='order_id')

df_consolidado['order_purchase_timestamp'] = pd.to_datetime(df_consolidado['order_purchase_timestamp'])

colunas_essenciais = [
    'order_id', 'customer_unique_id', 'customer_city', 'customer_state',
    'order_purchase_timestamp', 'payment_value', 'payment_type'
]
df_final = df_consolidado[colunas_essenciais]

print("\n--- PROCESSO DE TRANSFORMAÇÃO CONCLUÍDO ---")
print(f"Total de linhas processadas com sucesso: {len(df_final)}")
print("\nAmostra dos dados estruturados:")
print(df_final.head(3))

import sqlite3

print("\nIniciando o processo de Carga dos dados no banco estruturado SQLite...")

pasta_destino_banco_dados = "dados_processados"
if not os.path.exists(pasta_destino_banco_dados):
    os.makedirs(pasta_destino_banco_dados)
    
conexao = sqlite3.connect(os.path.join(pasta_destino_banco_dados, "olist_estruturado.db"))

df_final.to_sql("vendas_tratadas", conexao, if_exists="replace", index=False)

conexao.close()

print("Processo de ETL finalizado")
print("Arquivo 'olist_estruturado.db' gerado com sucesso dentro de 'dados_processados' e pronto para o Streamlit!")