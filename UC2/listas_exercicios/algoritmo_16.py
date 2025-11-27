# Extender a lista

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]
mercado.extend(["Petrobras", "BB", "Vale"])
print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

st.title("Estendendo (Adicionando Múltiplos Elementos) em uma Lista")

st.subheader("Lista Original")
st.code(mercado)

# Elementos a serem adicionados
novos_mercados = ["Petrobras", "BB", "Vale"]

# Usando extend()
mercado.extend(novos_mercados)

st.subheader("Elementos Adicionados")
st.write(f"Os elementos adicionados foram: {novos_mercados}")

st.subheader("Lista Final Após extend()")
# Exibindo a lista resultante
st.success(mercado)
