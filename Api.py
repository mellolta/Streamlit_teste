

import streamlit as st
import pandas as pd

"""Teste de aplicação"""

uploaded_file = st.file_uploader("Escolha um arquivo Excel")
st.session_state['Arquivo'] = uploaded_file

#- processa apenas se houver um arquivo carregado
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    df

#- exibe as propriedades da sessão
st.session_state


