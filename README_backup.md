# Projeto Integrador - Pipeline de ETL para E-Commerce (Olist)

Este módulo é responsável por executar o processo de **ETL (Extract, Transform, Load)** dos dados públicos de e-commerce da Olist, servindo como a fundação de dados estruturada para o dashboard interativo da aplicação.

## Arquitetura do Processo

### 1. Extração (Extract)
* **Arquivo:** `extracao_dados.py`
* **Tecnologia:** Python e biblioteca `kagglehub`.
* **Descrição:** Realiza a conexão com a API do Kaggle para efetuar o download programático dos datasets originais em formato `.csv`, salvando-os de forma íntegra na pasta `dados_brutos/`.

### 2. Transformação (Transform)
* **Arquivo:** `transformacao_dados.py`
* **Tecnologia:** Python e biblioteca `Pandas`.
* **Descrição:** Realiza o cruzamento (*merge*) das tabelas relacionais de pedidos, clientes e pagamentos pelas chaves primárias (`order_id` e `customer_id`). Nesta etapa, os campos de carimbo de data/hora são convertidos para o tipo `datetime` e os registros nulos são tratados, consolidando mais de 103 mil linhas de histórico.

### 3. Carga (Load)
- **Arquivo:** `transformacao_dados.py`
- **Tecnologia:** Python e biblioteca `sqlite3`.
- **Descrição:** Persiste os dados manipulados na memória RAM para um banco de dados estruturado relacional local (`olist_estruturado.db`), otimizando o tempo de carregamento e garantindo alta performance para o consumo das métricas no dashboard (Streamlit).

## Como Executar:

## Passo 1 - Crie e ative o ambiente virtual:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1

## Passo 2 - Execute o script de extração para coletar os dados: 
    ```bash
    python extracao_dados.py    


## Passo 3 - Execute o script de transformação para gerar a base estruturada:
    ```bash
    python transformacao_dados.py
