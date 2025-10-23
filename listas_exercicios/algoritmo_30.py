""" Enunciado: Criar um algoritmo que imprima o produto entre
entre dois números. """

numero1 = 5
numero2 = 10

produto = numero1 * numero2

print("O produto entre", numero1, "e", numero2, "é:", produto)

# Em Streamlit
import streamlit as st

# Variáveis
numero1 = 5
numero2 = 10

# Cálculo
produto = numero1 * numero2

# Configuração e exibição no Streamlit
st.title("Cálculo de Produto")

# Exibindo os números
st.write(f"O primeiro número é: **{numero1}**")
st.write(f"O segundo número é: **{numero2}**")

# Exibindo o resultado final
st.success(f"O produto entre {numero1} e {numero2} é: **{produto}**")

# Opcional: Usando st.metric para um visual de dashboard
st.metric(label=f"{numero1} x {numero2}", value=produto)
