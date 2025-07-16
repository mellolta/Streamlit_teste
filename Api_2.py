
import streamlit as st
import pandas as pd

# O ID da sua planilha, extraído do link fornecido
spreadsheet_id = "1Uam3-NE7m99zAKGiqatXP-rVwpTa8HHX"

# O ID da aba que você quer acessar
desvio = "2136860350"
cota = "1707724905"
siadh = "229062704"
medicoes = "521897502"

sheet_gid = desvio # Altere este valor se sua aba não for a primeira

# Constrói a URL para exportar a planilha como CSV
csv_export_url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={sheet_gid}"

st.title("Visualizador de Planilha do Google Drive")

try:
    # Lê os dados diretamente da URL CSV para um DataFrame do pandas
    df = pd.read_csv(csv_export_url)

    st.success("Planilha carregada com sucesso!")
    st.write("Aqui estão os primeiros registros da sua planilha:")
    st.dataframe(df.head()) # Exibe as primeiras linhas do DataFrame

    # Você pode adicionar mais elementos Streamlit aqui, como gráficos, filtros, etc.
    st.markdown("---")
    st.write(f"Sua planilha tem {df.shape[0]} linhas e {df.shape[1]} colunas.")

except Exception as e:
    st.error(f"Não foi possível carregar a planilha. Verifique se o link de compartilhamento está correto e se a planilha está configurada como 'Qualquer pessoa com o link pode ver'.")
    st.exception(e) # Mostra detalhes do erro para depuração


