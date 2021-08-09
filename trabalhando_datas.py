from datetime import date, timedelta

hoje = date.today()

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')
ontem = date.fromordinal(hoje.toordinal()-1) #dia anterior
ontem_br = ontem.strftime('%d/%m/%Y')

friday = date.today() - timedelta(days=3)

sexta = friday.strftime('%d/%m/%Y')


final_de_semana = date.today().weekday()

if final_de_semana > 5:
    print(sexta)
else:
    print(ontem_br)    

