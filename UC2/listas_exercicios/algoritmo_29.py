""" Enunciado: Imprimir seu nome. """

print("Marks Aurélio")

# Em Streamlit
import streamlit as st

nome = "Marcus Aurelius" # Assumindo a grafia "Marcus Aurelius"
# Se você quis dizer "Mark Zuckerberg" ou outro, ajuste a variável nome.

st.title("Nome em Destaque")

# Exibindo o nome como um texto simples
st.write(nome)

# Usando um subtítulo para dar um pouco mais de ênfase
st.subheader(f"Autor: {nome}")
