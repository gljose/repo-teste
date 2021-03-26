import mysql.connector as ms
from mysql.connector import Error

conn = ms.connect(host ='localhost', database = 'cadastro',user ='root',password ='')

if conn.is_connected():
    server_inf = conn.get_server_info()
    print('Conectado ao servidor MySQL versão ', server_inf)
    cursor = conn.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados ', linha)

if conn.is_connected():
    cursor.close()
    conn.close()
    print('A Conexão ao MySQL foi Encerrada com sucesso!')
