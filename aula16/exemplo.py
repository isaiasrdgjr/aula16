from sqlalchemy import create_engine
import pandas as pd
import numpy as np 

# variáveis de conexão

host = 'localhost'
user = 'root'
password = ''
database = 'bd_loja'


engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# obtendo dados
df_estoque = pd.read_sql('tb_produtos', engine)
print(df_estoque.head)

df_estoque['TotalEstoque'] = df_estoque['qtd'] * df_estoque['preco']

print(df_estoque[['produto', 'TotalEstoque']])
print(f'\nTotal Geral de produtos: R$ {df_estoque["TotalEstoque"].sum()}')

array_estoque = np.array(df_estoque['TotalEstoque'])

media = np.mean(array_estoque)
mediana = np.median(array_estoque)

distancia = (abs(media - mediana)/mediana) * 100

print(f'Média: {media:.2f}, \nMediana: {mediana}')
print(f'Distância média e mediana: {distancia:.2f}%')
