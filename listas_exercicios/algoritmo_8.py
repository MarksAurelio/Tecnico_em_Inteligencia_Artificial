# O quarto elemento da lista

lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

print(f"O quarto elemento da lista é: {lista[3]}")

# Em Streamlit
import streamlit as st

# A lista de dados
lista = [10, 5, 1, 1, 2, 2, 3, 5, 10, 2, 3, 5, 10, 2, 2, 4]

# Acessando o quarto elemento (índice 3)
quarto_elemento = lista[3]

# Configuração e exibição no Streamlit
st.title("Acessando Elementos de uma Lista")

# Exibindo a lista completa (opcional, mas útil para contexto)
st.write("A lista completa é:", lista)

# Exibindo o resultado final usando a formatação original
st.info(f"O quarto elemento da lista (índice 3) é: **{quarto_elemento}**")

# Você também pode usar um índice mais visual:
st.markdown("---")
st.markdown(f"**Lista[3]** = {lista[3]}")
