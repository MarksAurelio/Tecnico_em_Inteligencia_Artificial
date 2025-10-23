""" Algoritmo 42 – Entrar com um ângulo em graus e imprimir: seno, co-seno, tangente, secante, co-secante e co-tangente deste ângulo. Use o módulo math. """

import math

angulo_graus = float(input("Digite o ângulo em graus: "))

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

secante = 1 / cosseno
cossecante = 1 / seno
cotangente = 1 / tangente

print("\n--- Resultados ---")
print(f"Ângulo em Graus: {angulo_graus}")
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")
print(f"Secante: {secante:.2f}")
print(f"Cossecante: {cossecante:.2f}")
print(f"Cotangente: {cotangente:.2f}")

# Em Streamlit
import streamlit as st
import math

st.title("Calculadora Trigonométrica")

# 1. Widget de entrada para o ângulo em graus
angulo_graus = st.number_input(
    "Digite o ângulo em graus:",
    key="angulo_input",
    value=45.0,  # Valor inicial para teste (45 graus)
    format="%.2f"
)

# 2. Lógica de Cálculo (Executada sempre que o ângulo muda)

angulo_radianos = math.radians(angulo_graus)

seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Verificação para evitar divisão por zero (especialmente para a tangente, seno e cosseno)
# Usaremos um valor placeholder se o resultado for muito próximo de zero.

# Secante (1 / cosseno)
if abs(cosseno) < 1e-9:
    secante = "Indefinido (Cosseno ≈ 0)"
else:
    secante = 1 / cosseno

# Cossecante (1 / seno)
if abs(seno) < 1e-9:
    cossecante = "Indefinido (Seno ≈ 0)"
else:
    cossecante = 1 / seno

# Cotangente (1 / tangente)
if abs(tangente) < 1e-9:
    cotangente = "Indefinido (Tangente ≈ 0)"
else:
    cotangente = 1 / tangente

# 3. Exibição dos Resultados
st.write("---")
st.subheader("Resultados")

# Exibindo o ângulo e o valor em radianos
st.metric("Ângulo em Graus", f"{angulo_graus:.2f}°")
st.caption(f"Ângulo em Radianos: {angulo_radianos:.4f}")

# Usando colunas para organizar as funções principais (seno, cosseno, tangente)
col1, col2, col3 = st.columns(3)
col1.success(f"Seno: **{seno:.4f}**")
col2.success(f"Cosseno: **{cosseno:.4f}**")
col3.success(f"Tangente: **{tangente:.4f}**")

st.markdown("---")

# Usando colunas para organizar as funções recíprocas
st.subheader("Funções Recíprocas")
col4, col5, col6 = st.columns(3)

# Formatação condicional para as funções recíprocas
def format_reciprocal(valor):
    if isinstance(valor, str):
        return valor
    return f"{valor:.4f}"

col4.warning(f"Secante: **{format_reciprocal(secante)}**")
col5.warning(f"Cossecante: **{format_reciprocal(cossecante)}**")
col6.warning(f"Cotangente: **{format_reciprocal(cotangente)}**")
