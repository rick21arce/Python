import sqlite3

master_password = "mopa123"
senha = input("Insira sua senha master: ")

 

if senha != master_password:

 

    print("Senha inválida, Encerrando...")

 

    exit()

conn = sqlite3.connect("passwords.db")

cursor = conn.cursor()

cursor.execute('''

 

CREATE TABLE IF NOT EXISTS users(

 

    service TEXT NOT NULL,

 

    username TEXT NOT NULL,

 

    password TEXT NOT NULL

 

);

 

''')

def menu():
    
 

    print("*********** GERENCIADOR DE SENHAS ******************")

 

    print("* i: inserir uma nova senha *")

 

    print("* l: listar serviços salvos *")

 

    print("* r: recuperar uma senha *")

 

    print("* s: sair *")

 

    print("********** GERENCIADOR DE SENHAS *******************")

def get_password(service):
    
 

    cursor.execute(f'''

 

    SELECT username, password FROM users

 

    WHERE service = '{service}'

 

    ''')

 

    if cursor.rowcount == 0:

 

        print("Serviço não cadastrado (use '1' para verificar os serviços).")

 

    else:

 

        for user in cursor.fetchall():

 

            print(user)

def insert_password(service, username, password):
    
 

    cursor.execute(f'''

 

        INSERT INTO users (service, username, password)

 

        VALUES ('{service}', '{username}', '{password}')

 

    ''')

 

    conn.commit()


def show_services():
    
 

    cursor.execute('''

 

    SELECT service FROM users;

 

    ''')

 

    for service in cursor.fetchall():

 

        print(service)

while True:
    
 

    menu()

 

    op = input("O que deseja fazer?")

 

    if op not in ['i', 'l', 'r', 's']:

 

        print("Opção inválida")

 

        continue

 

    if op == 's':

 

        break

 

    if op == 'i':

 

        service = input("Qual o nome do serviço? ")

 

        username = input("Qual é o nome do usuário? ")

 

        password = input("Qual é a senha? ")

 

        insert_password(service, username, password)

 

    if op == 'l':

 

        show_services()

 

    if op == 'r':

 

        service = input("Qual é o serviço que gostaria de saber a senha? ")

 

        get_password(service)

conn.close()

