import PySimpleGUI as sg


def interface():
    """ Layout da interface """
    sg.theme('DarkGrey2')
    
    layout = [
        [sg.Multiline(size=(30, 5), key='info', disabled=True)],
    ]
    return sg.Window("Pylint",layout, finalize=True)


janela = interface()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break

