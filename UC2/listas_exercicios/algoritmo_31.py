""" Enunciado: Criar um algoritmo que imprima a média aritmética entre os números
8, 9 e 7. """

numero_1 = 8
numero_2 = 9
numero_3 = 7   

media = (numero_1 + numero_2 + numero_3) / 3

print("A média aritmética entre", numero_1, ",", numero_2, "e", numero_3, "é:", media)

# Em Streamlit
import streamlit as st

# Variáveis
numero_1 = 8
numero_2 = 9
numero_3 = 7

# Cálculo da média
media = (numero_1 + numero_2 + numero_3) / 3

# Configuração e exibição no Streamlit
st.title("Cálculo de Média Aritmética")

# Exibindo os números envolvidos
st.write(f"Os números para o cálculo são: **{numero_1}**, **{numero_2}** e **{numero_3}**.")

# Exibindo o resultado final
st.success(f"A média aritmética entre {numero_1}, {numero_2} e {numero_3} é: **{media:.2f}**")

# Opcional: Usando st.metric para destacar o resultado
st.metric(label="Média Calculada", value=f"{media:.2f}") # Formatado para 2 casas decimais
