import streamlit as st

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