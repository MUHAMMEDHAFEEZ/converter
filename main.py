import PySimpleGUI as sg
layout = [
    
    [sg.Button("convert",key='-CHANGE-'),sg.Input("",key='INPUT'),sg.Spin(['km to m','m to km','min to sec','sec to min'],key='-SPIN-',readonly=True)],
    [sg.Text("",key='-OUT-')]
]

window = sg.Window('converter ', layout,icon="download.ico")
while True:
    event, values = window.read()
    NUM = float(values['INPUT'])
    if event == sg.WIN_CLOSED:
        break
    if event == "-CHANGE-":
        if(values['-SPIN-']=='m to km'):
             window['-OUT-'].update(NUM/1000)
           
        elif(values['-SPIN-']=='km to m'):
             window['-OUT-'].update(NUM*1000)
             
        elif(values['-SPIN-']=='min to sec'):
             window['-OUT-'].update(NUM*60)    
             
        elif(values['-SPIN-']=='sec to min'):
             window['-OUT-'].update(NUM/60)   
             
    
window.close()
    
