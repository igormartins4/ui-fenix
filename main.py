import tkinter as tk


class Application:
    def __init__(self, window):
        self.window = window
        self.window.title("User Interface Missão Guará - Fênix UFMG")

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
        self.frame6 = tk.Frame(self.window, bg='purple',
                               width=self.window.winfo_width() / 2)

        # Adiciona os widgets aos frames
        tk.Label(self.frame1, text="Frame 1", font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame2, text="Frame 2", font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame3, text="Frame 3", font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame4, text="Frame 4", font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame5, text="Frame 5", font=('Arial', 16)).pack(pady=20)
        tk.Label(self.frame6, text="Frame 6", font=('Arial', 16)).pack(pady=20)

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


# Cria a janela
window = tk.Tk()

# Cria a aplicação
app = Application(window)

# Inicia o loop da aplicação
window.mainloop()
