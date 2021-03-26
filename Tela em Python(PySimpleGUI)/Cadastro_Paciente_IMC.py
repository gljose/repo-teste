import mysql.connector as ms
from mysql.connector import Error
import PySimpleGUI as sg

#Layouts
def janela_abertura():
    layout = [[sg.Text('Cadastrar Novo Paciente:'), sg.Button('Cadastrar')],
             [sg.Text('Encontre um Paciente:'), sg.Button('Procurar')]    
    ]
    return sg.Window('Cálculo de IMC', layout, finalize = True)
def janela_cadastro():
    layout = [[sg.Text('Nome:'), sg.Input(key='name')],
          [sg.Text('E-mail:'), sg.Input(key='mail')],
          [sg.Text('Idade:'), sg.Input(key='age')],
          [sg.Text('Sexo:'), sg.Input(key='sex')],
          [sg.Text('Peso:'), sg.Input(key='weight')],
          [sg.Text('Altura:'), sg.Input(key='height')],
          [sg.Button('Salvar'), sg.Button('Voltar')]
    ]
    return sg.Window('Cadastro novo Paciente', layout, finalize = True)
def janela_busca():
    layout = [[sg.Text('Nome:'), sg.Input(key='name_2')],
              [sg.Button('Buscar'), sg.Button('Voltar')]
              ]
    return sg.Window('Busca de Paciente', layout, finalize = True)
def inserir_paciente(dados):
    trs = True
    declaracao = '''INSERT INTO PESSOA
    (nome,email,idade,sexo,peso,altura,imc)
    VALUES('''
    sql = declaracao + dados
    print(sql)
    try:
        con = ms.connect(host= 'localhost', database = 'cadastro', user ='root', password = '')
        cursor = con.cursor()
        cursor.execute(sql)
        con.commit()
        print(cursor.rowcount, 'Registro inserido na tabela!')    
        cursor.close()
    except Error as erro:
        trs = False
        print('Falha ao inserir dados no MySQL: {}'.format(erro))   
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print('A Conexão ao MySQL foi Encerrada com sucesso!')            
    return trs
def busca_paciente(nome_busca):
    trs = True
    sql = '''SELECT IMC FROM PESSOA WHERE UPPER(NOME) LIKE \'%'''+ nome_busca +'%\' LIMIT 1'''
    print(sql)
    try:
        con = ms.connect(host= 'localhost', database = 'cadastro', user ='root', password = '')
        cursor = con.cursor()
        cursor.execute(sql)
        linha = cursor.fetchone()
    except Error as erro:
        trs = False
        print('Falha ao buscar dados no MySQL: {}'.format(erro))   
    finally:
        if (con.is_connected()):
            con.close()
            cursor.close()
            print('A Conexão ao MySQL foi Encerrada com sucesso!')            
    return trs,linha
#janela
janela1, janela2, janela3 = janela_abertura(), None, None
#Eventos(loop para leitura dos eventos)
while True:
    window, eventos,values = sg.read_all_windows()
    
    if window == janela1 and eventos == 'Cadastrar':
        janela2 = janela_cadastro()
        janela1.hide()
    if window == janela1 and eventos == 'Procurar':
        janela3 = janela_busca()
        janela1.hide()
    if window == janela3 and eventos == 'Buscar':
        nome_busca = values['name_2']
        trs, imc = busca_paciente(nome_busca)
        if trs:
            sg.popup(values['name_2']+' seu IMC é de: '+ str(imc))
    if window == janela2 and eventos == 'Salvar':
        imc = (float(values['weight'])/(float(values['height'].replace(',','.'))* float(values['height'].replace(',','.'))))        
        dados = '\''+ values['name'] + '\',\'' + values['mail'] + '\',' + values['age'] + ',\'' + values['sex'] + '\',' + values['weight'].replace(',','.') + ',' + values['height'].replace(',','.') + ',\''+ str(imc)+'\')'
        trs = inserir_paciente(dados)
        if trs == True:
            sg.popup('Paciente Incluído com Sucesso!')        
        else:
            sg.popup('Erro ao Inserir paciente, tente novamente!')    
    if window == janela2 and eventos == 'Voltar':
        janela1 = janela_abertura()
        janela2.hide()
    if window == janela3 and eventos == 'Voltar':
        janela1 = janela_abertura()
        janela3.hide()
        
    
