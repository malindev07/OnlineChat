import PySimpleGUI as sg

# All the stuff inside your window.
layout = [[sg.Text('Chat with user')],
          [sg.Text()],
          [sg.InputText()],
          [sg.Button('Close chat')]]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    
    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    print('Hello', values[0], '!')
    # print('Hello', values[1], '!')

window.close()
