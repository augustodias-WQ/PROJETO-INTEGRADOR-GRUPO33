# PROJETO-INTEGRADOR-GRUPO33
#  Projeto Integrador — Low Code em Ciência de Dados

##  Tema do Projeto

Análise de desempenho de vendas em um e-commerce utilizando técnicas de **Ciência de Dados e ferramentas Low Code**, com o objetivo de gerar **insights estratégicos por meio de visualizações em um dashboard interativo**.

O projeto utiliza a base **Brazilian E-Commerce Public Dataset by Olist**, composta por dados reais de vendas realizadas em marketplaces brasileiros entre **2016 e 2018**.



#  1️ Integrantes do Grupo

* **Juliana Alves Cabral**
* **Luis Augusto de Sousa Dias**
* **Guilherme Silva Alves do Nascimento**
* **Pedro Henrique Ferraz Ferreira**
* **Matheus de Oliveira Temistocles**



#  2️ Definição da Base de Dados

## Base de Dados Selecionada

A base de dados utilizada neste projeto é a **Brazilian E-Commerce Public Dataset by Olist**, disponibilizada publicamente na plataforma Kaggle.

Essa base reúne informações reais de vendas realizadas por meio de uma plataforma de **e-commerce brasileira**, abrangendo transações ocorridas entre **2016 e 2018**.

## Origem dos Dados

Os dados foram disponibilizados pela empresa **Olist**, que atua como intermediadora entre lojistas e marketplaces no Brasil.

O dataset foi publicado com finalidade educacional e de análise, sendo amplamente utilizado em projetos de **Ciência de Dados, Engenharia de Dados e Business Intelligence**.

## Contexto da Base

O conjunto de dados contém informações detalhadas sobre o processo de compra em um e-commerce, incluindo:

* identificação dos pedidos
* informações sobre clientes
* dados dos produtos vendidos
* categorias de produtos
* localização geográfica dos clientes
* datas de compra, envio e entrega
* valores de pagamento
* avaliações dos clientes

Essas informações permitem analisar **comportamento de consumo, desempenho de vendas e eficiência logística**.



#  3️ Objetivo da Análise

O objetivo deste projeto é aplicar ferramentas **Low Code voltadas à ciência de dados** para analisar o desempenho de vendas de um e-commerce e gerar **insights estratégicos por meio de visualizações em dashboards**.

A análise buscará identificar:

* produtos e categorias mais vendidos
* regiões com maior volume de vendas
* evolução do faturamento ao longo do tempo
* ticket médio das compras
* quantidade total de pedidos realizados
* padrões de comportamento dos consumidores

O resultado final será um **dashboard interativo** que permitirá visualizar as principais métricas do negócio de forma clara e acessível.



#  4️ Planejamento das Tarefas

As responsabilidades do projeto foram distribuídas entre os integrantes da seguinte forma:

### Luis Augusto de Sousa Dias

Responsável pela **criação e organização do repositório no GitHub**, incluindo a estrutura inicial do projeto e controle de versões.

### Juliana Alves Cabral

Responsável pela **definição da base de dados e contextualização do projeto**, incluindo a descrição da origem e objetivo da análise.

### Guilherme Silva Alves do Nascimento

Responsável pelo **planejamento do processo de ETL**, definindo como os dados serão extraídos, transformados e carregados para análise.

### Matheus de Oliveira Temistocles

Responsável pelo **planejamento do dashboard**, definindo as métricas, indicadores e visualizações a serem apresentadas.

### Pedro Henrique Ferraz Ferreira

Responsável pela **organização do README e planejamento geral das tarefas**, garantindo a documentação adequada do projeto.



#  5️ Cronograma de Desenvolvimento

 Etapa     Atividade                           
 
 Semana 1  Definição da base de dados          
 Semana 2  Planejamento do processo de ETL     
 Semana 3  Tratamento e integração dos dados   
 Semana 4  Desenvolvimento do dashboard        
 Semana 5  Análise dos resultados              
 Semana 6  Ajustes finais e entrega do projeto 



#  6️ Processo de ETL (Extract, Transform, Load)

Para preparação dos dados será utilizado um pipeline de **ETL**, composto por três etapas principais.

## Extração

Os dados serão extraídos do repositório público da Olist disponível na plataforma Kaggle.

## Transformação

Durante essa etapa serão realizadas:

* integração entre tabelas relacionadas
* tratamento de valores ausentes
* remoção de registros inconsistentes
* padronização de dados
* conversão de campos de data
* preparação de métricas analíticas

Essas transformações serão realizadas utilizando a linguagem **Python** e a biblioteca **Pandas**.

## Carga

Após o tratamento, os dados serão armazenados em um banco de dados **SQLite** ou em arquivos **Parquet**, permitindo consultas analíticas mais eficientes.



# 7️ Ideia Inicial do Dashboard

O dashboard será estruturado como uma ferramenta de **Business Intelligence**, permitindo análise em diferentes dimensões do negócio.

## Performance Comercial

* faturamento total
* ticket médio
* formas de pagamento

## Logística e Entregas

* tempo médio de entrega
* comparação entre entrega real e estimada
* mapa de vendas por região

## Experiência do Cliente

* avaliação média dos clientes
* análise de comentários
* relação entre atraso na entrega e satisfação

## Análise de Produtos

* categorias mais vendidas
* produtos com maior faturamento
* impacto de fotos e descrição nas vendas



# 8️ Métricas do Dashboard

Principais indicadores de desempenho (KPIs):

* faturamento total
* ticket médio
* número total de pedidos
* tempo médio de entrega
* avaliação média dos clientes
* vendas por região
* vendas por categoria



#  Estrutura do Repositório GitHub

O projeto seguirá uma organização profissional de repositório voltada para **projetos de ciência de dados e análise de dados**.


projeto-integrador-lowcode/

README.md

data/
├ raw/
│ dados brutos do Kaggle
│ olist.db
│ dados tratados após ETL

etl/
├ extract.py
├ transform.py
└ load.py

app/
├ dashboard
├ 
└ 


```

---

#  Tecnologias Utilizadas

* Python
* Pandas
* Kaggle Dataset
* Streamlit
* GitHub

---

#  Resultados Esperados

Com a análise dos dados e o desenvolvimento do dashboard, espera-se:

* identificar padrões de consumo
* entender o desempenho das vendas
* avaliar a eficiência logística
* analisar a satisfação dos clientes
* gerar insights estratégicos para tomada de decisão
