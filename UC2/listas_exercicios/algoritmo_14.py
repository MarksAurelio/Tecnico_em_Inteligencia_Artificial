# Alterar elementos numa lista

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

mercado[0:2] = ["Tesouro", "Títulos"]

print(mercado)

# Em Streamlit
import streamlit as st

# Lista original
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

st.title("Substituição de Elementos em uma Lista")

st.subheader("Lista Original")
st.code(mercado) # Exibe a lista original formatada

# Substituição dos elementos (índices 0 e 1)
# mercado[0:2] = ["Tesouro", "Títulos"]
mercado[0:2] = ["Tesouro", "Títulos"]

st.subheader("Substituição")
st.markdown("Substituindo `mercado[0:2]` por `['Tesouro', 'Títulos']`")

# Exibindo a lista resultante
st.subheader("Lista Após a Substituição")
st.success(f"A nova lista é: {mercado}")

# Exibindo o código de forma clara:
st.code("""
mercado[0:2] = ["Tesouro", "Títulos"]
""")
