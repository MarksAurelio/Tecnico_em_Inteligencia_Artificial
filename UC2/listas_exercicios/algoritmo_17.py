# Ordena a lista em ordem alfabética

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

print(mercado)

mercado.sort()

print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

st.title("Ordenação de Lista (Sort)")

st.subheader("1. Lista Original")
st.code(mercado) # Exibe a lista antes da ordenação

# Ordenando a lista INPLACE (modifica a lista original)
mercado.sort()

st.subheader("2. Lista Após a Ordenação (mercado.sort())")
# Exibindo a lista resultante (agora ordenada alfabeticamente)
st.success(mercado)

st.info("O método .sort() modifica a lista original diretamente.")
