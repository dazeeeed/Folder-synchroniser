import os
import shutil
from screeninfo import get_monitors
import PySimpleGUI as sg

WIDTH = 500
HEIGHT = 500

#1 layout
layout= [   [sg.Text('Choose folders you want to synchronise', justification='center', size=(WIDTH,1))], 
            [sg.Text('From: ', size=(10,1)), sg.Input(), sg.FolderBrowse(key="browseFrom")],
            [sg.Text('Sync with: ', size=(10,1)), sg.Input(), sg.FolderBrowse(key="browseTo")], 
            [sg.Button('Check files'), sg.Button('Begin syncing')] ]

#2 window
window = sg.Window('Folder synchronization', layout, grab_anywhere=True, location=(get_monitors()[0].width/4-WIDTH/2, 
        get_monitors()[0].height/2-HEIGHT/2), size=(WIDTH,HEIGHT))


#3 event loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Button':
        print('You pressed the button')
window.close()
