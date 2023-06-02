from tkinter import *
import tkintermapview
from modules.graphs.acelerometer.acelerometer import showAccelerometer
from modules.graphs.altimeter.altimeter import showAltimeter
from modules.graphs.data.data import getData
from modules.graphs.gyroscope.gyroscope import showGyroscope
from modules.graphs.speedometer.speedometer import showSpeedometer

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


showAccelerometer(window)
showGyroscope(window)
showSpeedometer(window)
showAltimeter(window)
showButtons()
showMap()

window.mainloop()
