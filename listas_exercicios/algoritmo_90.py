""" Algoritmo 90 – Entrar com um número e imprimi-lo caso seja maior que 20 """

numero = int(input("Digite um número: "))
if numero > 20:
    print(numero)  
else:
    print("Número menor ou igual a 20.")

# Em Streamlit
import streamlit as st

st.title("Verificação de Número Maior que 20")

# 1. Widget de entrada para o número inteiro
numero = st.number_input(
    "Digite um número inteiro:",
    key="num_input",
    step=1,
    value=0  # Valor inicial
)

# 2. Lógica Condicional (Executada sempre que o input muda)
st.write("---")
st.subheader("Resultado da Verificação")

if numero > 20:
    # Se a condição for VERDADEIRA
    st.success(f"O número digitado ({int(numero)}) é **maior que 20**.")
    # Exibe o próprio número, conforme o print original
    st.write(int(numero))
else:
    # Se a condição for FALSA (menor ou igual a 20)
    st.warning(f"O número digitado ({int(numero)}) é **menor ou igual a 20**.")
    