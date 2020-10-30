import os
import shutil
from screeninfo import get_monitors
import PySimpleGUI as sg

WIDTH = 500
HEIGHT = 500
start_cwd=os.getcwd()


#1 layout
layout= [   [sg.Text('Choose folders you want to synchronise', justification='center', size=(WIDTH,1))], 
            [sg.Text('From: ', size=(10,1)), sg.Input(key='browseInput'), sg.FolderBrowse(key="browseFrom")],
            [sg.Text('Sync with: ', size=(10,1)), sg.Input(key='browseOutput'), sg.FolderBrowse(key="browseTo")], 
            [sg.Button('Check files', key="checkButton",size=(20,1))],
            [sg.Text('-'*WIDTH)],
            [sg.Text('Current directory', size=(25,1), justification='center'), sg.Text(' '*10), sg.Text('Files that will be updated',size=(25,1), justification='center')], 
            [sg.Listbox(values=['..']+os.listdir(path=start_cwd), size=(int(WIDTH/50*3),10), key='fromListbox', bind_return_key=True), sg.VerticalSeparator(pad=None), sg.Listbox(values=[4,5,6], size=(int(WIDTH/50*3), 10), key='toListbox')],
            [sg.Button('Begin syncing', key='beginSync',)]        
        ]

#2 window
window = sg.Window('Folder synchronization', layout, grab_anywhere=False, location=(get_monitors()[0].width/4-WIDTH/2, 
        get_monitors()[0].height/2-HEIGHT/2), size=(WIDTH,HEIGHT), element_justification='c')

last_selected = ''
current_cwd = start_cwd.split('/')
for element in current_cwd:
    if len(element) == 0:
        current_cwd.remove(element)

   
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'checkButton':
        if values['browseInput'] != '':
            window['fromListbox'].update( values=['..']+os.listdir(path=values['browseInput']) )        
    elif len(values['fromListbox']) != 0:
        current_selected = values['fromListbox'][0]
        if current_selected == '..':
            last_selected = values['fromListbox'][0]
            window['fromListbox'].update( values=['..']+os.listdir('/'+'/'.join([str(current_cwd[i]) for i in range(len(current_cwd)-1)]) ))
        elif current_selected != last_selected:
            last_selected = values['fromListbox'][0]
            window['fromListbox'].update( values=['..']+os.listdir(path='/'+'/'.join([str(current_cwd[i]) for i in range(len(current_cwd)-1)])+'/'+last_selected ) )
    
    #print(start_cwd)
    #print('Default_cwd: ')
    #print('last_selected: '+last_selected)
    #print('add_to_cwd: ')
window.close()
