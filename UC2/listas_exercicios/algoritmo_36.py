""" Enunciado: Ler dois números inteiros e imprimir a soma. Antes do resultado, deverá aparecer a mensagem: Soma. """

numero_1 = int(input("Digite o primeiro número inteiro: "))
numero_2 = int(input("Digite o segundo número inteiro: "))

soma = numero_1 + numero_2

print("Soma:", soma)

# Em Streamlit

import streamlit as st

st.title("Calculadora de Soma Simples")

# 1. Widgets de entrada para os dois números
numero_1 = st.number_input(
    "Digite o primeiro número inteiro:",
    key="num1_input",
    step=1,
    value=0
)

numero_2 = st.number_input(
    "Digite o segundo número inteiro:",
    key="num2_input",
    step=1,
    value=0
)

# 2. Lógica de cálculo (Executada sempre que os inputs mudam)
# Garantindo que os valores são tratados como inteiros
num_1_int = int(numero_1)
num_2_int = int(numero_2)

soma = num_1_int + num_2_int

# 3. Exibição do resultado
st.write("---")

# Exibindo a operação e o resultado
st.markdown(f"**Operação:** {num_1_int} + {num_2_int}")
st.success(f"**Soma:** {soma}")

# Opcional: Usando st.metric para um destaque visual
st.metric(label="Resultado da Soma", value=soma)
