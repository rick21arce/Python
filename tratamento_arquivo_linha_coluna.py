import pandas as pd

arquivo = open(r'')

colunas = ['TESTE', 'ARROZ', 'FEIJAO']

dados = []

for line in arquivo:
    column = line

    TESTE = column [:]
    ARROZ = column [:]
    FEIJAO = column [:]

dados.append([TESTE, ARROZ, FEIJAO])

df = pd.DataFrame(dados, columns=colunas)

arquivo.close()

df.to_excel('c:/users/ricardo/downloads/teste.xlsx')