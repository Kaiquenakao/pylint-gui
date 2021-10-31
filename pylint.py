import PySimpleGUI as sg


titulo = ('Arial', 15)

def interface():
    """ Layout da interface """
    sg.theme('DarkGrey2')
    
    layout = [
        [sg.Text("PyLint", justification='center', size=(200, 1), font=titulo)],
        [sg.Input(default_text='Insira o arquivo: ', size=(55, None)), sg.FileBrowse('Selecionar', key='-IN-')],
        [sg.Multiline(size=(200, 200), key='info', disabled=True)],
    ]
    return sg.Window("Pylint", layout, finalize=True, size=(500, 500))


janela = interface()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break
    
    """"
        if event == "enviar":
            window['info'].update("teste")
    """
