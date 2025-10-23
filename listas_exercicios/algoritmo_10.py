# Total de elementos na lista

lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

print(f"O total de dados da lista é: {len(lista)}")

# Em Streamlit
import streamlit as st

# A lista de dados
lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

# Calculando o tamanho da lista
tamanho_lista = len(lista)

# Configuração e exibição no Streamlit
st.title("Tamanho da Lista")

# Exibindo a lista completa (opcional, mas útil para contexto)
st.write("A lista completa é:", lista)

# Exibindo o resultado final
st.info(f"O total de dados (comprimento) da lista é: **{tamanho_lista}**")

# Usando st.metric para um visual de dashboard (destaque)
st.metric(label="Total de Elementos na Lista", value=tamanho_lista)
