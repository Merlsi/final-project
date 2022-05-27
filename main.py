from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os

window = Tk()
window.geometry('400x400')

def openFile():
    global file
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\1\\Desktop\\project,title="Open file",filetypes',title="Open file",filetype=(("text files",".txt"),("pdf files",".pdf")))
    file = open(filepath, 'r')

def texttospeech():
    audio = file.read().replace("\n"," ")
    language = "en"
    output = gTTS(text=audio,lang=language,slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
    





button_to_audio = Button(text="click to listen the text",command=texttospeech)
button_to_audio.place(relx=0.5, rely=0.5,anchor=CENTER, width=160, height=40)



button = Button(text = "Open",command=openFile)
button.pack()
window.mainloop()
