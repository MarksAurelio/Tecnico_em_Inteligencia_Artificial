""" Algoritmo 94 - Entrar com um número e imprimir uma das mensagens: é múltiplo de 3 ou não é múltiplo de 3. """

numero = int(input("Digite um número: "))
if numero % 3 == 0:
    print(f"O número {numero} é múltiplo de 3.")
else:
    print(f"O número {numero} não é múltiplo de 3.")    

# Em Streamlit
import streamlit as st

st.title("Verificação de Múltiplo de 3")

# 1. Widget de entrada para o número inteiro
numero = st.number_input(
    "Digite um número inteiro:",
    key="num_input",
    step=1,
    value=15  # Valor inicial
)

# 2. Lógica Condicional (Executada sempre que o input muda)
num_int = int(numero)
st.write("---")
st.subheader(f"Verificando se {num_int} é Múltiplo de 3")

if num_int % 3 == 0:
    # Se o resto da divisão por 3 for 0
    st.success(f"O número **{num_int}** é **múltiplo de 3**.")
else:
    # Se o resto da divisão por 3 não for 0
    resto = num_int % 3
    st.warning(f"O número **{num_int}** **não é múltiplo de 3**.")
    st.caption(f"O resto da divisão por 3 é: {resto}")
