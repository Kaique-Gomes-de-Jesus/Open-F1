import streamlit as st
import requests
import json

#Função 4 - Salvar piloto
def salvar_piloto(numero_piloto):
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
            nome_arquivo = f"piloto{numero_piloto}.json"
            with open(f".\pilotos\{nome_arquivo}", "w", encoding="utf8") as arquivo:
                json.dump(piloto, arquivo, indent=4, ensure_ascii=False)
            st.success(f"Dados do piloto salvo.")
        else:
            st.warning("Piloto não encontrado.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")