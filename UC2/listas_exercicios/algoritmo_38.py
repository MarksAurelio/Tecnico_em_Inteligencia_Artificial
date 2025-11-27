""" Algoritmo 38 – Ler um número real e imprimir a parte terça deste número """

numero_real = float(input("Digite um número real: "))

terca_parte = numero_real / 3

print(f"A terça parte de {numero_real} é: {terca_parte}")

# Em Streamlit
import streamlit as st

st.title("Cálculo da Terça Parte de um Número Real")

# 1. Widget de entrada para o número real (float)
# Ao omitir 'step=1', permite-se a entrada de números decimais
numero_real = st.number_input(
    "Digite um número real (com casas decimais):",
    key="real_input",
    value=0.0,       # Valor inicial como float
    format="%.2f"    # Formato para exibir com 2 casas decimais no widget
)

# 2. Lógica de cálculo (Executada sempre que o input muda)
terca_parte = numero_real / 3

# 3. Exibição do resultado
st.write("---")

st.info(f"O número digitado foi: **{numero_real:.2f}**")

# Exibindo o resultado final, formatado para melhor leitura
st.success(f"A terça parte de {numero_real:.2f} é: **{terca_parte:.4f}**")
