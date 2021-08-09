from os import chdir, listdir

from os.path import isfile

caminho = ""

chdir(caminho)

lista = []

for arquivo in listdir():
    if isfile(arquivo):
        with open(f"{arquivo}", "r") as content:
            linha = content.readlines()
            ultima_linha = linha[len(linha) - 1]
            lista.append(ultima_linha)

with open("c:/users/ricardo/download/juntaultimaslinhas/novo.txt", "w") as f:
    for linha in lista:
        f.write(str(linha) + "\n")            