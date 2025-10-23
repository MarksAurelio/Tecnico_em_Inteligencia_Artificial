""" Enunciado: Ler um número inteiro e imprimir seu sucessor e seu antecessor. """

numero = int(input("Digite um número inteiro: "))

sucessor = numero + 1
antecessor = numero - 1

print("O número digitado foi:", numero)
print("O sucessor de", numero, "é:", sucessor)
print("O antecessor de", numero, "é:", antecessor)

# Em Streamlit

import streamlit as st

st.title("Sucessor e Antecessor")

# 1. Entrada do número pelo usuário
numero = st.number_input(
    "Digite um número inteiro:",
    min_value=None,
    step=1,
    value=10  # Valor inicial para facilitar o teste
)

# O Streamlit trata o valor de 'numero' como float por padrão.
# Convertendo para int para garantir a precisão, embora a aritmética funcione.
numero_int = int(numero)

# 2. Lógica de cálculo
sucessor = numero_int + 1
antecessor = numero_int - 1

# 3. Exibindo os resultados
st.write("---")

st.info(f"O número digitado foi: **{numero_int}**")

# Exibindo o sucessor
st.success(f"O **sucessor** de {numero_int} é: **{sucessor}**")

# Exibindo o antecessor
st.warning(f"O **antecessor** de {numero_int} é: **{antecessor}**")
