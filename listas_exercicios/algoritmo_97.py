""" Algoritmo 97 - Entrar comum número e informar se ele é divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes. """

numero = int(input("Digite um número: "))
if numero % 10 == 0:
    print(f"O número {numero} é divisível por 10.")
elif numero % 5 == 0:
    print(f"O número {numero} é divisível por 5.")
elif numero % 2 == 0:
    print(f"O número {numero} é divisível por 2.")
else:
    print(f"O número {numero} não é divisível por 10, por 5 ou por 2.")

# Em Streamlit
import streamlit as st

st.title("Verificação de Divisibilidade por 10, 5 ou 2")

# 1. Widget de entrada para o número inteiro
numero = st.number_input(
    "Digite um número inteiro:",
    key="num_input",
    step=1,
    value=15  # Valor inicial para teste
)

# 2. Lógica Condicional (Executada sempre que o input muda)
num_int = int(numero)
st.write("---")
st.subheader(f"Verificando {num_int}")

# Inicializa a variável de resultado
resultado = ""

if num_int % 10 == 0:
    # Primeira condição (é divisível por 10)
    resultado = f"O número **{num_int}** é **divisível por 10**."
    st.success(resultado)

elif num_int % 5 == 0:
    # Segunda condição (é divisível por 5, mas não por 10)
    resultado = f"O número **{num_int}** é **divisível por 5** (mas não por 10)."
    st.info(resultado)

elif num_int % 2 == 0:
    # Terceira condição (é divisível por 2, mas não por 10 nem por 5)
    resultado = f"O número **{num_int}** é **divisível por 2** (mas não por 10 ou 5)."
    st.warning(resultado)

else:
    # Nenhuma das condições anteriores é verdadeira
    resultado = f"O número **{num_int}** **não é divisível por 10, por 5 ou por 2**."
    st.error(resultado)

st.caption("A ordem de verificação (10, 5, 2) é mantida.")
