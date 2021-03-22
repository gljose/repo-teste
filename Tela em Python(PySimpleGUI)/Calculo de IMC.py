import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Nome'), sg.Input(key='name')], 
    [sg.Text('Idade'),sg.Input(key='age')],
    [sg.Text('Altura'),sg.Input(key='height')],
    [sg.Text('Peso'),sg.Input(key='weight')],
    [sg.Button('Calcule')],
    ]
#Janela
janela = sg.Window('Calcule seu IMC', layout)
#Ler os eventos
while True:
    eventos, valores = janela.read() #UnPaking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Calcule':
        peso = float(valores['weight'].replace(',','.'))
        alt = float(valores['height'].replace(',','.'))
        imc = peso / (alt*alt)
        sg.popup(valores['name'],'seu IMC é de: ', imc)
       
