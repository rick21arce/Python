from os import chdir, listdir
from os.path import isfile
import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import time

def tratamento_arquivos_za():
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

def tratamento_arquivos_zd():
    pass

def criar_base_excel():
    pass

if (__name__ == "__main__"):

    inicio_geral = datetime.now()

    inicio = datetime.now()
    tratamento_arquivos_za()
    fim = datetime.now()
    print(f'Base x importada, com o tempo de execução de: {fim - inicio}')

    inicio = datetime.now()
    tratamento_arquivos_zd()
    fim = datetime.now()
    print(f'Base x importada, com o tempo de execução de: {fim - inicio}')

    inicio = datetime.now()
    criar_base_excel()
    fim = datetime.now()
    print(f'Base x importada, com o tempo de execução de: {fim - inicio}')

