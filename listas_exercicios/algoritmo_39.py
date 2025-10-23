""" Algoritmo 39 – Entra com dois números reais e imprimir a média aritmética com a mensagem “média” """

numero_real_1 = float(input("Digite o primeiro número real: "))
numero_real_2 = float(input("Digite o segundo número real: "))

media = (numero_real_1 + numero_real_2) / 2

print(f"A média aritmética de {numero_real_1} e {numero_real_2} é: {media}")

# Em Streamlit
import streamlit as st

st.title("Média Aritmética de Dois Números Reais")

# 1. Widget de entrada para o primeiro número real
numero_real_1 = st.number_input(
    "Digite o primeiro número real:",
    key="real1_input",
    value=0.0,
    format="%.2f"
)

# 2. Widget de entrada para o segundo número real
numero_real_2 = st.number_input(
    "Digite o segundo número real:",
    key="real2_input",
    value=0.0,
    format="%.2f"
)

# 3. Lógica de cálculo (Executada sempre que os inputs mudam)
# O Streamlit já trata os valores como floats.
media = (numero_real_1 + numero_real_2) / 2

# 4. Exibição do resultado
st.write("---")

if numero_real_1 is not None and numero_real_2 is not None:
    st.info(f"Os números digitados foram: **{numero_real_1:.2f}** e **{numero_real_2:.2f}**")

    # Exibindo o resultado final, formatado para melhor leitura
    st.success(f"A média aritmética de {numero_real_1:.2f} e {numero_real_2:.2f} é: **{media:.4f}**")

    # Destaque visual
    st.metric(label="Média Calculada", value=f"{media:.4f}")
