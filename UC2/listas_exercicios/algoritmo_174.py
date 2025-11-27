# Imprimir todos os números de 1 até 100

for i in range(1, 101):
    print(i)

# Em Streamlit

import streamlit as st

st.title("Contagem de 1 a 100")

# 1. Gera a string com todos os números, um por linha
saida = ""
for i in range(1, 101):
    saida += str(i) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída do print)
st.subheader("Números de 1 a 100:")
st.text(saida)

# Alternativamente, para exibir de forma mais estruturada (usando listas/markdown):
st.markdown("---")
st.subheader("Exemplo de Exibição em Markdown (apenas os 10 primeiros)")

for i in range(1, 11):
    st.markdown(f"- **{i}**")
    