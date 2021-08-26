from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print('Iniciando Robô..')
arq = open("C:/Users/ricar/Downloads/resultado.txt","w")

dominios = []

#lendo do excel
workbook = xlrd.open_workbook('C:/Users/ricar/Downloads/dominios.xlsx')
sheet = workbook.sheet_by_index(0)

for linha in range(0,10):
    dominios.append(sheet.cell_value(linha,0))

#inicia o browser
driver = webdriver.Edge(executable_path='C:/Users/Public/robos_python_driver/msedgedriver.exe')

driver.get('https://registro.br/')
time.sleep(1)

driver.maximize_window()#maximiza tela do navegador
time.sleep(1)


for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    pesquisa.clear() #Limpando a barra de pesquisa
    pesquisa.send_keys(dominio)
    pesquisa.send_keys(Keys.RETURN)
    time.sleep(2)

    resultados = driver.find_elements_by_tag_name("strong")
    texto = "Domínio %s %s" % (dominio, resultados[4].text)
    arq.write(texto)#escreve resultado em arquivo txt

arq.close()
time.sleep(5)
driver.close()