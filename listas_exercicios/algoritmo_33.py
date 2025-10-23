""" Enunciado: Ler dois números inteiros e imprimi-los. """

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))   
        
print("Os números digitados foram:", numero_1, "e", numero_2)

# Em Streamlit
import streamlit as st

st.title("Entrada de Múltiplos Números Inteiros")

# 1. Entrada para o primeiro número
numero_1 = st.number_input(
    "Digite o primeiro número inteiro:",
    key="input1",  # Chave única
    step=1,
    value=0
)

# 2. Entrada para o segundo número
numero_2 = st.number_input(
    "Digite o segundo número inteiro:",
    key="input2",  # Chave única
    step=1,
    value=0
)

# 3. Exibindo os resultados
st.write("---")

# Certifica-se de que a exibição é executada
# O Streamlit recarrega o script sempre que qualquer um dos inputs é alterado.
if numero_1 is not None and numero_2 is not None:
    st.info(f"Os números digitados foram: **{int(numero_1)}** e **{int(numero_2)}**")
else:
    st.warning("Aguardando a digitação dos números...")
    