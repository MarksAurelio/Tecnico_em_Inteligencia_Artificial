# Imprimir os múltiplos de 5, no intervalo de 1 até 500

for i in range(5, 501, 5):
    print(i)

# Em Streamlit
import streamlit as st

st.title("Múltiplos de 5 (de 5 a 500)")

# 1. Gera a string com todos os números
saida = ""
for i in range(5, 501, 5):
    saida += str(i) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída do print)
st.subheader("Números (Múltiplos de 5):")
st.text(saida)

# Alternativamente, para exibir de forma mais estruturada (os 10 primeiros):
st.markdown("---")
st.subheader("Exemplo de Exibição Detalhada (10 Primeiros)")

for i in range(5, 51, 5):
    st.markdown(f"- **{i}**")
    