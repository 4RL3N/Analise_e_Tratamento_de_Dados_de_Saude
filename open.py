import os
import webbrowser
import tkinter as tk
from tkinter import messagebox

caminho_repositorio = os.path.dirname(os.path.abspath("index.html"))
caminho_html = "\site\index.html" # Caminho para o arquivo html em si

caminho_completo = os.path.join(caminho_repositorio + caminho_html)

if os.path.exists(caminho_completo):
    webbrowser.open('file://' + caminho_completo)

# Caso não ache o diretório, emita um popup alertando que o caminho não foi encontrado
else:
    tela = tk.Tk()
    tela.withdraw()
    messagebox.showinfo("Alerta!", "Diretório não encontrado")