# Imprimir todos os números de 100 até 1

for i in range(100, 0, -1):
    print(i)

# Em Streamlit
import streamlit as st

st.title("Contagem Regressiva de 100 a 1")

# 1. Gera a string com todos os números em ordem decrescente
saida = ""
for i in range(100, 0, -1):
    saida += str(i) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída do print)
st.subheader("Números de 100 a 1:")
st.text(saida)

# Alternativamente, para exibir de forma mais estruturada (apenas os 10 primeiros):
st.markdown("---")
st.subheader("Exemplo de Exibição Detalhada (10 Primeiros)")

for i in range(100, 90, -1):
    st.markdown(f"**{i}**")
