from tkinter.constants import DISABLED
import PySimpleGUI as sg
from os import path, chdir
from pylint import epylint as lint

titulo = ('Arial', 15)


def interface():
    """ Layout da interface """
    sg.theme('DarkGrey2')

    layout = [
        [sg.Text("PyLint", justification='center', size=(200, 1), font=titulo)],
        [sg.Input(default_text='Insira o arquivo: ', size=(55, None,), key='arquivo'),
         sg.FileBrowse('Selecionar', key='-IN-')],
        [sg.Button("Executar", key="carregar", pad=(200, None))],
        [sg.Multiline(size=(200, 200), key='info', disabled=True)],
    ]
    return sg.Window("Pylint", layout, finalize=True, size=(500, 500))


janela = interface()

while True:
    window, event, values = sg.read_all_windows()

    if event == sg.WINDOW_CLOSED:
        break

    if event == 'carregar' and path.isfile(values['arquivo']):
        arquivo = values['arquivo'].split('/').pop()
        dir = "/".join(values['-IN-'].split('/')[0:-1]) + "/"
        chdir(dir)
        (pylint_stdout, pylint_stderr) = lint.py_run(
            f'{arquivo} --disable C0114', return_std=True
        )
        window['info'].update(pylint_stdout.getvalue())


    if event == 'carregar' and (not path.isfile(values['arquivo'])):
        sg.Popup('Não é um arquivo')