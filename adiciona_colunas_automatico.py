import pandas as pd

adiciona_colunas = pd.read_excel('', usecols=['arroz', 'feijao', 'bife'])

adiciona_colunas = adiciona_colunas.iloc[:, [0, 2 , 1]]

colunas = ['arroz', 'feijao', 'bife']

adiciona_colunas['RESULTADO'] = adiciona_colunas[colunas].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)

adiciona_colunas.to_excel('', index=False)

print(adiciona_colunas)