""" Algoritmo 40 – Entrar com dois números inteiros e imprimir a seguinte saída: Dividendo Divisor Quociente Resto """

dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = dividendo // divisor
resto = dividendo % divisor

print("\n--- Resultados ---")
print(f"Dividendo: {dividendo}")
print(f"Divisor: {divisor}")
print(f"Quociente: {quociente}")
print(f"Resto: {resto}")

# Em Streamlit
import streamlit as st

st.title("Cálculo de Quociente e Resto (Divisão Inteira)")

# 1. Widgets de entrada para o dividendo
dividendo = st.number_input(
    "Digite o Dividendo (Número a ser dividido):",
    key="dividendo_input",
    step=1,
    value=10  # Valor inicial para teste
)

# 2. Widgets de entrada para o divisor
divisor = st.number_input(
    "Digite o Divisor (Número que divide):",
    key="divisor_input",
    step=1,
    min_value=1,  # Divisor não pode ser zero
    value=3       # Valor inicial para teste
)

# 3. Lógica de cálculo
# O Streamlit lida com o erro de divisão por zero se min_value=1 for ignorado,
# mas é sempre bom ter uma verificação.
if divisor == 0:
    st.error("Erro: O divisor não pode ser zero!")
    quociente = "Inválido"
    resto = "Inválido"
else:
    # Garantindo que os valores são inteiros para a divisão // e %
    dividendo_int = int(dividendo)
    divisor_int = int(divisor)

    quociente = dividendo_int // divisor_int
    resto = dividendo_int % divisor_int

# 4. Exibição dos resultados
st.write("---")
st.subheader("Resultados")

st.markdown(f"**Dividendo:** {int(dividendo)}")
st.markdown(f"**Divisor:** {int(divisor)}")
st.success(f"**Quociente:** {quociente}")
st.warning(f"**Resto:** {resto}")
