from tkinter import *

def showGyroscope(windowView):
    gyroscopeLabelFrame = LabelFrame(windowView, text="Giroscópio")
    gyroscopeLabelFrame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    gyroscope = Label(gyroscopeLabelFrame, text="Conteúdo")
    gyroscope.pack(fill='both', expand='yes')
