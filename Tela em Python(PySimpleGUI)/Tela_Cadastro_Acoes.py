from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome do Ativo:'), sg.Input(key='ativo', size = (10,1))],
    [sg.Text('Quantidade:'), sg.Input(key= 'qte', size = (10,1))],
    [sg.Text('Preço Médio'), sg.Input(key= 'pm', size = (10,1))],
    [sg.Button('Salvar')],
    [sg.Button('Mostrar')]
    ]
#Janela
janela = sg.Window('Cadastro de Ativos', layout, size = (300,180))
#Le os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Salvar':
        sg.popup('Dados Salvos!')
    if eventos == 'Mostrar':
        sg.popup('Ativo: ', valores['ativo'],'QTDE: ', valores['qte'],'PM: ',valores['pm'])
    
