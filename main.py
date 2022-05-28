import tkinter as tk
from tkinter import *
from tkinter import filedialog
from gtts import gTTS
import os
from PIL import ImageTk,Image
from tkinter import messagebox


#design of tkinter
window = Tk()

#for background
C = Canvas(window, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Users\\1\\Downloads\\backgroun1.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()






#for icon
 


#window.show()



def openFile():
    global file
    filepath = filedialog.askopenfilename(initialdir='C:\\Users\\1\\Desktop\\project,title="Open file",filetypes',title="Open file",filetype=(("text files","*.txt"),("pdf files","*.pdf")))
    if(filepath):
        file = open(filepath, 'r')
        
    
            


def texttospeech():
    audio = file.read().replace("\n"," ")
    language = "en"
    output = gTTS(text=audio,lang=language,slow=False)
    output.save("output.mp3")
    os.system("start output.mp3")
    

my_font1 = ('times',14,'bold')
button = Button(text = "Open file",font=my_font1,command=openFile)
button.pack(pady=10)


button_to_audio = Button(text="listen",font=my_font1,command=texttospeech)
button_to_audio.pack(pady=19)
#side=LEFT,anchor=N


window.mainloop()

