# Inserir elemento na lista

mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]
mercado.insert(2, "Fundo de Investimento")
print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "opções", "Futuro", "Dólar", "Ouro", "criptmoedas"]

st.title("Inserção de Elemento em uma Lista")

st.subheader("1. Lista Original")
st.code(mercado)

# Inserindo "Fundo de Investimento" na posição 2
st.markdown("Inserindo **'Fundo de Investimento'** no índice 2 usando `mercado.insert(2, 'Fundo de Investimento')`...")
mercado.insert(2, "Fundo de Investimento")

st.subheader("2. Lista Após a Inserção")
# Exibindo a lista resultante
st.success(mercado)

st.info("O novo elemento foi adicionado na terceira posição (índice 2), empurrando os demais.")
