import PySimpleGUI as sg

layout = [
    [sg.Text('N1: '), sg.InputText(key = 'n1')],
    [sg.Text('N2: '), sg.InputText(key = 'n2')],
    [sg.Button('Somar')],
    [sg.Button('Subtrair')],
    [sg.Button('Multiplicar')],
    [sg.Button('Dividir')]
]

window = sg.Window('Calculadora',layout)
while True:
    eventos, valores = window.read()
    if eventos == sg.WIN_CLOSED:
        break
    
    elif eventos == 'Somar':
         result = int(valores['n1']) + int(valores['n2'])
         sg.popup(f'resultado = {result}')

    elif eventos == 'Subtrair':
         result = int(valores['n1']) - int(valores['n2'])
         sg.popup(f'resultado = {result}')

    elif eventos == 'Multiplicar':
         result = int(valores['n1']) * int(valores['n2'])
         sg.popup(f'resultado = {result}')

    elif eventos == 'Dividir':
          result = int(valores['n1']) / int(valores['n2'])
          sg.popup(f'resultado = {result}')
window.close()
