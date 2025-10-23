""" Enunciado: Ler um número inteiro e imprimi-lo. """

numero = int(input("Digite um número inteiro: "))

print("O número digitado foi:", numero)

# Em Streamlit
import streamlit as st

st.title("Entrada de Dados Simples")

# 1. Usando st.number_input para garantir que seja um número inteiro
# O 'value=0' define o valor inicial.
numero = st.number_input(
    "Digite um número inteiro:",
    min_value=None,  # Sem mínimo definido
    max_value=None,  # Sem máximo definido
    step=1,          # Passo de 1 para garantir inteiros
    value=0          # Valor inicial
)

# A variável 'numero' já contém o valor digitado pelo usuário.
# O Streamlit recarrega o script sempre que o valor muda,
# então esta linha é executada automaticamente com o novo valor.

# 2. Exibindo o resultado
st.write("---")
st.info(f"O número digitado foi: **{int(numero)}**")
