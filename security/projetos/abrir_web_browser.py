"""
BIBLIOTECAs
- webbrowser: Fornece uma interface de alto nível para permitir a exibição de
documentos web aos usuários
- tkinter: Fornece interface padrão do Python para o Kit de ferramentas gráficas TK
"""

import webbrowser
from tkinter import *

from setuptools import Command

root = Tk( )
root.title('Abrir Browser')
root.geometry('380x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text="Abrir o Google", command=google).pack(pady=20)
root.mainloop()