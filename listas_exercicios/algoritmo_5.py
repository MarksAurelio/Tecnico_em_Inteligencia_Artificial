# Valor de Pi
pi = 3.14
print(f"O valor de PI é igual a: {pi} e o tipo de variável é {type(pi)}.")

# Em Streamlit
import streamlit as st

# Variável
pi = 3.14

# Exibindo o resultado no aplicativo web
st.title("Exibindo o Valor de PI")

# Exibindo a string formatada
st.write(f"O valor de PI é igual a: {pi}")

# Exibindo o tipo da variável
st.info(f"O tipo de variável de PI é: {type(pi)}.")

# Outra forma de exibir o valor com destaque
st.metric(label="Valor de PI", value=pi)
