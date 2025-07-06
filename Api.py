

import streamlit as st
import pandas as pd

"""Teste de aplicação"""

#< ------------------------------------------------------------------------------------------------------------------------------
def seleciona_arquivo():
    """ Abre uma janela de navegação que permite selecionar um único arquivo.\n
        Retorna o path do arquivo.\n
        - Esse procedimento evita que a janela de navegação fique atrás da janela de trabalho do VSCode.\n
    """
    #- carrega o módulo de navegação para a seleção com o mouse
    import tkinter as tk
    from  tkinter import filedialog

    root = tk.Tk()
    root.withdraw()  #- Oculta a janela principal (evita que a janela principal seja exibida por um breve momento)

    #- Mostra o diálogo de abertura de arquivo em primeiro plano
    root.lift()                         #- traz a janela principal para o primeiro plano
    root.attributes('-topmost', True)   #- tornar a janela principal a janela superior
    root.focus_force()

    #- Abre a janela de navegação e salva na variável
    arquivo = filedialog.askopenfilename()

    #- Restaura o comportamento padrão
    root.attributes('-topmost', False)

    root.destroy()

    return arquivo

#< ------------------------------------------------------------------------------------------------------------------------------

click = st.button("Selecione um arquivo (.csv)", 
                    key = 'click_arquivo',
                    help="clique para selecionar",
                    )

click
st.session_state

if click:
    arquivo = seleciona_arquivo()
    st.session_state['Arquivo'] = arquivo
    df = pd.read_excel(arquivo)
    df

st.session_state


