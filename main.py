import struct
from tkinter import *

import tkintermapview
import requests
import json

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import numpy as np
import serial
import datetime

window = Tk()
window.title("User Interface Missão Guará - Fênix UFMG")
window.iconbitmap("logo.ico")

# Configurar as colunas e linhas da janela para expansão
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)


def showAccelerometer():
    accelerometerLabelFrame = LabelFrame(window, text="Acelerômetro")
    accelerometerLabelFrame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=accelerometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Configuração da comunicação serial
    ser = serial.Serial('/dev/cu.usbserial-14430',
                        57600)  # Substitua 'COM6' pela porta correta e '9600' pela velocidade de comunicação correta

    # Listas para armazenar os dados do acelerômetro e timestamp
    accelerations = []
    timestamps = []

    # Função para atualizar o gráfico
    def update_graph():

        # Obtém os dados do acelerômetro e timestamp da comunicação serial
        data = ser.read(48)
        unpack_format = '12f'  # 12 float values
        values = struct.unpack(unpack_format, data)
        acceleration = values[0]
        timestamp = datetime.datetime.now()

        # Adiciona os dados às listas
        accelerations.append(acceleration)
        timestamps.append(timestamp)

        if len(accelerations) == 12:
            accelerations.pop(0)

        if len(timestamps) == 12:
            timestamps.pop(0)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, accelerations)
        ax.set_xlabel('Tempo')
        ax.set_ylabel('Aceleração')
        ax.set_title('Acelerômetro em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 1 segundo

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showAltimeter():
    altimeterLabelFrame = LabelFrame(window, text="Altímetro")
    altimeterLabelFrame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=altimeterLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Configuração da comunicação serial
    ser = serial.Serial('/dev/cu.usbserial-A50285BI', 57600)
    # Listas para armazenar os dados do altímetro e timestamp
    altitudes = []
    timestamps = []

    # Função para atualizar o gráfico
    def update_graph():
        # Obtém os dados do altímetro e timestamp da comunicação serial
        data = ser.read(48)
        unpack_format = '12f'  # 12 float values
        values = struct.unpack(unpack_format, data)
        altitude = values[5]
        timestamp = datetime.datetime.now()

        # Adiciona os dados às listas
        altitudes.append(altitude)
        timestamps.append(timestamp)

        if len(altitudes) == 12:
            altitudes.pop(0)

        if len(timestamps) == 12:
            timestamps.pop(0)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, altitudes)
        ax.set_xlabel('Tempo')
        ax.set_ylabel('Altitude')
        ax.set_title('Altímetro em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 1 segundo

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showGyroscope():
    gyroscopeLabelFrame = LabelFrame(window, text="Giroscópio")
    gyroscopeLabelFrame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=gyroscopeLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Configuração da comunicação serial
    ser = serial.Serial('/dev/cu.usbserial-A50285BI', 57600)
    # Listas para armazenar os dados de giroscópio e timestamp
    gyro_values = []
    timestamps = []

    # Função para atualizar o gráfico
    def update_graph():
        # Obtém os dados de giroscópio e timestamp da comunicação serial
        data = ser.read(48)
        unpack_format = '12f'  # 12 float values
        values = struct.unpack(unpack_format, data)
        gyro_value = values[0]
        timestamp = datetime.datetime.now()

        # Adiciona os dados às listas
        gyro_values.append(gyro_value)
        timestamps.append(timestamp)

        if len(gyro_values) == 12:
            gyro_values.pop(0)

        if len(timestamps) == 12:
            timestamps.pop(0)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, gyro_values)
        ax.set_xlabel('Tempo')
        ax.set_ylabel('Giroscópio')
        ax.set_title('Giroscópio em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 1 segundo

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showSpeedometer():
    speedometerLabelFrame = LabelFrame(window, text="Velocímetro")
    speedometerLabelFrame.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=speedometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Configuração da comunicação serial
    ser = serial.Serial('/dev/cu.usbserial-A50285BI', 57600)
    # Listas para armazenar os dados de velocidade e timestamp
    speeds = []
    timestamps = []

    # Função para atualizar o gráfico
    def update_graph():
        # Obtém os dados de velocidade e timestamp da comunicação serial
        data = ser.read(48)
        unpack_format = '12f'  # 12 float values
        values = struct.unpack(unpack_format, data)
        speed = values[6]
        timestamp = datetime.datetime.now()

        # Adiciona os dados às listas
        speeds.append(speed)
        timestamps.append(timestamp)


        if len(speeds) == 12:
            speeds.pop(0)

        if len(timestamps) == 12:
            timestamps.pop(0)


        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, speeds)
        ax.set_xlabel('Tempo')
        ax.set_ylabel('Velocidade')
        ax.set_title('Velocidade em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 1 segundo

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showMap():
    mapLabelFrame = LabelFrame(window, text="Mapa")
    mapLabelFrame.grid(row=0, column=2, rowspan=4, padx=10, pady=10, sticky='nsew')

    latitude = None
    longitude = None
    intervalo = 2  # atualiza a cada 2 segundos

    # Configuração da comunicação serial
    ser = serial.Serial('/dev/cu.usbserial-A50285BI', 57600)

    # Função para atualizar a posição no mapa
    def update_map():
        nonlocal latitude, longitude

        # Obtém os dados de latitude e longitude do GPS da comunicação serial
        data = ser.read(48)
        unpack_format = '12f'  # 12 float values
        values = struct.unpack(unpack_format, data)
        element = data.split(" ")
        latitude = float(values[4])
        longitude = float(values[5])

        # Remove o mapa antigo
        for widget in mapLabelFrame.winfo_children():
            widget.destroy()

        # Cria um novo mapa com as novas coordenadas
        openMap(latitude, longitude)

        # Chama novamente a função para atualizar o mapa após n segundos
        window.after(intervalo * 10000, update_map)

    # Função para exibir o mapa na tela
    def openMap(latitude, longitude):
        map_widget = tkintermapview.TkinterMapView(mapLabelFrame, width=400, height=400)
        map_widget.set_position(latitude, longitude)
        map_widget.pack(fill='both', expand=True)

    # Chama a função para atualizar o mapa após a definição
    update_map()


def showButtons():
    buttonsLabelFrame = LabelFrame(window, text="Botões")
    buttonsLabelFrame.grid(row=2, column=0, padx=10,
                           pady=10, sticky='nsew', columnspan=2)
    buttons = Label(buttonsLabelFrame, text="Conteúdo")
    buttons.pack(fill='both', expand='yes')


Button(window, text="Mostrar Mapa", command=showMap).grid(row=2, column=2, padx=10, pady=10)
Button(window, text="Mostrar Altímetro", command=showAltimeter).grid(row=2, column=0, padx=10, pady=10)
Button(window, text="Mostrar Giroscópio", command=showGyroscope).grid(row=2, column=1, padx=10, pady=10)
Button(window, text="Mostrar Velocímetro", command=showSpeedometer).grid(row=3, column=0, padx=10, pady=10)
Button(window, text="Mostrar Acelerômetro", command=showAccelerometer).grid(row=3, column=1, padx=10, pady=10)

window.mainloop()

showGyroscope()
showSpeedometer()
showAltimeter()

showAccelerometer()
