# Remove

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

mercado.remove("Ouro")

print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Remoção de Elemento em uma Lista")

st.subheader("1. Lista Original")
st.code(mercado)

# Removendo o elemento "Ouro"
st.markdown("Removendo **'Ouro'** da lista usando `mercado.remove('Ouro')`...")
mercado.remove("Ouro")

st.subheader("2. Lista Após a Remoção")
# Exibindo a lista resultante
st.success(mercado)

st.info("O método `.remove()` remove a primeira ocorrência do valor especificado.")
