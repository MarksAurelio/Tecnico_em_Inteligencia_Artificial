# Fatiamento
# Slice
# Extrair um elemento ou um conjunto de elementos
# Para estudos em particular
# Lista de mercados
# Fatiar os três primeiros 

mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

print(mercado[0:3])

# Em Streamlit
import streamlit as st

# A lista de dados
mercado = ["Ações", "Opções", "Futuro", "Dólar", "Ouro", "Criptmoedas"]

# Criando a fatia da lista (do índice 0 até, mas não incluindo, o índice 3)
fatia_mercado = mercado[0:3]

# Configuração e exibição no Streamlit
st.title("Fatiamento de Lista (Primeiros 3 Elementos)")

# Exibindo a lista completa para contexto
st.write("Lista completa:", mercado)

# Exibindo a fatia da lista
st.info(f"Os elementos do índice 0 ao 2 (mercado[0:3]) são: **{fatia_mercado}**")

# Você também pode usar um subtítulo para a fatia
st.subheader("Primeiros Mercados")
st.write(fatia_mercado)
