import requests
import base64
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

txts = ['teste.txt']

def api_to_txt(arquivo):
    req = requests.post('linkapi', json={"comando":"{]".format(arquivo)}, verify=False)

    api_teste = req.json()

    api = api_banco['result']

    txt = base64.b64decode(api)

    caminho = 'c:/users/ricardo/download/{}'.format(arquivo)
    with open(caminho, 'wb') as c:
        c.write(txt)

for t in txts:
    api_to_txt(t)        