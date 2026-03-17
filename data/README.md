
# Projeto Integrador – Análise de Dados de E‑commerce (Olist)

## Definição da Base de Dados
A base de dados utilizada neste projeto é a **Brazilian E‑Commerce Public Dataset by Olist**,
disponibilizada publicamente na plataforma Kaggle.

Essa base reúne informações reais de vendas realizadas por meio de uma plataforma de
e‑commerce brasileira entre os anos de **2016 e 2018**. O conjunto de dados foi disponibilizado
pela empresa **Olist**, que atua como intermediadora entre lojistas e marketplaces no Brasil.

O dataset contém aproximadamente **100 mil pedidos**, incluindo informações sobre clientes,
produtos, pagamentos, avaliações, vendedores e localização geográfica.

## Estrutura da Base
Os principais arquivos CSV utilizados são:

- olist_customers_dataset.csv
- olist_orders_dataset.csv
- olist_order_items_dataset.csv
- olist_order_payments_dataset.csv
- olist_order_reviews_dataset.csv
- olist_products_dataset.csv
- olist_sellers_dataset.csv
- olist_geolocation_dataset.csv
- product_category_name_translation.csv

## Objetivo da Análise
O objetivo do projeto é explorar os dados de vendas do e‑commerce para gerar insights como:

- análise de vendas por período
- desempenho de categorias de produtos
- avaliação de clientes
- tempo de entrega
- comportamento de pagamento
- distribuição geográfica de clientes e vendedores

## Organização do Projeto

data/
    Arquivos CSV do dataset

sql/
    Script para criação das tabelas no banco de dados

python/
    Script Python para importar os dados

docs/
    Modelo de banco de dados (ER Diagram)

