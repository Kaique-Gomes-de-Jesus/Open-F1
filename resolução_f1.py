import streamlit as st
import requests
import json

st.title("OpenF1 API - Consulta de Pilotos.")
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

#Função 2 - Mostrar pilotos conhecidos
def listar_pilotos_conhecidos():
    st.subheader("Pilotos e seus números conhecidos")
    st.code("""
    Max Verstappen: #1
    Lando Norris: #4
    Gabriel Bortoleto: #5
    Isack Hadjar: #6
    Jack Doohan: #7
    Oscar Piastri: #8
    Pierre Gasly: #10
    Kimi Antonelli: #12
    Charles Leclerc: #16
    Liam Lawson: #30
    Lewis Hamilton: #44
    Oliver Bearman: #87
    """, language="python")

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
            with open(nome_arquivo, "w", encoding="utf8") as arquivo:
                json.dump(piloto, arquivo, indent=4, ensure_ascii=False)
            st.success(f"Dados do piloto salvo.")
        else:
            st.warning("Piloto não encontrado.")
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao acessar a API: {e}")

#Interface streamlit
opcao = st.sidebar.selectbox("Escolha uma opção", [
    "Buscar por número", "Listar pilotos conhecidos", "Listar todos os pilotos", "Salvar piloto em json"
])

if opcao == "Buscar por número":
    numero = st.text_input("Digite o número do piloto: ")
    if numero:
        buscar_piloto_por_numero(numero)

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
