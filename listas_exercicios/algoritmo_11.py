# Visualização do elementos de uma lista

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

print(mercado)

# Em Streamlit
import streamlit as st

# A lista de dados
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

# Configuração e exibição no Streamlit
st.title("Lista de Mercados Financeiros")

# Exibindo a lista usando st.write()
st.write("A lista completa de mercados é:")
st.write(mercado)

# Alternativamente, você pode usar uma lista não ordenada com st.markdown
st.subheader("Lista Detalhada")
for item in mercado:
    st.markdown(f"- {item}")
