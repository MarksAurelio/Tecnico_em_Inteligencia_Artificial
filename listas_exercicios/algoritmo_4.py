# Imprima a ponteciação de 2 por 3
base = 2
cubo = 3
ponteciacao = base ** cubo
print(f"A potência de {base} elevado ao cubo {cubo} é: {ponteciacao}")

# Em Streamlit
import streamlit as st

# Lógica da potenciação
base = 2
cubo = 3
potenciacao = base ** cubo

# Configuração e exibição no Streamlit
st.title("Exemplo de Potenciação em Python")

st.write(f"A base é: **{base}**")
st.write(f"O expoente é: **{cubo}**")

# Exibindo o resultado final
st.write(f"A potência de {base} elevado ao cubo ({cubo}) é: {potenciacao}")

# Usando um cabeçalho para destacar a resposta
st.header(f"Resultado: {potenciacao}")
