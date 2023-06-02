from tkinter import *

def showSpeedometer(windowView):
    speedometerLabelFrame = LabelFrame(windowView, text="Velocímetro")
    speedometerLabelFrame.grid(
        row=1, column=1, padx=10, pady=10, sticky='nsew')
    speedometer = Label(speedometerLabelFrame, text="Conteúdo")
    speedometer.pack(fill='both', expand='yes')
