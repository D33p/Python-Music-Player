import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.mp3 import MP3
from tkinter import *

from PIL import ImageTk, Image
import tkinter as tk
import random

root = Tk()
root.title("MUSIC PLAYER")
root.minsize(800,600)
listofsong =[]                                             # LIST OF SONG INDEX
list = []
text = Text(root)
path = ("giphy.ico")
root.iconbitmap(path)
index = 0

def nextsong(event):                                       # FOR NEXT SONG
    global index
    timing.set(0)
    audio=MP3(listofsong[index])
    index =(index+1)%len(listofsong)
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()

def previoussong(event):                                  # FOR PREVIOUS SONG
    global index
    timing.set(0)
    audio=MP3(listofsong[index])
    index = (index-1)%len(listofsong)
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()

offset=0

def seeksong(event):
    global offset
    offset=timing.get()*(audio.info.length)/100
    print (pygame.mixer.music.get_pos())
    print (offset)
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play(0,offset)
    
    
def stopsong(event):                                      # FOR STOP SONG
    pygame.mixer.music.stop()

def play(event):                                          # FOR PLAY THE SONG
    global index,audio
    clock=pygame.time.Clock()
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.play()
#    print (audio.info.length)
#    while(pygame.mixer.music.get_busy()):
#       y=pygame.mixer.music.get_pos()/(audiolength*100)
#       print(y)
#       timing.set(y)
#       clock.tick(0.1)


def pause(event):                                         # FOR PAUSE THE SONG
    global index
    pygame.mixer.music.load(listofsong[index])
    pygame.mixer.music.pause()

def shuffle(event):                                      # FOR SHHUFFLE THE SONG
    s = random.randrange(0,len(listofsong),1)
    pygame.mixer.music.load(listofsong[s])
    pygame.mixer.music.queue(listofsong[s])
    pygame.mixer.music.play()
    pygame.display.update()
    clock.tick(15)

def pluse(event):                                        # FOR VOLUMNE
    pygame.mixer.music.set_volume(volumne.get())

def tune_changed(event):                                  # FOR HELP TO CHOOSE IN LIST BOX WISHING MUSIC
    idx = event.widget.curselection()[0]
    pygame.mixer.music.load(listofsong[idx])
    pygame.mixer.music.play()

def directorychooser():                                    # DIRECTORY FUNCTION

    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):                  # FIND THE MUSIC FILE DIRECTIORY
        if files.endswith(".mp3"):
            listofsong.append(files)
    print(files)                                        # PRINT THE MUSIC FILE ON THE OUTPUT
    pygame.mixer.init()
    pygame.mixer.music.load(listofsong[0])
    #pygame.mixer.music.play()

directorychooser()                                         # IT IS USE FOR THE CALL DIRECTORY FUNCTION

label =Label(root,text='MUSIC PLAYER',font=('Sans-serif',30,'bold'),fg='black',width=350)                 # WRITE THE MUSIC PLAYER ON TOP OF BOX
label.pack()

scrollbar = Scrollbar(root, width=25)                       # MAKE THE SCROLLBAR OF THE BOX
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set,width=30,font=('Arial',10))# MAKE THE BOX FOR THE MUSIC LIST
listbox.pack(side=RIGHT, fill=BOTH,padx=20,pady=10,ipadx=10,ipady=10)
scrollbar.config(command=listbox.yview)                       # GIVE THE COMMAND FOR SCROLLBAR

listofsong.reverse()
for items in listofsong:
    listbox.insert(0,items)
listofsong.reverse()

listbox.bind("<Double-Button-1>", tune_changed)               # LISTBOX IS BIND THE DOUBLE CLICK ON MUSIC

#listbox.bind("<<ListboxSelect>>", tune_changed)              # IT IS USE FOR JUST CLICK AND PLAY
shufflebutton = Button(root,text='Shuffle all mp3',width=100,bg='white')     # SHUFFLE FOR MUSIC
shufflebutton.pack()

global audio
audio=MP3(listofsong[index])
audiolength=float(audio.info.length)                                                         # MAKE THE VOLUMNE SLIDER

timing = Scale(root,orient=HORIZONTAL,length=300,width=8,command=seeksong,
               sliderlength=8,from_=0,to=100,tickinterval=10,resolution=(audiolength/100))
timing.pack(side=BOTTOM,fill=X)
timing.set(0)

##Button(root,command=seeksong).pack()
buttonsFrame = Frame(root)

Play = Button(buttonsFrame,width=6,text='Play',font=('Arial',12),bd=3)              # USE FOR PLAY THE SOUND
Play.grid(row = 0, column=0)

pausebutton = Button(buttonsFrame,width=6,text='Pause',font=('Arial',12),bd=3)      # USE FORPAUSE THE SONG
pausebutton.grid(row = 0, column=1)

stop = Button(buttonsFrame,width=6,text='Stop',font=('Arial',12),bd=3)              # STOP BUTTON FOR SONG
stop.grid(row = 0, column=2)

previous = Button(buttonsFrame,text='Previous',font=('Arial',12),bd=3 )             # PREVIOUS BUTTON FOR SONG
previous.grid(row = 0, column=3)

Next = Button(buttonsFrame,width=6,text='Next',font=('Arial',12),bd=3)              # NEXT BUTTON FOR SONG
Next.grid(row = 0, column=4)


volumne = Scale(buttonsFrame,orient=HORIZONTAL,length=100,width=8,sliderlength=8,from_=0,to=100,tickinterval=100,
                command=pluse, resolution = 1)
volumne.grid(row=0,column=5)

buttonsFrame.pack(side=BOTTOM)                # PACK OR CREATE ALL BUTTON
Next.bind("<Button-1>",nextsong)              # BIND THE BUTTON FOR NEXT SONG
previous.bind("<Button-1>",previoussong)      # BIND THE BUTTON FOR PREVIOUS SONG
stop.bind("<Button-1>",stopsong)              # BIND THE BUTTON FOR STOP SONG
pausebutton.bind("<Button-1>",pause)          # BIND THE BUTTON FOR PAUSE THE SONG
Play.bind("<Button-1>",play)                  # BIND THE BUTTON FOR PLAY THE SONG
shufflebutton.bind("<Button-1>",shuffle)      # BIND THE BUTTON FOR SHUFFLE THE SONG


root.geometry("800x600")
path = ("giphy.gif")          # FILL THE IMAGE ON THE PANNEL
img = ImageTk.PhotoImage(Image.open(path))                         # PATH OF THE IMAGE

panel = tk.Label(root, image = img)
panel.pack(side = "top", fill = "both", expand = "yes")

root.configure(background='black')                                  # FILL THE BACKGROUND COLOUR

root.mainloop()
