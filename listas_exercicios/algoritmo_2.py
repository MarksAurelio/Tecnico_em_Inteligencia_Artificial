# Imprima a divisão de 3 por 2
dividendo = 3
divisor = 2
quociente = dividendo // divisor
resto = dividendo % divisor
print(f"A divisão de {dividendo} / {divisor} = {quociente} e o resto é: {resto}")

# O código em Streamlit
import streamlit as st

# Lógica da divisão
dividendo = 3
divisor = 2
quociente = dividendo // divisor
resto = dividendo % divisor

# Exibindo o resultado no aplicativo web
st.title("Exemplo de Divisão em Python")

st.write(f"O dividendo é: **{dividendo}**")
st.write(f"O divisor é: **{divisor}**")

# Usando st.write() ou st.markdown() para exibir o resultado final
st.write(f"A divisão de {dividendo} / {divisor} = {quociente} e o resto é: {resto}")

# Se quiser usar Markdown para destacar:
st.markdown(f"---")
st.markdown(f"Resultado: O **quociente** é **{quociente}** e o **resto** é **{resto}**.")
