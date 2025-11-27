# Apagar elementos da lista

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
print(mercado)
mercado.clear()
print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Limpando uma Lista (.clear())")

st.subheader("1. Lista Original")
st.code(mercado) # Exibe a lista antes da limpeza

# Limpando a lista
st.markdown("Limpando a lista usando `mercado.clear()`...")
mercado.clear()

st.subheader("2. Lista Após a Limpeza")
# Exibindo a lista resultante (agora vazia)
st.error(mercado)

st.info("O método `.clear()` remove todos os elementos, resultando em uma lista vazia: `[]`.")
