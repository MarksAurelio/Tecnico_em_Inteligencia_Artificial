# Criar um algoritmo que imprima os números pares no intervalo de 1 a 600

for i in range(2, 601, 2):
    print(i)
    
# Em Streamlit
import streamlit as st

st.title("Números Pares de 2 a 600")

# 1. Gera a string com todos os números pares
saida = ""
for i in range(2, 601, 2):
    saida += str(i) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída do print)
st.subheader("Sequência de Números Pares:")
st.text(saida)

# Alternativamente, para exibir de forma mais estruturada (apenas os 10 primeiros):
st.markdown("---")
st.subheader("Exemplo de Exibição Detalhada (10 Primeiros)")

for i in range(2, 21, 2):
    st.markdown(f"- **{i}**")
    