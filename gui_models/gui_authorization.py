import PySimpleGUI as sg

# All the stuff inside your window.
layout = [[sg.Text("What's your login?")],
          [sg.InputText()],
          [sg.Text("What's your password?")],
          [sg.InputText()],
          [sg.Button('Go'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Hello Example', layout)

# Event Loop to process "events" and get the "values" of the inputs
# while True:
#     event, values = window.read()
#
#     # if user closes window or clicks cancel
#     if event == sg.WIN_CLOSED or event == 'Cancel':
#         break
#
#     print('Hello', values[0], '!')
#     print('Hello', values[1], '!')

window.close()
