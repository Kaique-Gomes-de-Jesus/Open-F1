
'''
Identificação
Dev: Kaique Gomes de Jesus
RA: 24271635
Data: 02/06/2025
'''
import streamlit as st
import requests
from buscar_piloto import buscar_piloto_por_numero
from listar_pilotos_conhecidos import listar_pilotos_conhecidos
from listar_todos_pilotos import listar_todos_pilotos
from salvar_pilotos import salvar_piloto

st.title("OpenF1 API - Consulta de Pilotos.")
#Interface streamlit
opcao = st.sidebar.selectbox("Escolha uma opção", [
    "Buscar por número", "Listar pilotos conhecidos", "Listar todos os pilotos", "Salvar piloto em json"
])

if opcao == "Buscar por número":
    numero = st.text_input("Digite o número do piloto: ")
    if st.button("Buscar informações do piloto"):
        if numero:
            buscar_piloto_por_numero(numero)
        else:
            st.warning("Digite um número de piloto para buscar.")


elif opcao == "Listar pilotos conhecidos":
    listar_pilotos_conhecidos()

elif opcao == "Listar todos os pilotos":
    listar_todos_pilotos()

elif opcao == "Salvar piloto em json":
    numero = st.text_input("Digite o número do piloto para salvar: ")
    if st.button("Salvar json"):
        if numero:
            salvar_piloto(numero)
        else:
            st.warning("Digite um número de piloto para salvar.")