# Imprimir o número do índice do elemento da lista

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
print(mercado.index("Dólar"))

# Em Streamlit
import streamlit as st

# Lista
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Encontrando o Índice de um Elemento")

st.subheader("Lista de Mercados")
st.code(mercado)

# Encontrando o índice do elemento "Dólar"
indice_dolar = mercado.index("Dólar")

# Exibindo o resultado
st.info(f"O índice do elemento 'Dólar' na lista é: **{indice_dolar}**")

# Para dar mais contexto, mostramos o elemento na posição
st.markdown(f"Isso significa que `mercado[{indice_dolar}]` é igual a **'{mercado[indice_dolar]}'**.")
