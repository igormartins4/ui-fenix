import tkinter as tk
import tkintermapview
import requests
import json

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Application():
    def __init__(self, window):
        self.window = window
        self.window.title("User Interface Missão Guará - Fênix UFMG")
        self.window.iconbitmap("logo.ico")

        largura = 1280
        altura = 720

        # define o tamanho da janela com as dimensões da tela
        window.geometry("%dx%d+0+0" % (largura, altura))

        # Define o grid
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)

        # Cria os frames
        self.frame1 = tk.Frame(self.window, bg='red')
        self.frame2 = tk.Frame(self.window, bg='green')
        self.frame3 = tk.Frame(self.window, bg='blue')
        self.frame4 = tk.Frame(self.window, bg='yellow')
        self.frame5 = tk.Frame(self.window, bg='orange')
        self.frame6 = tk.Frame(self.window, bg='purple')

        # Adiciona os widgets aos frames
        tk.Label(self.frame1, text="Acelerômetro",
                 font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame2, text="Giroscópio",
                 font=('Arial', 16)).pack(pady=20)
        # tk.Label(self.frame3, text="Altímetro", font=('Arial', 10)).pack(pady=5)
        tk.Label(self.frame4, text="Velocímetro",
                 font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame5, text="Botões", font=('Arial', 16)).pack(pady=20)
        # tk.Label(self.frame6, text="Mapa GPS", font=('Arial', 16)).pack(pady=20)

        # Chama a função showAltitude para exibir o gráfico no Frame 3
        self.showAltitude()

        # Define a posição dos frames no grid
        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame2.grid(row=0, column=1, sticky='nsew')
        self.frame3.grid(row=1, column=0, sticky='nsew')
        self.frame4.grid(row=1, column=1, sticky='nsew')
        self.frame5.grid(row=2, column=0, sticky='nsew', columnspan=2)
        self.frame6.grid(column=2, row=0, sticky='nsew',
                         columnspan=1, rowspan=3)

        # Define a proporção das colunas e linhas
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=2)

        self.window.rowconfigure(0, weight=1)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)

        self.latitude = None
        self.longitude = None
        self.intervalo = 2  # atualiza a cada 2 segundos

        self.atualizar_posicao()  # chama o método para atualizar a posição

    # Função que mostra onde está a ISS, apenas para efeitos visuais
    def atualizar_posicao(self):
        response = requests.get('http://api.open-notify.org/iss-now.json')
        data = json.loads(response.content)
        self.latitude = float(data['iss_position']['latitude'])
        self.longitude = float(data['iss_position']['longitude'])

        # remove o mapa antigo
        for widget in self.frame6.winfo_children():
            widget.destroy()

        # cria um novo mapa com as novas coordenadas
        self.showMap(self.latitude, self.longitude)

        # chama novamente a função atualizar_posicao() após 5 segundos
        self.window.after(self.intervalo * 1000, self.atualizar_posicao)

    # Função que exibe o mapa na tela
    def showMap(self, latitude, longitude):
        map_widget = tkintermapview.TkinterMapView(
            self.frame6, width=400, height=1280)
        map_widget.set_position(latitude, longitude)
        map_widget.pack(fill='both', expand=True)
        self.frame6.columnconfigure(0, weight=1)
        self.frame6.rowconfigure(0, weight=1)

        map_widget.set_zoom(10)

    def showAltitude(self):
        altura = [10, 200, 300, 400]
        tempo = [1, 20, 90, 160]

        # Cria um objeto Figure do Matplotlib
        fig = Figure(figsize=(1, 1), dpi=100)
        fig.suptitle('Altímetro')

        # Adiciona um subplot ao objeto Figure
        ax = fig.add_subplot(1, 1, 1)

        # Plota um gráfico de linha simples
        ax.plot(altura, tempo)

        ax.set_xlabel('Tempo em segundos')
        ax.set_ylabel('Altura em metros')

        # Cria um widget FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.frame3)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)
        
        # Gráfico para o Giroscópio
        altura_giroscopio = [100, 200, 300, 400, 500]
        tempo_giroscopio = [1, 20, 40, 80, 160]

        # Cria um objeto Figure do Matplotlib
        fig = Figure(figsize=(1, 1), dpi=100)
        fig.suptitle('Giroscopio')

        # Adiciona um subplot ao objeto Figure
        ax = fig.add_subplot(1, 1, 1)

        # Plota um gráfico de linha simples
        ax.plot(altura_giroscopio, tempo_giroscopio)

        ax.set_xlabel('Tempo em segundos')
        ax.set_ylabel('Altura em metros')

        # Cria um widget FigureCanvasTkAgg
        canvas = FigureCanvasTkAgg(fig, master=self.frame2)
        canvas.draw()
        canvas.get_tk_widget().pack(side='top', fill='both', expand=True)


# Cria a janela
window = tk.Tk()

# Cria a aplicação
app = Application(window)

# Inicia o loop da aplicação
window.mainloop()
