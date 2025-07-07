

import streamlit as st
import pandas as pd

"""Teste de aplicação"""

#< ------------------------------------------------------------------------------------------------------------------------------
def seleciona_arquivo_streamlit():
    # st.title("Meu Visualizador de Excel")

    # Usa st.file_uploader para permitir que o usuário faça upload de um arquivo
    # uploaded_file = st.file_uploader("Escolha um arquivo Excel (.xls ou .xlsx)", type=["xls", "xlsx"])
    uploaded_file = st.file_uploader("Escolha um arquivo")

    # if uploaded_file is not None:
    #     # Se um arquivo foi carregado, o pandas pode lê-lo diretamente
    #     try:
    #         df = pd.read_excel(uploaded_file)
    #         st.write("Conteúdo do arquivo Excel:")
    #         st.dataframe(df) # Exibe o DataFrame como uma tabela no Streamlit
    #     except Exception as e:
    #         st.error(f"Erro ao ler o arquivo Excel: {e}")
    #         st.write("Certifique-se de que o arquivo é um arquivo Excel válido.")
    # else:
    #     st.write("Por favor, carregue um arquivo Excel para visualizar o conteúdo.")
    
    return uploaded_file
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


