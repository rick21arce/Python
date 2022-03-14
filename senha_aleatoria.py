import random

import string

 

letras = string.ascii_letters

digitos = string.digits

caracteres = "#$@&"

geral = letras + digitos + caracteres

senha_aleatoria = ''.join(random.choices(geral, k=15))

 

print(senha_aleatoria)