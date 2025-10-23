""" Algoritmo 41 – Entrar com quatro números e imprimir a média ponderada , sabendo-se que os pesos são respectivamente: 1, 2, 3 e 4. """

pesos = [1, 2, 3, 4]
soma_produtos = 0
soma_pesos = 0

for i in range(4):
  numeros = float(input(f"Digite o {i+1}° número: "))
  peso = pesos[i]
  soma_produtos += numeros * peso
  soma_pesos += peso
  media_ponderada = soma_produtos / soma_pesos
  print(f"A média ponderada é: {media_ponderada:.2f}")

# Em Streamlit
import streamlit as st

st.title("Cálculo de Média Ponderada Fixa")

# Variáveis fixas
pesos = [1, 2, 3, 4]
num_entradas = len(pesos)
soma_pesos = sum(pesos) # Soma total dos pesos: 1 + 2 + 3 + 4 = 10

st.write(f"Esta média utiliza **{num_entradas}** números com os seguintes pesos: **{pesos}** (Soma dos pesos = {soma_pesos}).")

st.markdown("---")

# 1. Criação dos widgets de entrada e coleta dos números
# Usamos um dicionário para armazenar os valores de entrada
numeros_digitados = {}
soma_produtos = 0

# Criamos as entradas em colunas para organização
cols = st.columns(num_entradas)

for i in range(num_entradas):
    peso_atual = pesos[i]

    # Cria o widget de entrada na coluna correspondente
    numero = cols[i].number_input(
        f"Número {i+1} (Peso {peso_atual}):",
        key=f"num_{i}",
        value=0.0,
        format="%.2f"
    )

    numeros_digitados[f"num_{i}"] = numero

    # Calcula a soma dos produtos (Número * Peso)
    soma_produtos += numero * peso_atual


# 2. Lógica de cálculo (executada após a coleta de todos os inputs)
if soma_pesos > 0:
    media_ponderada = soma_produtos / soma_pesos
else:
    media_ponderada = 0

# 3. Exibição do resultado
st.markdown("---")

st.subheader("Resultados:")

st.info(f"Soma dos Produtos (Σ(Número * Peso)): **{soma_produtos:.2f}**")
st.success(f"A média ponderada é: **{media_ponderada:.2f}**")

# Destaque visual
st.metric(label="Média Ponderada Final", value=f"{media_ponderada:.2f}")
