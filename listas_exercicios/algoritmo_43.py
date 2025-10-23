""" Algoritmo 43 – Entrar com um número e imprimir o logaritmo desse número na base 10. """

import math

numero = float(input("Digite um número positivo: "))
logaritmo = math.log10(numero)
print(f"O logaritmo de {numero} na base 10 é: {logaritmo}")

# Em Streamlit
import streamlit as st
import math

st.title("Cálculo de Logaritmo (Base 10)")

# 1. Widget de entrada para o número positivo
# O 'min_value=0.000001' é usado para evitar o logaritmo de zero ou números negativos.
numero = st.number_input(
    "Digite um número positivo:",
    key="log_input",
    min_value=0.000001,  # Deve ser maior que zero
    value=10.0,          # Valor inicial para teste
    format="%.4f"
)

# 2. Lógica de Cálculo (Executada sempre que o input muda)
logaritmo = 0.0
erro = None

if numero > 0:
    try:
        logaritmo = math.log10(numero)
    except ValueError:
        # Esta exceção só ocorreria se min_value fosse violado ou fosse um NaN
        erro = "Número inválido para cálculo de logaritmo (deve ser > 0)."
else:
    erro = "O número deve ser positivo (maior que zero)."

# 3. Exibição dos Resultados
st.write("---")

if erro:
    st.error(erro)
else:
    st.info(f"O número digitado é: **{numero:.4f}**")
    
    # Exibindo o resultado final
    st.success(f"O logaritmo de {numero:.4f} na base 10 é: **{logaritmo:.6f}**")

    # Destaque visual
    st.metric(label="Log₁₀(Número)", value=f"{logaritmo:.6f}")
    