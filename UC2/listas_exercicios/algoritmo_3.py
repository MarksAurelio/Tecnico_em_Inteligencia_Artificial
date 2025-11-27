# Imprima a subtração 4 - 11
minuendo = 4
subtraendo = 11
diferenca = minuendo - subtraendo
print(f"A subtração de {minuendo} - {subtraendo} = {diferenca}")

# O código em Streamlit
import streamlit as st

# Lógica da subtração
minuendo = 4
subtraendo = 11
diferenca = minuendo - subtraendo

# Exibindo o resultado no aplicativo web
st.title("Exemplo de Subtração em Python")

st.write(f"O minuendo é: **{minuendo}**")
st.write(f"O subtraendo é: **{subtraendo}**")

# Usando st.write() para exibir o resultado final
st.write(f"A subtração de {minuendo} - {subtraendo} = {diferenca}")

# Você pode adicionar um pouco de destaque:
st.success(f"A diferença é: {diferenca}")
