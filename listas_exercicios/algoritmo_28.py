""" Enunciado: Imprimir a mensagem: "É PRECISO FAZER TODOS OS ALGORITMOS PARA
APRENDER". """

print("É PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER")

# Em Streamlit
import streamlit as st

# A frase
frase = "É PRECISO FAZER TODOS OS ALGORITMOS PARA APRENDER"

st.title("Lema de Aprendizado")

# Exibindo a frase com destaque
st.header(frase)

# Usando um alerta para enfatizar a importância
st.warning("⚠️ **ATENÇÃO:** " + frase)
