import PySimpleGUI as sg

from lec0511.caesar_encoding import caesar_encode
from lec0511.caesar_encoding import caesar_decode


def encode(text):
    return "".join(caesar_encode(text))

def decode(text):
    return "".join(caesar_decode(text))

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('입력텍스트'),  sg.InputText(key="-INPUTTEXT-")],
            [sg.Text('출력텍스트'), sg.InputText(key="-RESULT-")],
            [sg.Button('암호화'), sg.Button('복호화')],
            [sg.Combo(["딸기", "사과"])]
            ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "암호화":
        window["-RESULT-"].update(encode(values["-INPUTTEXT-"]))
    if event == "복호화":
        window["-RESULT-"].update(decode(values["-INPUTTEXT-"]))

    print('You entered ', values["-INPUTTEXT-"])


window.close()