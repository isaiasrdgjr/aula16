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
df_vendas = pd.read_sql('tb_vendas', engine)
print(df_vendas.head(6))

arrecadacao_vendas = df_vendas['qtd'] * df_vendas['preco']

media_vendas = np.mean(df_vendas['qtd'])
mediana_vendas = np.median(df_vendas['qtd'])

distancia = (abs(media_vendas - mediana_vendas)/mediana_vendas) * 100


print(f'A média é de: {media_vendas:.2f} vendas.')

if distancia > 30.0:
    print(f'\nA média não é confiável, a variação é de: {distancia:.2f} %')
elif distancia > 10.0:
    print(f'\nMédia moderadamente confiável, variação é de: {distancia:.2f} %')
else:
    print(f'\nA média é confiável, a variação é de: {distancia:.2f} %')
