from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import datetime

import requests

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
def calcular_tempo_execucao():
    segundos = datetime.datetime.now()
    return segundos

def showAltimeter(windowView):
    speedometerLabelFrame = LabelFrame(windowView, text="Altímetro")
    speedometerLabelFrame.grid(
        row=0, column=1, padx=10, pady=10, sticky='nsew')

    # Criação do canvas para o gráfico
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=speedometerLabelFrame)
    canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    # Listas para armazenar os dados de altitude e timestamp
    altitudes = []
    timestamps = []

    calcular_tempo_execucao()

    # Função para atualizar o gráfico
    def update_graph():

        nonlocal altitudes, timestamps  # Usa variáveis não locais

        # Obtém os dados de altitude e timestamp
        data = getData()
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
        ax.set_title('Gráfico de Altitude em Tempo Real')

        # Redesenha o gráfico
        canvas.draw()

        # Chama a função para atualizar o gráfico após intervalo de tempo
        windowView.after(2000, update_graph)  # Chama novamente após 2 segundos

    # Chama a função para atualizar o gráfico após a definição
    update_graph()
