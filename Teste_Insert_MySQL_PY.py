import mysql.connector as ms
from mysql.connector import Error

#inserir registros em um banco MySQL
print('Rotina para cadastro de IMC de Pacientes')
print('Entre com os dados conforme solicitado')

nomePes = input('Nome: ')
idadePes = input('Idade: ')
sexoPes = input('Sexo: ')
pesoPes = input('Peso: ')
alturaPes = input('Altura: ')
nacioPes = input('Nacionalidade: ')

dados = '\''+ nomePes + '\',' + idadePes + ',\'' + sexoPes + '\',' + pesoPes + ',' + alturaPes + ',\'' + nacioPes + '\')'

declaracao = '''INSERT INTO PESSOA
(nome,idade,sexo,peso,altura,nacionalidade)
VALUES('''
sql = declaracao + dados

print(sql)

try:
    con = ms.connect(host= 'localhost', database = 'cadastro', user ='root', password = '')

    inserir_cliente = sql
    cursor = con.cursor()
    cursor.execute(inserir_cliente)
    con.commit()
    print(cursor.rowcount, 'Registro inserido na tabela!')
    cursor.close()
except Error as erro:
    print('Falha ao inserir dados no MySQL: {}'.format(erro))
finally:
    if (con.is_connected()):
        con.close()
        cursor.close()
        print('A Conexão ao MySQL foi Encerrada com sucesso!')
