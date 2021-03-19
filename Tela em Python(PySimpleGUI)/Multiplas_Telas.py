from PySimpleGUI import PySimpleGUI as sg

#Layouts
def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nome')],
        [sg.Input()],
        [sg.Button('Continuar')]
    ]
    return sg.Window('Login', layout, finalize = True)
    
def janela_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Fazer Pedido')],
        [sg.Checkbox('Margherita',key ='pz1'),sg.Checkbox('Queijo',key ='pz2')],
        [sg.Checkbox('Calabresa',key ='pz3'),sg.Checkbox('Banana',key ='pz4')],
        [sg.Button('Sair'),sg.Button('Pedido')]
    ]
    return sg.Window('Montar Pedido', layout, finalize = True)
   
#Criar janelas iniciais
janela1, janela2 = janela_login(), None # Chama apenas a primeira janela
#Criar um loop de leitura de eventos
while True:
    window,eventos,values = sg.read_all_windows()
    #Quando a janela for fechada
    
    if window == janela1:
        evento = janela1.read()
        if evento == sg.WIN_CLOSED:
            break
    if window == janela2:
        evento = janela2.read()
        if evento == sg.WIN_CLOSED:
            break  
    #Quando queremos ir para prox. Janela
    if window == janela1 and eventos == 'Continuar':
         janela2 = janela_pedido()
         janela1.hide()
    if window == janela2 and eventos == 'Sair':
         janela1 = janela_login()
         janela2.hide()
    if window == janela2 and eventos == 'Pedido':
        if values['pz1']==True and values['pz2'] and values['pz3'] and values['pz4']:
            sg.popup('Foram selecionadas: Margherita, Queijo, Calabresa e Banana' )
        elif values['pz1']==True:
            sg.popup('Foram selecionadas: Margherita' )
        elif values['pz2']==True:
            sg.popup('Foram selecionadas: Queijo' )
        elif values['pz3']==True:
            sg.popup('Foram selecionadas: Calabresa' )
        elif values['pz4']==True:
            sg.popup('Foram selecionadas: Banana' )     
   
    #Quando queremos voltar para a janela anterior
    
#Lógica de que deve acontecer ao cliecar nos botões

