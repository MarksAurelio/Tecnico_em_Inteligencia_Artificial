# Uma lista é uma sequência ordenada
# Os elementos da lista são sempre associados a índice
# A facilidade e a simplicidade das listas do python é única
# A lista tem como ínicio o índice 0

""" lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]
print(f"O primeiro elemento da lista é: {lista[0]}")
print(f"O segundo elemento da lista é: {lista[1]}") """

import streamlit as st

# A lista de dados
lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

# Título do aplicativo
st.title("Acessando Elementos de uma Lista com Streamlit")

# Exibindo a lista completa
st.header("A Lista Original:")
st.code(lista) # Usa st.code() para exibir a lista formatada como código

# Exibindo o primeiro elemento
primeiro_elemento = lista[0]
st.write(f"O primeiro elemento da lista é: **{primeiro_elemento}**")

# Exibindo o segundo elemento
segundo_elemento = lista[1]
st.write(f"O segundo elemento da lista é: **{segundo_elemento}**")

# Você também pode usar st.markdown para destacar mais
st.markdown(f"O terceiro elemento é: **{lista[2]}**")
