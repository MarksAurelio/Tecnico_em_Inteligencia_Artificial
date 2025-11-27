""" Algoritmo 93 - Entrar com um número e imprimir a raiz quadrada do número caso ele seja positivo e o quadrado do número caso ele seja negativo. """

import math

numero = float(input("Digite um número: "))
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é:", raiz_quadrada)
else:
    quadrado = numero ** 2
    print("O quadrado de", numero, "é:", quadrado)  

# Em Streamlit
import streamlit as st
import math

st.title("Raiz Quadrada ou Quadrado")

# 1. Widget de entrada para o número real
numero = st.number_input(
    "Digite um número (positivo ou negativo):",
    key="num_input",
    value=0.0,
    format="%.2f"
)

# 2. Lógica Condicional (Executada sempre que o input muda)
st.write("---")
st.subheader("Resultado")

if numero >= 0:
    # Se o número for positivo ou zero, calcula a raiz quadrada
    raiz_quadrada = math.sqrt(numero)

    st.success(f"O número digitado ({numero:.2f}) é **positivo ou zero**.")
    st.info(f"A **raiz quadrada** de {numero:.2f} é: **{raiz_quadrada:.4f}**")

    st.metric(label="Raiz Quadrada", value=f"{raiz_quadrada:.4f}")
else:
    # Se o número for negativo, calcula o quadrado
    quadrado = numero ** 2

    st.warning(f"O número digitado ({numero:.2f}) é **negativo**.")
    st.info(f"O **quadrado** de {numero:.2f} é: **{quadrado:.4f}**")

    st.metric(label="Quadrado", value=f"{quadrado:.4f}")
