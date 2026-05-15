import pandas as pd
import os
import sqlite3

# Pastas e banco de dados 
data_path = 'data'
output_path = 'output'
db_path = os.path.join(output_path, 'olist_analitico.db')

# Carregando os arquivos 
print("Carregando dados...")
orders = pd.read_csv(os.path.join(data_path, 'olist_orders_dataset.csv'))
items = pd.read_csv(os.path.join(data_path, 'olist_order_items_dataset.csv'))
customers = pd.read_csv(os.path.join(data_path, 'olist_customers_dataset.csv'))
products = pd.read_csv(os.path.join(data_path, 'olist_products_dataset.csv'))
payments = pd.read_csv(os.path.join(data_path, 'olist_order_payments_dataset.csv'))

# Unindo as tabelas (Merge)
print("Iniciando união de arquvos...")

# Pedidos + Itens + Clientes
df_final = pd.merge(orders, items, on='order_id', how='inner')
df_final = pd.merge(df_final, customers, on='customer_id', how='inner')

# Adicionando detalhes dos produtos e pagamentos
df_final = pd.merge(df_final, products, on='product_id', how='left')
df_final = pd.merge(df_final, payments, on='order_id', how='left')

# Tratamento de valores nulos e inconsistentes
df_final = df_final.dropna(subset=['order_delivered_customer_date'])
df_final = df_final.dropna(subset=['order_id']) # Garante que não há pedidos sem ID
df_final['product_category_name'] = df_final['product_category_name'].fillna('sem_categoria')

# Remoção de registros Duplicados
df_final = df_final.drop_duplicates()

# Padronização de dados
df_final['product_category_name'] = df_final['product_category_name'].str.lower().str.replace('_', ' ')

# Conversão de campos de data e Métricas 
df_final['order_purchase_timestamp'] = pd.to_datetime(df_final['order_purchase_timestamp'])
df_final['ano_mes_compra'] = df_final['order_purchase_timestamp'].dt.to_period('M').astype(str)

# Nova métrica: Tempo de entrega previsto em dias
df_final['order_estimated_delivery_date'] = pd.to_datetime(df_final['order_estimated_delivery_date'])
df_final['prazo_entrega_estimado'] = (df_final['order_estimated_delivery_date'] - df_final['order_purchase_timestamp']).dt.days

# Criando métricas (Ano-Mês)
df_final['order_purchase_timestamp'] = pd.to_datetime(df_final['order_purchase_timestamp'])
df_final['ano_mes_compra'] = df_final['order_purchase_timestamp'].dt.to_period('M').astype(str)

# mostrando clunas 
print(df_final.columns)

# Salvando no Banco de Dados
try:
    conn = sqlite3.connect(db_path)
    df_final.to_sql('vendas_completas', conn, if_exists='replace', index=False)
    conn.close()
    print("Transformação concluída e banco criado com sucesso!")
except Exception as e:
    print(f"Ocorreu um erro: {e}")
