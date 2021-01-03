# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 09:10:38 2020

@author: 20304834
"""
import os
import pygame
from mutagen.id3 import ID3
from tkinter.filedialog import askdirectory
from tkinter import *
root=Tk()
root.title("MUSIC PLAYER")
root.geometry('800x400+10+10')
root.config(bg='black')

listofsongs=[]
realnames=[]
global index
index=0 
def stopsong(event):
    pygame.mixer.music.stop()
    
def directorychooser():
    directory=askdirectory()
    os.chdir(directory)
    for file in os.listdir(directory):
        if file.endswith('.mp3'):
            realdir=os.path.realpath(file)
            audio=ID3(realdir)
            #print(audio)
            realnames.append(audio.get('TIT2')) #realnames.append(audio['TIT2'].text[0])
            listofsongs.append(file)
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()            
    #print(audio)
def nextsong(event):
    global index
    global v
    try:
        index+=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=0
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()        
def prevsong(event):
    global index
    global v
    try:
        index-=1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()
    except IndexError:
        index=len(listofsongs)-1
        pygame.mixer.music.load(listofsongs[index])
        pygame.mixer.music.play()        
     
directorychooser()
label=Label(root, text='MUSIC PLAYER', width=20,font=('arial', 28,'bold'),background='cadet blue', fg='gold' )
label.place(x=10,y=10)

listbox=Listbox(root, width=65, font=('arial',10,'bold'),background='black', fg='gold')
listbox.place(x=10,y=60)
for items in realnames:
    listbox.insert(0,items)
nextbutton=Button(root, width=16,text='Next Song',fg='blue',font=('Monotype Corsiva', 16, 'bold'))
nextbutton.place(x=20,y=290)
previousbutton=Button(root, width=16,text='Previous Song',fg='blue',font=('Monotype Corsiva', 16, 'bold'))
previousbutton.place(x=240,y=290)
stopbutton=Button(root, width=26,text='Stop Music',fg='blue',font=('Monotype Corsiva', 16, 'bold'))
stopbutton.place(x=40,y=350)
nextbutton.bind('<Button-1>',nextsong)
previousbutton.bind('<Button-1>',prevsong)
stopbutton.bind('<Button-1>',stopsong)
# =============================================================================
# 
# =============================================================================






root.mainloop()