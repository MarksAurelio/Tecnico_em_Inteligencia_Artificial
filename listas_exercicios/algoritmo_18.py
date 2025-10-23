# Ordena ignorando a diferença entre maiúsculas e minúsculas (de forma case-insensitive)

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
print(mercado)
mercado.sort(key=str.casefold)
print(mercado)

# Em Streamlit
import streamlit as st

# Lista original (com letras maiúsculas e minúsculas misturadas)
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Ordenação de Lista Sem Diferenciar Maiúsculas/Minúsculas")

st.subheader("1. Lista Original")
st.code(mercado) # Exibe a lista antes da ordenação

# Ordenando a lista INPLACE, usando str.casefold para ignorar o caso das letras
mercado.sort(key=str.casefold)

st.subheader("2. Lista Após a Ordenação (mercado.sort(key=str.casefold))")
# Exibindo a lista resultante (agora ordenada de forma case-insensitive)
st.success(mercado)

st.info("Com `key=str.casefold`, 'Ações' e 'opções' são tratadas de forma igual, resultando em uma ordem alfabética mais 'natural'.")
