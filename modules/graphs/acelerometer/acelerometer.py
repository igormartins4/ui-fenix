from tkinter import *

def showAccelerometer(windowView):
    accelerometerLabelFrame = LabelFrame(windowView, text="Acelerômetro")
    accelerometerLabelFrame.grid(
        row=0, column=0, padx=10, pady=10, sticky='nsew')
    accelerometer = Label(accelerometerLabelFrame, text="Conteúdo")
    accelerometer.pack(fill='both', expand='yes')
