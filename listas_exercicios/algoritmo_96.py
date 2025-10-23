""" Algoritmo 96 - Entrar com um número e informar se ele é divisível por 3 e por 7. """

numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 7 == 0:
    print(f"O número {numero} é divisível por 3 e por 7.")
else:
    print(f"O número {numero} não é divisível por 3 e por 7.")

# Em Streamlit
import streamlit as st

st.title("Verificação de Divisibilidade por 3 e 7")

# 1. Widget de entrada para o número inteiro
numero = st.number_input(
    "Digite um número inteiro:",
    key="num_input",
    step=1,
    value=21  # Valor inicial para teste
)

# 2. Lógica Condicional (Executada sempre que o input muda)
num_int = int(numero)
st.write("---")
st.subheader(f"Verificando se {num_int} é Divisível por 3 e 7")

# A condição verifica se o resto da divisão por 3 é zero E o resto da divisão por 7 é zero
if num_int % 3 == 0 and num_int % 7 == 0:
    st.success(f"O número **{num_int}** é **divisível por 3 e por 7**.")
    st.caption("Isso significa que ele é divisível por 21.")
else:
    st.warning(f"O número **{num_int}** **não é divisível por 3 e por 7**.")
    # Exibe o resto para dar mais contexto (opcional)
    resto_3 = num_int % 3
    resto_7 = num_int % 7
    st.caption(f"Resto da divisão por 3: {resto_3} | Resto da divisão por 7: {resto_7}")
    