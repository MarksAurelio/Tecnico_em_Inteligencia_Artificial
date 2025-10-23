""" Algoritmo 91 – Construir um algoritmo que leia dois valores numéricos inteiros e efetue a adição; caso o resultado seja maior que 10, apresentá-lo. """

numero_1 = int(input("Digite o primeiro número: "))
numero_2 = int(input("Digite o segundo número: "))

soma = numero_1 + numero_2

if soma > 10:
    print("A soma é:", soma)        
else:
    print("A soma é menor ou igual a 10.")

# Em Streamlit
import streamlit as st

st.title("Soma e Condição (Maior que 10)")

# 1. Widgets de entrada para os dois números
numero_1 = st.number_input(
    "Digite o primeiro número inteiro:",
    key="num1_input",
    step=1,
    value=5
)

numero_2 = st.number_input(
    "Digite o segundo número inteiro:",
    key="num2_input",
    step=1,
    value=5
)

# 2. Lógica de cálculo (Executada sempre que os inputs mudam)
num1_int = int(numero_1)
num2_int = int(numero_2)
soma = num1_int + num2_int

st.write(f"**Operação:** {num1_int} + {num2_int}")
st.metric(label="Soma Total", value=soma)

# 3. Lógica Condicional e Exibição
st.write("---")
st.subheader("Resultado da Verificação")

if soma > 10:
    # Se a condição for VERDADEIRA
    st.success(f"A soma é: **{soma}**")
    st.markdown("A soma é **maior que 10**.")
else:
    # Se a condição for FALSA (menor ou igual a 10)
    st.warning("A soma é **menor ou igual a 10**.")
    st.markdown(f"A soma é: **{soma}**.") # O print original só mostra a soma se > 10, mas aqui a mostramos para contexto.
    