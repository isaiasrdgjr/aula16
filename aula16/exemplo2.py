from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import numpy as np 
import os

# variáveis de conexão
load_dotenv()

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

query_vendedor = "SELECT * FROM tb_vendas WHERE nome_vendedor = 'Carlos Silva'"
# obtendo dados
df_vendas = pd.read_sql('tb_vendas', engine)
print(df_vendas.head(6))

arrecadacao_vendas = df_vendas['qtd'] * df_vendas['preco']

media_vendas = np.mean(df_vendas['qtd'])
mediana_vendas = np.median(df_vendas['qtd'])

distancia = (abs(media_vendas - mediana_vendas)/mediana_vendas) * 100

df_vendas['valor_venda'] = df_vendas['qtd'] * df_vendas['preco']


df_vendas['comissao'] = (df_vendas['valor_venda'] * 0.09).round(2)

print(df_vendas[['nome_vendedor', 'valor_venda', 'comissao']].head(10))

array_valor_vendas = np.array(df_vendas['valor_venda'])

# Calcula média e mediana
media = np.mean(array_valor_vendas)
mediana = np.median(array_valor_vendas)

# MEDIDAS DE TENDÊNCIA CENTRAL
print('\nMEDIDAS DE TENDÊNCIA CENTRAL')
print(f"Média das comissões: R$ {media:.2f}")
print(f"Mediana das comissões: R$ {mediana:.2f}")
