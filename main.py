from tkinter import *

import tkintermapview
import requests
import json

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

import datetime


def getData():

    # URL da API
    url = "https://api.wheretheiss.at/v1/satellites/25544"

    try:
        # Faz a solicitação GET para a API
        response = requests.get(url)

        # Verifica se a resposta foi bem-sucedida (código de status 200)
        if response.status_code == 200:
            # Retorna os dados JSON da resposta
            return response.json()
        else:
            print("Erro na solicitação da API:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Ocorreu um erro ao obter dados:", e)


data = getData()

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
    accelerometerLabelFrame.grid(
        row=0, column=0, padx=10, pady=10, sticky='nsew')
    # accelerometer = Label(accelerometerLabelFrame, text="Conteúdo")
    # accelerometer.pack(fill='both', expand='yes')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=accelerometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Listas para armazenar os dados de altitude e timestamp
    altitudes = []
    timestamps = []

    def calcular_tempo_execucao():
        segundos = datetime.datetime.now()
        return segundos

    # Função para atualizar o gráfico
    def update_graph():

        nonlocal altitudes, timestamps  # Usa variáveis não locais

        # Obtém os dados de altitude e timestamp
        # data = getData()
        altitude = float(data['altitude']) * 1000
        timestamp = calcular_tempo_execucao()

        # Adiciona os dados às listas
        altitudes.append(altitude)
        timestamps.append(timestamp)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, altitudes)
        ax.set_xlabel('Tempo (em segundos)')
        ax.set_ylabel('Aceleração (em m/s²)')
        # ax.set_title('Aceleração em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 2 segundos

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showAltimeter():
    speedometerLabelFrame = LabelFrame(window, text="Altímetro")
    speedometerLabelFrame.grid(
        row=0, column=1, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=speedometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Listas para armazenar os dados de altitude e timestamp
    altitudes = []
    timestamps = []

    def calcular_tempo_execucao():
        segundos = datetime.datetime.now()
        return segundos

    # Função para atualizar o gráfico
    def update_graph():

        nonlocal altitudes, timestamps  # Usa variáveis não locais

        # Obtém os dados de altitude e timestamp
        # data = getData()
        altitude = float(data['altitude']) * 1000
        timestamp = calcular_tempo_execucao()

        # Adiciona os dados às listas
        altitudes.append(altitude)
        timestamps.append(timestamp)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, altitudes)
        ax.set_xlabel('Tempo (em segundos)')
        ax.set_ylabel('Altitude (em metros)')
        # ax.set_title('Altitude em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 2 segundos

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showGyroscope():
    gyroscopeLabelFrame = LabelFrame(window, text="Giroscópio")
    gyroscopeLabelFrame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
    # gyroscope = Label(gyroscopeLabelFrame, text="Conteúdo")
    # gyroscope.pack(fill='both', expand='yes')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=gyroscopeLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Listas para armazenar os dados de altitude e timestamp
    altitudes = []
    timestamps = []

    def calcular_tempo_execucao():
        segundos = datetime.datetime.now()
        return segundos

    # Função para atualizar o gráfico
    def update_graph():

        nonlocal altitudes, timestamps  # Usa variáveis não locais

        # Obtém os dados de altitude e timestamp
        # data = getData()
        altitude = float(data['altitude']) * 1000
        timestamp = calcular_tempo_execucao()

        # Adiciona os dados às listas
        altitudes.append(altitude)
        timestamps.append(timestamp)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, altitudes)
        ax.set_xlabel('Tempo (em segundos)')
        ax.set_ylabel('Altitude (em metros)')
        # ax.set_title('Giroscópio em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 2 segundos

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showSpeedometer():
    speedometerLabelFrame = LabelFrame(window, text="Velocímetro")
    speedometerLabelFrame.grid(
        row=1, column=1, padx=10, pady=10, sticky='nsew')
    # speedometer = Label(speedometerLabelFrame, text="Conteúdo")
    # speedometer.pack(fill='both', expand='yes')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=speedometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Listas para armazenar os dados de altitude e timestamp
    altitudes = []
    timestamps = []

    def calcular_tempo_execucao():
        segundos = datetime.datetime.now()
        return segundos

    # Função para atualizar o gráfico
    def update_graph():

        nonlocal altitudes, timestamps  # Usa variáveis não locais

        # Obtém os dados de altitude e timestamp
        # data = getData()
        altitude = float(data['altitude']) * 1000
        timestamp = calcular_tempo_execucao()

        # Adiciona os dados às listas
        altitudes.append(altitude)
        timestamps.append(timestamp)

        # Atualiza os dados no gráfico
        ax.clear()
        ax.plot(timestamps, altitudes)
        ax.set_xlabel('Tempo (em segundos)')
        ax.set_ylabel('Velocidade (em m/s)')
        # ax.set_title('Velocidade em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        window.after(1000, update_graph)  # Chama novamente após 2 segundos

    # Chama a função para atualizar o gráfico após a definição
    update_graph()


def showButtons():
    buttonsLabelFrame = LabelFrame(window, text="Botões")
    buttonsLabelFrame.grid(row=2, column=0, padx=10,
                           pady=10, sticky='nsew', columnspan=2)
    buttons = Label(buttonsLabelFrame, text="Conteúdo")
    buttons.pack(fill='both', expand='yes')


def showMap():
    mapLabelFrame = LabelFrame(window, text="Mapa")
    mapLabelFrame.grid(row=0, column=2, rowspan=4,
                       padx=10, pady=10, sticky='nsew')

    latitude = None
    longitude = None
    intervalo = 2  # atualiza a cada 2 segundos

    # Função que mostra onde está a ISS, apenas para efeitos visuais
    def atualizar_posicao():

        # Obtém os dados de latitude e longitude
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])

        # remove o mapa antigo
        for widget in mapLabelFrame.winfo_children():
            widget.destroy()

        # cria um novo mapa com as novas coordenadas
        openMap(latitude, longitude)

        # chama novamente a função atualizar_posicao() após n segundos
        window.after(intervalo * 1000, atualizar_posicao)

    # Função que exibe o mapa na tela
    def openMap(latitude, longitude):
        map_widget = tkintermapview.TkinterMapView(
            mapLabelFrame, width=400, height=1280)
        map_widget.set_position(latitude, longitude)
        map_widget.pack(fill='both', expand=True)
        mapLabelFrame.columnconfigure(0, weight=1)
        mapLabelFrame.rowconfigure(0, weight=1)

        map_widget.set_zoom(10)

    # Chama a função atualizar_posicao() após a definição
    atualizar_posicao()


showAccelerometer()
showGyroscope()
showSpeedometer()
showAltimeter()
showButtons()
showMap()

window.mainloop()
