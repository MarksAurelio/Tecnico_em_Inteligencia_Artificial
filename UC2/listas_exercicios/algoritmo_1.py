# Mostre o resultado de 1 + 1
x = 1
y = 1
soma = x + y
print(f"A soma de {x} + {y} = {soma}.")

# O código em Streamlit
import streamlit as st

# Variáveis (o código Python normal permanece)
x = 1
y = 1
soma = x + y

# Usando st.write() ou st.markdown() para exibir o resultado no aplicativo web
st.write(f"A soma de {x} + {y} = {soma}.")

# Alternativamente, você pode usar:
# st.markdown(f"A soma de **{x} + {y}** é igual a **{soma}**.")
