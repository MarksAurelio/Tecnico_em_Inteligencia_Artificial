# Use a função count() quantas vezes apareceu a palavra Dólar

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]
mercado.append("Dólar")
print(mercado)
print(f"A quantidade de ocorrências da palavra 'Dólar' na lista é: {mercado.count("Dólar")}")

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

st.title("Adicionando e Contando Elementos em uma Lista")

st.subheader("Lista Original")
st.code(mercado)

# Adicionando o elemento
mercado.append("Dólar")

st.subheader("Lista Após Adição de 'Dólar'")
# Exibindo a nova lista
st.write(mercado)

# Contando as ocorrências de "Dólar"
ocorrencias_dolar = mercado.count("Dólar")

# Exibindo a contagem
st.info(f"A quantidade de ocorrências da palavra 'Dólar' na lista é: **{ocorrencias_dolar}**")
