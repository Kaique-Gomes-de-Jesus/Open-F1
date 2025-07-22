import streamlit as st
import requests


'''
Identificação
Dev: Kaique Gomes de Jesus
RA: 24271635
Data: 02/06/2025
'''

#Função 1 - Buscar informações do piloto
def buscar_piloto_por_numero(numero_piloto):
    url = f"https://api.openf1.org/v1/drivers?driver_number={numero_piloto}&session_key=9158"
    try:
        #Requisição da api
        response = requests.get(url)
        #Erros da api
        response.raise_for_status()
        #Transformar em json
        dados = response.json()
        if dados:
            piloto = dados[0]
            st.subheader("Informações do piloto.")
            st.write(f"""
            Nome: {piloto.get('full_name', 'Desconhecido')}\n
            Equipe: {piloto.get('team_name', 'Não disponível')}\n
            Nacionalidade: {piloto.get('country_code', 'Não informada')}\n
            Número do carro: {piloto.get('driver_number', 'N/A')}\n
            """)
            st.image(piloto.get('headshot_url', 'Sem imagem disponível'), width=150) 
        else:
            st.warning("Piloto não encontrado para essa sessão.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")