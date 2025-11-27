""" Algoritmo 95 - Entrar com um número e informar se ele é ou não divisível por 5. """

numero = int(input("Digite um número: "))
if numero % 5 == 0:
    print(f"O número {numero} é divisível por 5.")
else:
    print(f"O número {numero} não é divisível por 5.")

# Em Streamlit
import streamlit as st

st.title("Verificação de Divisibilidade por 5")

# 1. Widget de entrada para o número inteiro
numero = st.number_input(
    "Digite um número inteiro:",
    key="num_input",
    step=1,
    value=25  # Valor inicial
)

# 2. Lógica Condicional (Executada sempre que o input muda)
num_int = int(numero)
st.write("---")
st.subheader(f"Verificando se {num_int} é Divisível por 5")

if num_int % 5 == 0:
    # Se o resto da divisão por 5 for 0
    st.success(f"O número **{num_int}** é **divisível por 5**.")
else:
    # Se o resto da divisão por 5 não for 0
    resto = num_int % 5
    st.warning(f"O número **{num_int}** **não é divisível por 5**.")
    st.caption(f"O resto da divisão por 5 é: {resto}")
       