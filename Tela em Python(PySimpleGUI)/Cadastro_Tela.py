from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size =(19,1))], #Largura,Altura
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*', size =(20,1))],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')]
    ]
#Janela
janela = sg.Window('Tela de Login', layout, size =(250,120))
#Ler os eventos
while True:
    eventos, valores = janela.read() #UnPaking
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'gabriel' and valores['senha'] == '123456':
            print('Bem-Vindo ao Mundo do Gabriel!!')
        else:
            print('Você não esta Cadastrado!')
