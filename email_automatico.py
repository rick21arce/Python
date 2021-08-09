from datetime import date
import win32com.client as win32
import pandas as pd
from pandas import DataFrame

data_atual = date.today()
data_em_texto = 'teste_{}{}'.format(data_atual.strftime('%d/%m/%y'), '.txt')

df = open("{}".format(data_em_texto))
linha = df.readlines()
teste = linha [-1]

outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = ''
mail.Cc = ''
mail.Subject = 'teste de envio de email automatico'
mail.body = 'se vc recebeu este e-mail o código funcionou'

mail.Send()