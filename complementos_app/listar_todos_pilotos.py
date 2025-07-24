import streamlit as st
import requests
'''
Identificação
Dev: Kaique Gomes de Jesus
RA: 24271635
Data: 02/06/2025
'''

#Função 3 - Listar todos os pilotos
def listar_todos_pilotos():
    url = f"https://api.openf1.org/v1/drivers?session_key=9158"
    try:
        #Requisição da api
        response = requests.get(url)
        #Erros da api
        response.raise_for_status()
        #Transformar em json
        dados = response.json()
        st.subheader("Todos os pilotos.")
        if dados:
            for piloto in dados:
                nome = {piloto.get('full_name', 'Desconhecido')}
                equipe = {piloto.get('team_name', 'Não disponível')}
                nacionalidade = {piloto.get('country_code', 'Não informada')}
                numero = {piloto.get('driver_number', 'N/A')}
                st.write(f"""
                        ***{nome}*** | 
                        Número: {numero} | 
                        Equipe: {equipe} | 
                        Nacionalidade: {nacionalidade}
                        """)
            
        else:
            st.warning("Piloto não encontrado para essa sessão.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")
