
import pandas as pd
import sqlite3
import os

DATA_PATH = "../data"

conn = sqlite3.connect("olist.db")

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "payments": "olist_order_payments_dataset.csv",
    "reviews": "olist_order_reviews_dataset.csv",
    "products": "olist_products_dataset.csv",
    "sellers": "olist_sellers_dataset.csv"
}

for table, file in files.items():
    path = os.path.join(DATA_PATH, file)
    df = pd.read_csv(path)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Tabela {table} importada com sucesso")

conn.close()
