import os
import webbrowser

caminho_repositorio = os.path.dirname(os.path.abspath("index.html"))
caminho_html = "\site\index.html"

caminho_completo = os.path.join(caminho_repositorio + caminho_html)

if os.path.exists(caminho_completo):
    webbrowser.open('file://' + caminho_completo)