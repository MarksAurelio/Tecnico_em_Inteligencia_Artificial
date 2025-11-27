# Imprimir os 100 primeiros pares

for i in range(1, 101):
    print(i * 2)
    
# Em Streamlit
import streamlit as st

st.title("Múltiplos de 2 (de 1 a 100)")

# 1. Gera a string com todos os resultados (2, 4, 6, ..., 200)
saida = ""
for i in range(1, 101):
    resultado = i * 2
    saida += str(resultado) + "\n"

# 2. Exibe o resultado como um bloco de texto (simulando a saída sequencial)
st.subheader("Resultados (2 x i, para i de 1 a 100):")
st.text(saida)

# Alternativamente, para exibir de forma mais estruturada (apenas os 10 primeiros):
st.markdown("---")
st.subheader("Exemplo de Exibição Detalhada (10 Primeiros)")

for i in range(1, 11):
    resultado = i * 2
    st.markdown(f"**{i}** x 2 = **{resultado}**")
    