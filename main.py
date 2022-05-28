import tkinter as tk
from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os
from PIL import ImageTk, Image
from tkinter import messagebox


window = Tk()
window.title('Text_to_speech')

C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file="nature1.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()

window.iconbitmap(r'alatoo16.ico')
Label(window, text="Ala Too International University",
      font='aharoni 30 bold',
      fg='black', width='45').pack(side='bottom')


def openFile():
    global file
    filepath = filedialog.askopenfilename(
        initialdir = 'C: \\Users\\1\\Desktop\\project',
        title="Open file",
        filetype=(
            ("text files", "*.txt"),))
    if(filepath):
        file = open(filepath, 'r')
# function to convert from text to audio


def texttospeech():
    audio = file.read().replace("\n", " ")
    language = "en"
    output = gTTS(text=audio, lang=language, slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
my_font1 = ('times', 14, 'bold')
button = Button(text="Open file", font=my_font1, command=openFile)
button.pack(side=LEFT, anchor=NW)

button_to_audio = Button(text="listen", font=my_font1, command=texttospeech)
button_to_audio.pack(side=LEFT, anchor=NW)

window.mainloop()
