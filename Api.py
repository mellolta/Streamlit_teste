

import streamlit as st
import pandas as pd

"""Teste de aplicação"""

uploaded_file = st.file_uploader("Escolha um arquivo")
st.session_state['Arquivo'] = uploaded_file
df = pd.read_excel(uploaded_file)
df

st.session_state


