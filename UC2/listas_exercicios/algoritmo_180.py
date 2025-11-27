# Criar um algoritmo que imprima os números de 120 a 300

for i in range(120, 301):
    print(i)

# Em Streamlit
import streamlit as st

st.title("Contagem de 120 a 300")

# 1. Gera a string com todos os números
saida = ""
# range(120, 301) inclui o 120 e vai até, mas não inclui, o 301, ou seja, até 300.
for i in range(120, 301):
    saida += str(i) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída do print)
st.subheader("Números de 120 a 300:")
st.text(saida)

# Exibição de um resumo ou parte da sequência
st.markdown("---")
st.markdown(f"**Primeiros números:** {', '.join(map(str, range(120, 126)))}...")
st.markdown(f"**Últimos números:** ..., {', '.join(map(str, range(295, 301)))}")
