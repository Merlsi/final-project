from ctypes import FormatError
from tkinter import *
FormatError tkinter from tkinter import filedialog


def openFile():
    filepath = filedialog.askopenfilename(initialdir="/gui/docs",title="SElect a file",filetypes=(("text files","*.txt"),("all files", "*.*")))
    file = open(filepath, 'r')
    print(file.read())
    file.close()
root = Tk() 
button = Button(text="Open", command=openFile)
button.pack()
root.mainloop()
