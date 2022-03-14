import os

import shutil

 

caminho_original = ''

caminho_novo = '' #coloque a pasta nova criada

 

try:

    os.mkdir(caminho_novo)

except FileExistsError as e:

    print(f'Pasta {caminho_novo} já existe')    

 

for root, dirs, files, in os.walk(caminho_original):

    for file in files:

        pasta_caminho_antiga = os.path.join(root, file)

        pasta_caminho_novo = (caminho_novo, file)

 

        shutil.move(pasta_caminho_antiga, pasta_caminho_novo)

        print(f'Arquivo {file} movido com sucesso')