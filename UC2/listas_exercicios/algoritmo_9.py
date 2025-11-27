# O último elemento da lista

lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

print(f"O último elemento da lista é: {lista[-1]}")

# Em Streamlit
import streamlit as st

# A lista de dados
lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

# Acessando o último elemento (índice -1)
ultimo_elemento = lista[-1]

# Configuração e exibição no Streamlit
st.title("Acessando o Último Elemento da Lista")

# Exibindo a lista completa
st.write("A lista completa é:", lista)

# Exibindo o resultado final
st.success(f"O último elemento da lista (acessado com o índice -1) é: **{ultimo_elemento}**")

# Você pode mostrar a posição do último elemento
st.markdown(f"O comprimento da lista é **{len(lista)}**. O último elemento está na posição: **{len(lista) - 1}**.")
