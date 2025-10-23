# Raiz quadrada de 25

import math

numero = 25
raiz_quadrada = int(math.sqrt(numero))
print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

# Em Streamlit
import streamlit as st
import math  # A biblioteca math continua sendo necessária

# Variáveis e lógica
numero = 25
raiz_quadrada = int(math.sqrt(numero))

# Configuração e exibição no Streamlit
st.title("Calculadora de Raiz Quadrada")

st.write(f"O número é: **{numero}**")

# Exibindo o resultado final
st.success(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

# Opcional: Usando st.metric para um visual de dashboard
st.metric(label=f"Raiz Quadrada de {numero}", value=raiz_quadrada)
